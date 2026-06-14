import pandas as pd

from tcepepy import cache as cache_mod
from tcepepy.cache import cache_clear, cache_info, cached


def setup_function(_):
    cache_clear()


def test_producer_called_once_when_cached():
    calls = {"n": 0}

    def producer():
        calls["n"] += 1
        return pd.DataFrame({"a": [1, 2]})

    cached("k1", producer)
    cached("k1", producer)
    assert calls["n"] == 1


def test_use_cache_false_always_runs():
    calls = {"n": 0}

    def producer():
        calls["n"] += 1
        return pd.DataFrame()

    cached("k2", producer, use_cache=False)
    cached("k2", producer, use_cache=False)
    assert calls["n"] == 2


def test_different_keys_are_independent():
    cached("a", lambda: pd.DataFrame({"x": [1]}))
    cached("b", lambda: pd.DataFrame({"x": [1, 2]}))
    info = cache_info()
    assert set(info["key"]) == {"a", "b"}


def test_ttl_expiry(monkeypatch):
    from tcepepy.config import config

    calls = {"n": 0}

    def producer():
        calls["n"] += 1
        return pd.DataFrame()

    t = {"now": 1000.0}
    monkeypatch.setattr(cache_mod.time, "time", lambda: t["now"])
    monkeypatch.setattr(config, "cache_ttl", 100)

    cached("k", producer)
    t["now"] = 1050.0  # within TTL
    cached("k", producer)
    assert calls["n"] == 1
    t["now"] = 1200.0  # past TTL
    cached("k", producer)
    assert calls["n"] == 2


def test_cache_clear_with_pattern():
    cached("Contratos?a=1", lambda: pd.DataFrame())
    cached("Obras?a=1", lambda: pd.DataFrame())
    removed = cache_clear("Contratos")
    assert removed == 1
    assert set(cache_info()["key"]) == {"Obras?a=1"}
