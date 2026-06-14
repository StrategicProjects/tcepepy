"""Offline endpoint catalog: discovery, parameter mapping and validation.

Everything here reads from the bundled
``_data/tcepe_dados_abertos_catalogo.json`` and works without network access
(the live API is geo-restricted to Brazilian IP addresses). Mirrors
``catalog.R`` + ``introspection.R`` from the R package.
"""

from __future__ import annotations

import json
import re
from functools import lru_cache
from typing import Any, Dict, List, Optional

import pandas as pd

try:  # Python 3.9+: importlib.resources.files
    from importlib.resources import files as _resource_files
except ImportError:  # pragma: no cover
    _resource_files = None  # type: ignore

from .naming import clean_name

__all__ = ["catalog", "endpoint", "params", "fields"]

_NON_ALNUM = re.compile(r"[^a-z0-9]+")


class UnknownEndpointError(ValueError):
    """Raised when an endpoint name is not in the catalog."""


class UnknownParameterError(ValueError):
    """Raised when a query parameter is not valid for an endpoint."""


# ---- Catalog loading ---------------------------------------------------------


@lru_cache(maxsize=1)
def _load_catalog() -> Dict[str, Any]:
    if _resource_files is not None:
        data = (
            _resource_files("tcepepy")
            .joinpath("_data/tcepe_dados_abertos_catalogo.json")
            .read_text(encoding="utf-8")
        )
    else:  # pragma: no cover - legacy fallback
        import os

        here = os.path.dirname(__file__)
        with open(
            os.path.join(here, "_data", "tcepe_dados_abertos_catalogo.json"),
            encoding="utf-8",
        ) as fh:
            data = fh.read()
    return json.loads(data)


def _methods() -> List[Dict[str, Any]]:
    return _load_catalog().get("metodos", []) or []


def _norm_key(value: Optional[str]) -> str:
    return _NON_ALNUM.sub("", (value or "").lower())


def _find_method(name: str) -> Optional[Dict[str, Any]]:
    key = _norm_key(name)
    for method in _methods():
        if _norm_key(method.get("entidade")) == key:
            return method
    return None


def _api_name(param: Dict[str, Any]) -> Optional[str]:
    return param.get("api_name") or param.get("nome") or param.get("parametro")


def _build_param_lookup(method: Dict[str, Any]) -> Dict[str, str]:
    """Map a normalised user key -> the exact API parameter name."""
    lookup: Dict[str, str] = {}
    for param in method.get("entrada", []) or []:
        api = _api_name(param)
        if not api:
            continue
        # snake_case, CamelCase and raw all normalise to the same key, so a
        # single normalised entry accepts every spelling the user might pass.
        for candidate in (api, clean_name(api)):
            lookup[_norm_key(candidate)] = api
    return lookup


# ---- Parameter mapping & validation (used by request.py) ---------------------


def map_params(name: str, params: Dict[str, Any]) -> Dict[str, Any]:
    """Rewrite user parameter names to their official API spelling."""
    if not params:
        return params
    method = _find_method(name)
    if method is None:
        return params
    lookup = _build_param_lookup(method)
    if not lookup:
        return params
    return {lookup.get(_norm_key(k), k): v for k, v in params.items()}


def assert_allowed_params(name: str, params: Dict[str, Any]) -> None:
    """Raise :class:`UnknownParameterError` for parameters not in the catalog."""
    if not params:
        return
    method = _find_method(name)
    if method is None:
        return
    lookup = _build_param_lookup(method)
    if not lookup:
        return
    unknown = [k for k in params if _norm_key(k) not in lookup]
    if not unknown:
        return
    allowed = params_df(method)
    lines = "\n".join(
        f"  - {row.r_name} ({row.api_name})"
        for row in allowed.itertuples(index=False)
    )
    raise UnknownParameterError(
        f"Unknown query parameter(s) for endpoint {name!r}: "
        f"{', '.join(unknown)}.\nAllowed parameters:\n{lines}"
    )


# ---- Public discovery API ----------------------------------------------------


def catalog(search: Optional[str] = None) -> pd.DataFrame:
    """List the available API endpoints.

    Parameters
    ----------
    search:
        Optional case-insensitive substring to filter by endpoint name or
        description (e.g. ``"licit"`` for procurement endpoints).

    Returns
    -------
    pandas.DataFrame
        Columns ``endpoint``, ``group``, ``title`` and ``url``.
    """
    df = pd.DataFrame(
        [
            {
                "endpoint": m.get("entidade"),
                "group": m.get("grupo"),
                "title": m.get("descricao"),
                "url": m.get("url"),
            }
            for m in _methods()
        ]
    )
    if search:
        s = search.lower()
        mask = df["endpoint"].str.lower().str.contains(s, na=False) | df[
            "title"
        ].str.lower().str.contains(s, na=False)
        df = df[mask].reset_index(drop=True)
    return df


def endpoint(name: str) -> Dict[str, Any]:
    """Return the full catalog metadata dict for a single endpoint."""
    method = _find_method(name)
    if method is None:
        raise UnknownEndpointError(
            f"Unknown endpoint {name!r}. Use tcepepy.catalog() to list endpoints."
        )
    return method


def params_df(method: Dict[str, Any]) -> pd.DataFrame:
    rows = []
    for p in method.get("entrada", []) or []:
        api = _api_name(p)
        if not api:
            continue
        rows.append(
            {
                "api_name": api,
                "r_name": clean_name(api),
                "required": (p.get("obrigatorio") or p.get("required")) == "S"
                or p.get("obrigatorio") is True,
                "type": p.get("tipo_api") or p.get("type") or "string",
                "description": p.get("descricao") or p.get("description"),
            }
        )
    return pd.DataFrame(
        rows, columns=["api_name", "r_name", "required", "type", "description"]
    )


def params(name: str) -> pd.DataFrame:
    """List the input parameters accepted by an endpoint.

    Returns a DataFrame with ``api_name`` (exact API spelling), ``r_name``
    (snake_case alias you may also pass), ``required``, ``type`` and
    ``description``.
    """
    return params_df(endpoint(name))


def fields(name: str) -> pd.DataFrame:
    """List the output columns returned by an endpoint.

    Returns a DataFrame with ``name`` (raw API name), ``r_name`` (the
    snake_case column name you get back when ``clean_names=True``), ``type``
    and ``description``.
    """
    method = endpoint(name)
    rows = []
    for f in method.get("saida", []) or []:
        raw = f.get("nome") or f.get("name") or f.get("campo")
        if not raw:
            continue
        rows.append(
            {
                "name": raw,
                "r_name": clean_name(raw),
                "type": f.get("tipo_api") or f.get("type") or "string",
                "description": f.get("descricao") or f.get("description"),
            }
        )
    return pd.DataFrame(rows, columns=["name", "r_name", "type", "description"])
