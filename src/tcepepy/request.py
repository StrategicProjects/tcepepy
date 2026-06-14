"""Core request engine for the TCE-PE Open Data API.

Mirrors ``request.R``. Three TCE-PE quirks are handled here:

* **Struts2 URLs** – the API invokes methods with a literal ``!`` (e.g.
  ``Contratos!json``). The query string is assembled by hand so the ``!`` is
  never percent-encoded (the server ignores parameters otherwise).
* **ISO-8859-1 backend** – query values are transcoded UTF-8 -> Latin-1 before
  percent-encoding, and the response body is decoded as Latin-1, so accented
  Portuguese values round-trip correctly.
* **100,000-row limit** – when a result hits the API cap, a warning is issued.

The host only accepts connections from Brazilian IP addresses; calls from
elsewhere surface as connection/TLS errors (translated into a clear message).
"""

from __future__ import annotations

import json
import time
from typing import Any, Dict, Optional
from urllib.parse import quote

import httpx
import pandas as pd

from . import _console
from .catalog import assert_allowed_params, map_params
from .config import config
from .naming import clean_names as _clean_names

__all__ = ["request", "cache_key", "TceApiError", "TceRequestError"]

BASE_URL = "https://sistemas.tcepe.tc.br/DadosAbertos/"
DEFAULT_LIMIT = 100_000
_USER_AGENT = "tcepepy (https://github.com/StrategicProjects/tcepepy)"


class TceApiError(RuntimeError):
    """The API returned a non-OK / unexpected payload."""


class TceRequestError(RuntimeError):
    """The request could not be completed (network / TLS / timeout / HTTP)."""


# ---- URL construction --------------------------------------------------------


def _build_params(params: Dict[str, Any]) -> Dict[str, Any]:
    """Drop ``None`` values; stringify the rest."""
    return {k: v for k, v in params.items() if v is not None}


def _encode_latin1(value: Any) -> str:
    """Percent-encode a query value using ISO-8859-1 byte semantics."""
    text = str(value)
    if not text:
        return text
    # Latin-1 bytes; characters outside Latin-1 degrade to '?' like the R client.
    raw = text.encode("iso-8859-1", errors="replace")
    return quote(raw, safe="")


def _build_request_url(endpoint: str, params: Dict[str, Any]) -> str:
    url = f"{BASE_URL}{endpoint}!json"
    if not params:
        return url
    query = "&".join(f"{name}={_encode_latin1(val)}" for name, val in params.items())
    return f"{url}?{query}"


def cache_key(endpoint: str, params: Dict[str, Any]) -> str:
    """Build a stable cache key from endpoint + validated, sorted params."""
    params = _build_params(params)
    assert_allowed_params(endpoint, params)
    params = map_params(endpoint, params)
    if not params:
        return endpoint
    ordered = sorted(params.items())
    return endpoint + "?" + "&".join(f"{k}={v}" for k, v in ordered)


# ---- HTTP --------------------------------------------------------------------


def _perform(url: str, max_tries: int, timeout: float) -> httpx.Response:
    """GET ``url`` with retries on transient transport / 429 / 503 errors."""
    last_exc: Optional[Exception] = None
    for attempt in range(1, max_tries + 1):
        try:
            with httpx.Client(
                timeout=timeout,
                headers={"User-Agent": _USER_AGENT},
                follow_redirects=True,
            ) as client:
                resp = client.get(url)
            if resp.status_code in (429, 503) and attempt < max_tries:
                time.sleep(min(2 ** (attempt - 1), 8))
                continue
            return resp
        except httpx.TransportError as exc:
            last_exc = exc
            if attempt < max_tries:
                time.sleep(min(2 ** (attempt - 1), 8))
                continue
    raise _explain_request_error(last_exc, url)  # type: ignore[arg-type]


def _explain_request_error(exc: Exception, url: str) -> TceRequestError:
    msg = str(exc).lower()
    if any(s in msg for s in ("could not resolve", "name or service", "getaddrinfo")):
        detail = (
            "Could not resolve sistemas.tcepe.tc.br. The TCE-PE API only "
            "accepts connections from Brazilian IP addresses; check your "
            "connection, DNS or VPN location."
        )
    elif any(s in msg for s in ("ssl", "tls", "certificate", "handshake")):
        detail = (
            "TLS handshake with sistemas.tcepe.tc.br failed. Outside Brazil "
            "the API is geo-restricted and may drop the connection."
        )
    elif "timeout" in msg or "timed out" in msg:
        detail = (
            "Request timed out. The API can be slow for broad queries; add "
            "more filters or raise the timeout."
        )
    else:
        detail = f"Request to {url} failed: {exc}"
    return TceRequestError(detail)


# ---- Public entry point ------------------------------------------------------


def request(
    endpoint: str,
    *,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """Send a GET request to any TCE-PE endpoint and return a DataFrame.

    Parameters
    ----------
    endpoint:
        API method name, e.g. ``"Contratos"`` or ``"DespesasEstaduais"``.
    clean_names:
        Convert column names to snake_case (default True).
    max_tries:
        Max attempts on transient failures (default 3).
    timeout:
        Per-request timeout in seconds (default 60).
    progress, verbose:
        Override :data:`tcepepy.config` for this call.
    **params:
        Query parameters, using either the API name (``CodigoEfiscoUG``) or
        its snake_case alias (``codigo_efisco_ug``). ``None`` values are
        dropped.

    Returns
    -------
    pandas.DataFrame
        Empty if the query matched no records.
    """
    progress = config.progress if progress is None else progress
    verbose = config.verbose if verbose is None else verbose

    params = _build_params(params)
    assert_allowed_params(endpoint, params)
    params = map_params(endpoint, params)
    url = _build_request_url(endpoint, params)

    if verbose:
        _console.rule("tcepepy request")
        _console.info(f"Endpoint: {endpoint}")
        _console.info(f"URL: {url}")

    if progress:
        _console.info(f"Querying {endpoint} from the TCE-PE API…")

    started = time.time()
    resp = _perform(url, max_tries=max_tries, timeout=timeout)
    elapsed = time.time() - started

    if verbose:
        size = len(resp.content)
        _console.info(
            f"HTTP {resp.status_code} · {resp.headers.get('content-type', '?')} "
            f"· {size} B · {round(elapsed, 2)}s"
        )

    _check_response(resp, endpoint, url)

    try:
        parsed = json.loads(resp.content.decode("iso-8859-1"))
    except (json.JSONDecodeError, UnicodeDecodeError) as exc:
        raise TceApiError(
            f"The API response for {endpoint!r} could not be parsed as JSON "
            f"(URL: {url}). Underlying error: {exc}"
        ) from exc

    return _extract(parsed, endpoint, url, progress, clean_names)


def _check_response(resp: httpx.Response, endpoint: str, url: str) -> None:
    if resp.is_error:
        raise TceRequestError(
            f"HTTP {resp.status_code} {resp.reason_phrase} when calling "
            f"{endpoint!r} (URL: {url})."
        )
    ctype = resp.headers.get("content-type", "")
    if "json" not in ctype.lower() and "javascript" not in ctype.lower():
        excerpt = resp.text[:200].replace("\n", " ")
        raise TceApiError(
            f"The API did not return JSON for {endpoint!r} "
            f"(Content-Type: {ctype!r}, URL: {url}). Excerpt: {excerpt}"
        )


def _extract(
    parsed: Dict[str, Any],
    endpoint: str,
    url: str,
    progress: bool,
    clean_names: bool,
) -> pd.DataFrame:
    resposta = parsed.get("resposta")
    if resposta is None:
        raise TceApiError(
            f"Unexpected response from {endpoint!r}: no 'resposta' field "
            f"(URL: {url})."
        )

    status = resposta.get("status")
    if status != "OK":
        message = resposta.get("mensagem") or resposta.get("message")
        raise TceApiError(
            f"The API returned status {status!r} for {endpoint!r}"
            + (f": {message}" if message else "")
            + f" (URL: {url})."
        )

    tamanho = int(resposta.get("tamanhoResultado") or 0)
    limite = int(resposta.get("limiteResultado") or DEFAULT_LIMIT)

    if tamanho == 0:
        if progress:
            _console.warn(f"No records found for {endpoint}. Try relaxing filters.")
        return pd.DataFrame()

    if progress:
        _console.success(f"{tamanho} record(s) returned for {endpoint}.")

    if tamanho >= limite:
        _console.warn(
            f"Result reached the API limit of {limite} records for {endpoint}; "
            "some rows are likely missing. Add filters to narrow the query."
        )

    conteudo = resposta.get("conteudo")
    if not conteudo:
        return pd.DataFrame()

    df = pd.DataFrame(conteudo)
    if clean_names:
        df.columns = _clean_names(df.columns)
    return df
