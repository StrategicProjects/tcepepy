"""Runtime configuration, mirroring the R package's ``options(tceper.*)``.

Settings can be changed at runtime via the module-level ``config`` object or
seeded from environment variables:

================  ======================  ========  ===================================
Attribute         Environment variable    Default   Meaning
================  ======================  ========  ===================================
``verbose``       ``TCEPEPY_VERBOSE``     False     Print the final API URL on each call
``progress``      ``TCEPEPY_PROGRESS``    True      Show progress / status messages
``cache_ttl``     ``TCEPEPY_CACHE_TTL``   3600      In-memory cache time-to-live (seconds)
================  ======================  ========  ===================================

Usage::

    import tcepepy
    tcepepy.config.verbose = True
    tcepepy.config.cache_ttl = 7200
"""

from __future__ import annotations

import os
from dataclasses import dataclass

__all__ = ["config", "Config"]


def _env_bool(name: str, default: bool) -> bool:
    raw = os.environ.get(name)
    if raw is None:
        return default
    return raw.strip().lower() in {"1", "true", "yes", "on"}


def _env_int(name: str, default: int) -> int:
    raw = os.environ.get(name)
    if raw is None:
        return default
    try:
        return int(raw)
    except ValueError:
        return default


@dataclass
class Config:
    """Mutable global configuration for tcepepy.

    Access the singleton via ``tcepepy.config`` and set attributes directly,
    e.g. ``tcepepy.config.verbose = True``.
    """

    verbose: bool = False
    """Print the final API URL (and request/response details) on each call."""

    progress: bool = True
    """Show progress / status messages."""

    cache_ttl: int = 3600
    """In-memory cache time-to-live, in seconds."""


config = Config(
    verbose=_env_bool("TCEPEPY_VERBOSE", False),
    progress=_env_bool("TCEPEPY_PROGRESS", True),
    cache_ttl=_env_int("TCEPEPY_CACHE_TTL", 3600),
)
