import json

import httpx
import pytest
import respx

import tcepepy as tce
from tcepepy.cache import cache_clear
from tcepepy.request import (
    TceApiError,
    TceRequestError,
    _build_request_url,
    _encode_latin1,
    cache_key,
    request,
)

API = "https://sistemas.tcepe.tc.br/DadosAbertos/"


def setup_function(_):
    cache_clear()


def _ok(conteudo, tamanho=None, limite=100000):
    payload = {
        "resposta": {
            "status": "OK",
            "tamanhoResultado": len(conteudo) if tamanho is None else tamanho,
            "limiteResultado": limite,
            "conteudo": conteudo,
        }
    }
    body = json.dumps(payload, ensure_ascii=False).encode("iso-8859-1")
    return httpx.Response(
        200, content=body, headers={"content-type": "application/json;charset=ISO-8859-1"}
    )


# ---- URL construction (no network) -------------------------------------------


def test_url_preserves_literal_bang_json():
    url = _build_request_url("Contratos", {"CodigoEfiscoUG": "510101"})
    assert url == f"{API}Contratos!json?CodigoEfiscoUG=510101"


def test_latin1_query_encoding():
    # ã -> %E3, é -> %E9, space -> %20
    assert _encode_latin1("São José") == "S%E3o%20Jos%E9"


def test_cache_key_is_sorted_and_mapped():
    key = cache_key("Contratos", {"ano_contrato": "2025", "codigo_efisco_ug": "510101"})
    assert key == "Contratos?AnoContrato=2025&CodigoEfiscoUG=510101"


# ---- request() against a mocked API ------------------------------------------


@respx.mock
def test_successful_query_returns_dataframe_with_clean_names():
    respx.get(url__regex=rf"{API}Contratos!json.*").mock(
        return_value=_ok([{"CodigoEfiscoUG": "510101", "AnoContrato": "2025"}])
    )
    df = request("Contratos", codigo_efisco_ug="510101", progress=False)
    assert list(df.columns) == ["codigo_efisco_ug", "ano_contrato"]
    assert df.iloc[0]["codigo_efisco_ug"] == "510101"


@respx.mock
def test_latin1_response_roundtrip():
    respx.get(url__regex=rf"{API}Municipios!json.*").mock(
        return_value=_ok([{"MUNICIPIO": "São José da Coroa Grande"}])
    )
    df = request("Municipios", progress=False)
    assert df.iloc[0]["municipio"] == "São José da Coroa Grande"


@respx.mock
def test_empty_result_returns_empty_dataframe():
    respx.get(url__regex=rf"{API}Contratos!json.*").mock(
        return_value=_ok([], tamanho=0)
    )
    df = request("Contratos", codigo_efisco_ug="000", progress=False)
    assert df.empty


@respx.mock
def test_status_not_ok_raises():
    body = json.dumps(
        {"resposta": {"status": "ERRO", "mensagem": "parametro invalido"}}
    ).encode("iso-8859-1")
    respx.get(url__regex=rf"{API}Contratos!json.*").mock(
        return_value=httpx.Response(
            200, content=body, headers={"content-type": "application/json"}
        )
    )
    with pytest.raises(TceApiError) as exc:
        request("Contratos", progress=False)
    assert "ERRO" in str(exc.value)


@respx.mock
def test_non_json_content_raises():
    respx.get(url__regex=rf"{API}Contratos!json.*").mock(
        return_value=httpx.Response(
            200, text="<html>oops</html>", headers={"content-type": "text/html"}
        )
    )
    with pytest.raises(TceApiError):
        request("Contratos", progress=False)


@respx.mock
def test_http_error_raises_request_error():
    respx.get(url__regex=rf"{API}Contratos!json.*").mock(
        return_value=httpx.Response(500, json={}, headers={"content-type": "application/json"})
    )
    with pytest.raises(TceRequestError):
        request("Contratos", progress=False)


@respx.mock
def test_limit_reached_warns():
    respx.get(url__regex=rf"{API}Contratos!json.*").mock(
        return_value=_ok([{"X": "1"}], tamanho=100000, limite=100000)
    )
    with pytest.warns(UserWarning, match="limit"):
        request("Contratos", progress=False)


@respx.mock
def test_transport_error_is_translated():
    respx.get(url__regex=rf"{API}Contratos!json.*").mock(
        side_effect=httpx.ConnectError("Could not resolve host")
    )
    with pytest.raises(TceRequestError, match="resolve"):
        request("Contratos", progress=False, max_tries=1)


@respx.mock
def test_wrapper_caches_and_hits_api_once():
    route = respx.get(url__regex=rf"{API}Contratos!json.*").mock(
        return_value=_ok([{"CodigoEfiscoUG": "510101"}])
    )
    tce.contracts(codigo_efisco_ug="510101", progress=False)
    tce.contracts(codigo_efisco_ug="510101", progress=False)  # cache hit
    assert route.call_count == 1
