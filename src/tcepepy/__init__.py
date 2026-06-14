"""tcepepy — Python client for the Open Data API of the Tribunal de Contas do
Estado de Pernambuco (TCE-PE), Brazil.

Tidy, ready-to-use functions to query public data on revenues, expenditures,
commitments, procurement, contracts, agreements, public works, legal
processes, personnel and reference tables for every state and municipal
government entity in Pernambuco. Results are returned as ``pandas`` DataFrames
with snake_case columns.

Quick start
-----------
>>> import tcepepy
>>> tcepepy.catalog()                       # discover endpoints (offline)
>>> tcepepy.params("Contratos")             # inspect parameters (offline)
>>> tcepepy.contracts(codigo_efisco_ug="510101")   # query (needs a BR IP)

The live API host (``sistemas.tcepe.tc.br``) only accepts connections from
Brazilian IP addresses. The discovery helpers (:func:`catalog`,
:func:`endpoint`, :func:`params`, :func:`fields`) read a bundled catalog and
work offline anywhere.
"""

from __future__ import annotations

from . import endpoints as _endpoints
from .cache import cache_clear, cache_info
from .catalog import (
    UnknownEndpointError,
    UnknownParameterError,
    catalog,
    endpoint,
    fields,
    params,
)
from .config import config
from .request import (
    TceApiError,
    TceRequestError,
    request,
)

__version__ = "0.1.0"

# Re-export every generated endpoint wrapper at the top level.
for _name in _endpoints.__all__:
    globals()[_name] = getattr(_endpoints, _name)

__all__ = [
    "catalog",
    "endpoint",
    "params",
    "fields",
    "request",
    "cache_info",
    "cache_clear",
    "config",
    "TceApiError",
    "TceRequestError",
    "UnknownEndpointError",
    "UnknownParameterError",
    *_endpoints.__all__,
]
