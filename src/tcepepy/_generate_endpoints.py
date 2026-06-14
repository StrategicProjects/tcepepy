"""Code generator for ``endpoints.py``.

Reads the bundled catalog and emits one wrapper function per endpoint. Run it
whenever the catalog changes::

    python -m tcepepy._generate_endpoints

The generated file is committed to the repository so that editors get real
function signatures, type hints and docstrings (no runtime metaprogramming).
"""

from __future__ import annotations

import os

from .catalog import _find_method

# Public Python name -> official API endpoint. Mirrors the R package's
# hand-written wrappers (one per exported tce_* function).
NAME_TO_ENDPOINT = {
    # revenues
    "state_revenues": "ReceitasEstaduais",
    "municipal_revenues": "ReceitasMunicipais",
    "budgeted_revenues": "ReceitasPrevistas",
    # expenditures
    "state_expenditures": "DespesasEstaduais",
    "municipal_expenditures": "DespesasMunicipais",
    "municipal_transfers": "TransferenciasConcedidasMunicipais",
    "municipal_creditor_types": "TipoCredorMunicipal",
    "state_creditor_types": "TipoCredorEstadual",
    "commitment_summary": "EmpenhoResumo",
    "commitment_liquidations": "EmpenhoLiquidacao",
    "commitment_payments": "EmpenhoPagamento",
    "state_commitment_items": "ItemEmpenhoEstadual",
    "state_price_comparison": "ComparativoPrecoEstado",
    # procurement
    "contracts": "Contratos",
    "contract_documents": "ContratoDocumentos",
    "contract_items": "ContratoItemObjeto",
    "contract_amendments": "TermoAditivo",
    "agreements": "Convenios",
    "bids": "LicitacaoUG",
    "bid_details": "LicitacoesDetalhes",
    "bid_documents": "LicitacoesDocumentos",
    "bid_stages": "EstagioLicitacao",
    "bid_modalities": "ModalidadeLicitacao",
    "bid_statuses": "SituacaoLicitacao",
    "object_characteristics": "CaracteristicaObjeto",
    "object_classifications": "ClassificacaoObjeto",
    "bid_legal_basis": "FundamentacaoLegalLicitacao",
    "object_nature": "NaturezaObjeto",
    # processes
    "processes": "Processos",
    "determinations": "Determinacoes",
    "consideranda": "Considerandos",
    "recommendations": "Recomendacoes",
    "outcomes": "Resultados",
    "retirement_outcomes": "ResultadosAPR",
    "special_accountability": "ResultadosTomadaContaEspecial",
    "debts_fines": "DebitosMultas",
    "spending_limits": "DadosLimiteGastos",
    # public works
    "public_works": "Obras",
    "public_works_contractors": "ObrasDadosContratacao",
    "public_works_audits": "DadosObrasAuditoria",
    "school_transport": "TransporteEscolar",
    # reference / personnel
    "servants": "ListaServidores",
    "municipalities": "Municipios",
    "entities": "UnidadesJurisdicionadas",
    "state_entities": "UnidadesJurisdicionadasEstaduais",
    "municipal_entities": "UnidadesJurisdicionadasMunicipais",
    "sub_units": "SubunidadesUnidadesJurisdicionadas",
    "creditor_types": "TipoCredor",
    "payroll_types": "TipoFolha",
    "funding_sources": "TipoFonteRecurso",
    "inactivation_reasons": "TipoMotivoInativacao",
    # remessa / reference tables
    "benefit_types": "TipoBeneficio",
    "reference_sources": "FonteReferencia",
    "reference_dates": "DataReferencia",
    "reference_codes": "CodigoReferencia",
    "update_indices": "IndiceAtualizacao",
    "budget_statuses": "OrcamentoSituacao",
    "legal_instruments": "Remessa_InstrumentoJuridico",
    "legal_instrument_documents": "Remessa_InstrumentoJuridicoDocumento",
    "legal_instrument_items": "Remessa_InstrumentoJuridicoItens",
    "legal_instrument_participants": "Remessa_InstrumentoJuridicoParticipantes",
    "procurement_processes": "Remessa_ProcessoContratacao",
    "procurement_process_documents": "Remessa_ProcessoContratacaoDocumento",
    "procurement_process_budget": "Remessa_ProcessoContratacaoOrcamento",
    "procurement_process_participants": "Remessa_ProcessoContratacaoParticipantes",
    "remessa_works": "Remessa_Obra",
    "remessa_works_execution": "Remessa_ObraExecucao",
    "remessa_works_geometry": "Remessa_ObraGeometria",
    # suppliers
    "suppliers": "Fornecedores",
    "person_creditor_types": "TipoCredorPessoa",
    "sanctions": "Sancoes",
}

_HEADER = '''"""Endpoint wrapper functions — GENERATED, do not edit by hand.

Regenerate with ``python -m tcepepy._generate_endpoints``. One function per
TCE-PE endpoint; all share the same signature and forward to
:func:`tcepepy.request.request`, with in-memory caching.
"""

from __future__ import annotations

from typing import Any, Optional

import pandas as pd

from .cache import cached
from .request import cache_key, request

__all__ = [
{all_block}]
'''

_TEMPLATE = '''

def {name}(
    *,
    cache: bool = True,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """{summary}

    Endpoint ``{endpoint}``{group}. Discover parameters and output fields with
    ``tcepepy.params({endpoint!r})`` and ``tcepepy.fields({endpoint!r})``.
    """
    return cached(
        cache_key({endpoint!r}, params),
        lambda: request(
            {endpoint!r},
            clean_names=clean_names,
            max_tries=max_tries,
            timeout=timeout,
            progress=progress,
            verbose=verbose,
            **params,
        ),
        use_cache=cache,
    )
'''


def render() -> str:
    all_block = "".join(f"    {name!r},\n" for name in NAME_TO_ENDPOINT)
    parts = [_HEADER.format(all_block=all_block)]
    for name, endpoint in NAME_TO_ENDPOINT.items():
        method = _find_method(endpoint) or {}
        descricao = (method.get("descricao") or endpoint).strip()
        grupo = method.get("grupo")
        summary = descricao.replace("\\", "\\\\").replace('"', '\\"')
        group = f" (group: {grupo})" if grupo else ""
        parts.append(
            _TEMPLATE.format(
                name=name,
                endpoint=endpoint,
                summary=summary,
                group=group,
            )
        )
    return "".join(parts)


def main() -> None:
    out_path = os.path.join(os.path.dirname(__file__), "endpoints.py")
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(render())
    print(f"Wrote {len(NAME_TO_ENDPOINT)} wrappers to {out_path}")


if __name__ == "__main__":
    main()
