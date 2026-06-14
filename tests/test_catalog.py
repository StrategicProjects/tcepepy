import pytest

import tcepepy as tce
from tcepepy.catalog import (
    UnknownEndpointError,
    UnknownParameterError,
    assert_allowed_params,
    map_params,
)


def test_catalog_has_71_endpoints():
    df = tce.catalog()
    assert len(df) == 71
    assert list(df.columns) == ["endpoint", "group", "title", "url"]


def test_catalog_search_filters():
    df = tce.catalog(search="contrat")
    assert len(df) > 0
    assert df["endpoint"].str.contains("Contrato").any()


def test_params_columns_and_aliases():
    p = tce.params("Contratos")
    assert list(p.columns) == ["api_name", "r_name", "required", "type", "description"]
    assert "codigo_efisco_ug" in set(p["r_name"])
    assert "CodigoEfiscoUG" in set(p["api_name"])


def test_fields_columns():
    f = tce.fields("Contratos")
    assert list(f.columns) == ["name", "r_name", "type", "description"]
    assert len(f) > 0


def test_endpoint_lookup_is_case_insensitive():
    assert tce.endpoint("contratos")["entidade"] == "Contratos"


def test_unknown_endpoint_raises():
    with pytest.raises(UnknownEndpointError):
        tce.endpoint("DoesNotExist")


def test_map_params_snake_to_api():
    assert map_params("Contratos", {"codigo_efisco_ug": "510101"}) == {
        "CodigoEfiscoUG": "510101"
    }


def test_map_params_passes_api_names_through():
    assert map_params("Contratos", {"CodigoEfiscoUG": "510101"}) == {
        "CodigoEfiscoUG": "510101"
    }


def test_assert_allowed_rejects_unknown():
    with pytest.raises(UnknownParameterError) as exc:
        assert_allowed_params("Contratos", {"xyz": "foo"})
    assert "xyz" in str(exc.value)
    assert "Allowed parameters" in str(exc.value)


def test_assert_allowed_accepts_valid():
    # should not raise
    assert_allowed_params("Contratos", {"ano_contrato": "2025"})
