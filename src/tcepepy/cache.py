"""In-memory result cache keyed by endpoint + parameters, with a TTL.

Mirrors ``cache.R``. The TTL is read from :data:`tcepepy.config.cache_ttl`
(default 3600s). Results are cached per process; there is no disk persistence.
"""

from __future__ import annotations

import time
from typing import Callable, Dict, Tuple

import pandas as pd

from . import _console
from .config import config

__all__ = ["cached", "cache_clear", "cache_info"]

# key -> (value, unix_timestamp)
_CACHE: Dict[str, Tuple[pd.DataFrame, float]] = {}


def cached(key: str, producer: Callable[[], pd.DataFrame], use_cache: bool = True) -> pd.DataFrame:
    """Return a cached result for ``key`` or compute and store it.

    ``producer`` is a zero-argument callable that performs the actual API
    request; it is only invoked on a cache miss (or when ``use_cache`` is
    False).
    """
    if not use_cache:
        return producer()

    ttl = config.cache_ttl
    entry = _CACHE.get(key)
    if entry is not None:
        value, stamped = entry
        age = time.time() - stamped
        if age < ttl:
            if config.progress:
                _console.success(
                    f"Cache hit ({round(age)}s old, {len(value)} row(s))."
                )
            return value

    result = producer()
    _CACHE[key] = (result, time.time())
    return result


def cache_clear(pattern: str | None = None) -> int:
    """Clear cached entries.

    Parameters
    ----------
    pattern:
        Optional substring; only keys containing it are removed. If omitted,
        the entire cache is cleared.

    Returns
    -------
    int
        Number of entries removed.
    """
    if pattern is None:
        keys = list(_CACHE)
    else:
        keys = [k for k in _CACHE if pattern in k]
    for k in keys:
        del _CACHE[k]
    if keys:
        _console.success(f"Cleared {len(keys)} cached entr{'y' if len(keys) == 1 else 'ies'}.")
    else:
        _console.info("No cached entries to clear.")
    return len(keys)


def cache_info() -> pd.DataFrame:
    """Return a DataFrame describing currently cached entries."""
    now = time.time()
    rows = [
        {
            "key": key,
            "rows": len(value),
            "cached_at": pd.to_datetime(stamped, unit="s"),
            "age_secs": round(now - stamped),
        }
        for key, (value, stamped) in _CACHE.items()
    ]
    return pd.DataFrame(rows, columns=["key", "rows", "cached_at", "age_secs"])
