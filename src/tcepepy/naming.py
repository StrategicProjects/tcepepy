"""snake_case name cleaning, mirroring R's ``janitor::clean_names()``.

The TCE-PE API returns column names in a mix of ``ALLCAPS``,
``CamelCase`` and ``SNAKE_WITH_UNDERSCORES``. ``clean_name`` normalises a
single name to ``snake_case``; ``clean_names`` applies it to an iterable and
disambiguates duplicates with a numeric suffix (``name``, ``name_2``, ...).
"""

from __future__ import annotations

import re
import unicodedata
from typing import Iterable, List

__all__ = ["clean_name", "clean_names"]

# camelCase / PascalCase boundary insertion, run in order.
_ACRONYM_RE = re.compile(r"([A-Z]+)([A-Z][a-z])")  # "UGCodigo" -> "UG_Codigo"
_CAMEL_RE = re.compile(r"([a-z\d])([A-Z])")  # "aB" -> "a_B"
_NON_ALNUM_RE = re.compile(r"[^A-Za-z0-9]+")
_MULTI_US_RE = re.compile(r"_+")


def _transliterate(text: str) -> str:
    """Strip accents (``Município`` -> ``Municipio``) via ASCII folding."""
    decomposed = unicodedata.normalize("NFKD", text)
    return "".join(ch for ch in decomposed if not unicodedata.combining(ch))


def clean_name(name: str) -> str:
    """Convert a single string to ``snake_case``.

    Examples
    --------
    >>> clean_name("CodigoEfiscoUG")
    'codigo_efisco_ug'
    >>> clean_name("ID_UNIDADE_GESTORA")
    'id_unidade_gestora'
    >>> clean_name("Município")
    'municipio'
    """
    s = _transliterate(str(name))
    s = _ACRONYM_RE.sub(r"\1_\2", s)
    s = _CAMEL_RE.sub(r"\1_\2", s)
    s = _NON_ALNUM_RE.sub("_", s)
    s = _MULTI_US_RE.sub("_", s)
    s = s.strip("_").lower()
    if not s:
        s = "x"
    elif s[0].isdigit():
        s = "x" + s
    return s


def clean_names(names: Iterable[str]) -> List[str]:
    """Clean an iterable of names, disambiguating duplicates."""
    cleaned: List[str] = []
    seen: dict[str, int] = {}
    for raw in names:
        base = clean_name(raw)
        count = seen.get(base, 0) + 1
        seen[base] = count
        cleaned.append(base if count == 1 else f"{base}_{count}")
    return cleaned
