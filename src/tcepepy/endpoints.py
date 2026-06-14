"""Endpoint wrapper functions — GENERATED, do not edit by hand.

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
    'state_revenues',
    'municipal_revenues',
    'budgeted_revenues',
    'state_expenditures',
    'municipal_expenditures',
    'municipal_transfers',
    'municipal_creditor_types',
    'state_creditor_types',
    'commitment_summary',
    'commitment_liquidations',
    'commitment_payments',
    'state_commitment_items',
    'state_price_comparison',
    'contracts',
    'contract_documents',
    'contract_items',
    'contract_amendments',
    'agreements',
    'bids',
    'bid_details',
    'bid_documents',
    'bid_stages',
    'bid_modalities',
    'bid_statuses',
    'object_characteristics',
    'object_classifications',
    'bid_legal_basis',
    'object_nature',
    'processes',
    'determinations',
    'consideranda',
    'recommendations',
    'outcomes',
    'retirement_outcomes',
    'special_accountability',
    'debts_fines',
    'spending_limits',
    'public_works',
    'public_works_contractors',
    'public_works_audits',
    'school_transport',
    'servants',
    'municipalities',
    'entities',
    'state_entities',
    'municipal_entities',
    'sub_units',
    'creditor_types',
    'payroll_types',
    'funding_sources',
    'inactivation_reasons',
    'benefit_types',
    'reference_sources',
    'reference_dates',
    'reference_codes',
    'update_indices',
    'budget_statuses',
    'legal_instruments',
    'legal_instrument_documents',
    'legal_instrument_items',
    'legal_instrument_participants',
    'procurement_processes',
    'procurement_process_documents',
    'procurement_process_budget',
    'procurement_process_participants',
    'remessa_works',
    'remessa_works_execution',
    'remessa_works_geometry',
    'suppliers',
    'person_creditor_types',
    'sanctions',
]


def state_revenues(
    *,
    cache: bool = True,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """Relação das Receitas Estaduais

    Endpoint ``ReceitasEstaduais`` (group: Receitas). Discover parameters and output fields with
    ``tcepepy.params('ReceitasEstaduais')`` and ``tcepepy.fields('ReceitasEstaduais')``.
    """
    return cached(
        cache_key('ReceitasEstaduais', params),
        lambda: request(
            'ReceitasEstaduais',
            clean_names=clean_names,
            max_tries=max_tries,
            timeout=timeout,
            progress=progress,
            verbose=verbose,
            **params,
        ),
        use_cache=cache,
    )


def municipal_revenues(
    *,
    cache: bool = True,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """Relação das Receitas Municipais

    Endpoint ``ReceitasMunicipais`` (group: Receitas). Discover parameters and output fields with
    ``tcepepy.params('ReceitasMunicipais')`` and ``tcepepy.fields('ReceitasMunicipais')``.
    """
    return cached(
        cache_key('ReceitasMunicipais', params),
        lambda: request(
            'ReceitasMunicipais',
            clean_names=clean_names,
            max_tries=max_tries,
            timeout=timeout,
            progress=progress,
            verbose=verbose,
            **params,
        ),
        use_cache=cache,
    )


def budgeted_revenues(
    *,
    cache: bool = True,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """Relação das Receitas Previstas (apenas Municipais)

    Endpoint ``ReceitasPrevistas`` (group: Receitas). Discover parameters and output fields with
    ``tcepepy.params('ReceitasPrevistas')`` and ``tcepepy.fields('ReceitasPrevistas')``.
    """
    return cached(
        cache_key('ReceitasPrevistas', params),
        lambda: request(
            'ReceitasPrevistas',
            clean_names=clean_names,
            max_tries=max_tries,
            timeout=timeout,
            progress=progress,
            verbose=verbose,
            **params,
        ),
        use_cache=cache,
    )


def state_expenditures(
    *,
    cache: bool = True,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """Relação das Despesas Estaduais

    Endpoint ``DespesasEstaduais`` (group: Despesas). Discover parameters and output fields with
    ``tcepepy.params('DespesasEstaduais')`` and ``tcepepy.fields('DespesasEstaduais')``.
    """
    return cached(
        cache_key('DespesasEstaduais', params),
        lambda: request(
            'DespesasEstaduais',
            clean_names=clean_names,
            max_tries=max_tries,
            timeout=timeout,
            progress=progress,
            verbose=verbose,
            **params,
        ),
        use_cache=cache,
    )


def municipal_expenditures(
    *,
    cache: bool = True,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """Relação das Despesas Municipais - Chave composta (ID_EMPENHO, ANOREFERENCIA, NUMERO_EMPENHO e ID_UNIDADE_GESTORA)

    Endpoint ``DespesasMunicipais`` (group: Despesas). Discover parameters and output fields with
    ``tcepepy.params('DespesasMunicipais')`` and ``tcepepy.fields('DespesasMunicipais')``.
    """
    return cached(
        cache_key('DespesasMunicipais', params),
        lambda: request(
            'DespesasMunicipais',
            clean_names=clean_names,
            max_tries=max_tries,
            timeout=timeout,
            progress=progress,
            verbose=verbose,
            **params,
        ),
        use_cache=cache,
    )


def municipal_transfers(
    *,
    cache: bool = True,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """Relação das transferências concedidas entre unidades juirisdicionadas do mesmo município

    Endpoint ``TransferenciasConcedidasMunicipais`` (group: Despesas). Discover parameters and output fields with
    ``tcepepy.params('TransferenciasConcedidasMunicipais')`` and ``tcepepy.fields('TransferenciasConcedidasMunicipais')``.
    """
    return cached(
        cache_key('TransferenciasConcedidasMunicipais', params),
        lambda: request(
            'TransferenciasConcedidasMunicipais',
            clean_names=clean_names,
            max_tries=max_tries,
            timeout=timeout,
            progress=progress,
            verbose=verbose,
            **params,
        ),
        use_cache=cache,
    )


def municipal_creditor_types(
    *,
    cache: bool = True,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """Lista dos tipos de credores Municipal

    Endpoint ``TipoCredorMunicipal`` (group: Despesas). Discover parameters and output fields with
    ``tcepepy.params('TipoCredorMunicipal')`` and ``tcepepy.fields('TipoCredorMunicipal')``.
    """
    return cached(
        cache_key('TipoCredorMunicipal', params),
        lambda: request(
            'TipoCredorMunicipal',
            clean_names=clean_names,
            max_tries=max_tries,
            timeout=timeout,
            progress=progress,
            verbose=verbose,
            **params,
        ),
        use_cache=cache,
    )


def state_creditor_types(
    *,
    cache: bool = True,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """Lista dos tipos de credores Estadual

    Endpoint ``TipoCredorEstadual`` (group: Despesas). Discover parameters and output fields with
    ``tcepepy.params('TipoCredorEstadual')`` and ``tcepepy.fields('TipoCredorEstadual')``.
    """
    return cached(
        cache_key('TipoCredorEstadual', params),
        lambda: request(
            'TipoCredorEstadual',
            clean_names=clean_names,
            max_tries=max_tries,
            timeout=timeout,
            progress=progress,
            verbose=verbose,
            **params,
        ),
        use_cache=cache,
    )


def commitment_summary(
    *,
    cache: bool = True,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """Relação dos Valores Originais, Reforços e Estornos dos Empenhos Municipais e Estaduais

    Endpoint ``EmpenhoResumo`` (group: Despesas). Discover parameters and output fields with
    ``tcepepy.params('EmpenhoResumo')`` and ``tcepepy.fields('EmpenhoResumo')``.
    """
    return cached(
        cache_key('EmpenhoResumo', params),
        lambda: request(
            'EmpenhoResumo',
            clean_names=clean_names,
            max_tries=max_tries,
            timeout=timeout,
            progress=progress,
            verbose=verbose,
            **params,
        ),
        use_cache=cache,
    )


def commitment_liquidations(
    *,
    cache: bool = True,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """Relação das Liquidações dos Empenhos Municipais e Estaduais

    Endpoint ``EmpenhoLiquidacao`` (group: Despesas). Discover parameters and output fields with
    ``tcepepy.params('EmpenhoLiquidacao')`` and ``tcepepy.fields('EmpenhoLiquidacao')``.
    """
    return cached(
        cache_key('EmpenhoLiquidacao', params),
        lambda: request(
            'EmpenhoLiquidacao',
            clean_names=clean_names,
            max_tries=max_tries,
            timeout=timeout,
            progress=progress,
            verbose=verbose,
            **params,
        ),
        use_cache=cache,
    )


def commitment_payments(
    *,
    cache: bool = True,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """Relação dos Pagamentos dos Empenhos (apenas Municipais)

    Endpoint ``EmpenhoPagamento`` (group: Despesas). Discover parameters and output fields with
    ``tcepepy.params('EmpenhoPagamento')`` and ``tcepepy.fields('EmpenhoPagamento')``.
    """
    return cached(
        cache_key('EmpenhoPagamento', params),
        lambda: request(
            'EmpenhoPagamento',
            clean_names=clean_names,
            max_tries=max_tries,
            timeout=timeout,
            progress=progress,
            verbose=verbose,
            **params,
        ),
        use_cache=cache,
    )


def state_commitment_items(
    *,
    cache: bool = True,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """Relaçao de cada parte que compõem os empenhos Estaduais

    Endpoint ``ItemEmpenhoEstadual`` (group: Despesas). Discover parameters and output fields with
    ``tcepepy.params('ItemEmpenhoEstadual')`` and ``tcepepy.fields('ItemEmpenhoEstadual')``.
    """
    return cached(
        cache_key('ItemEmpenhoEstadual', params),
        lambda: request(
            'ItemEmpenhoEstadual',
            clean_names=clean_names,
            max_tries=max_tries,
            timeout=timeout,
            progress=progress,
            verbose=verbose,
            **params,
        ),
        use_cache=cache,
    )


def state_price_comparison(
    *,
    cache: bool = True,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """Itens dos empenhos estaduais com valores para comparação de preços

    Endpoint ``ComparativoPrecoEstado`` (group: Despesas). Discover parameters and output fields with
    ``tcepepy.params('ComparativoPrecoEstado')`` and ``tcepepy.fields('ComparativoPrecoEstado')``.
    """
    return cached(
        cache_key('ComparativoPrecoEstado', params),
        lambda: request(
            'ComparativoPrecoEstado',
            clean_names=clean_names,
            max_tries=max_tries,
            timeout=timeout,
            progress=progress,
            verbose=verbose,
            **params,
        ),
        use_cache=cache,
    )


def contracts(
    *,
    cache: bool = True,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """Listas dos Contratos Estaduais e Municipais

    Endpoint ``Contratos`` (group: Licitações, Contratos e Convênios). Discover parameters and output fields with
    ``tcepepy.params('Contratos')`` and ``tcepepy.fields('Contratos')``.
    """
    return cached(
        cache_key('Contratos', params),
        lambda: request(
            'Contratos',
            clean_names=clean_names,
            max_tries=max_tries,
            timeout=timeout,
            progress=progress,
            verbose=verbose,
            **params,
        ),
        use_cache=cache,
    )


def contract_documents(
    *,
    cache: bool = True,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """Lista dos documentos de um contrato

    Endpoint ``ContratoDocumentos`` (group: Licitações, Contratos e Convênios). Discover parameters and output fields with
    ``tcepepy.params('ContratoDocumentos')`` and ``tcepepy.fields('ContratoDocumentos')``.
    """
    return cached(
        cache_key('ContratoDocumentos', params),
        lambda: request(
            'ContratoDocumentos',
            clean_names=clean_names,
            max_tries=max_tries,
            timeout=timeout,
            progress=progress,
            verbose=verbose,
            **params,
        ),
        use_cache=cache,
    )


def contract_items(
    *,
    cache: bool = True,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """Relaçao de cada parte que compõem o contrato

    Endpoint ``ContratoItemObjeto`` (group: Licitações, Contratos e Convênios). Discover parameters and output fields with
    ``tcepepy.params('ContratoItemObjeto')`` and ``tcepepy.fields('ContratoItemObjeto')``.
    """
    return cached(
        cache_key('ContratoItemObjeto', params),
        lambda: request(
            'ContratoItemObjeto',
            clean_names=clean_names,
            max_tries=max_tries,
            timeout=timeout,
            progress=progress,
            verbose=verbose,
            **params,
        ),
        use_cache=cache,
    )


def contract_amendments(
    *,
    cache: bool = True,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """Listas dos termos Aditivos dos contratos Estaduais e Municipais

    Endpoint ``TermoAditivo`` (group: Licitações, Contratos e Convênios). Discover parameters and output fields with
    ``tcepepy.params('TermoAditivo')`` and ``tcepepy.fields('TermoAditivo')``.
    """
    return cached(
        cache_key('TermoAditivo', params),
        lambda: request(
            'TermoAditivo',
            clean_names=clean_names,
            max_tries=max_tries,
            timeout=timeout,
            progress=progress,
            verbose=verbose,
            **params,
        ),
        use_cache=cache,
    )


def agreements(
    *,
    cache: bool = True,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """Listas dos Convênios Estaduais e Municipais

    Endpoint ``Convenios`` (group: Licitações, Contratos e Convênios). Discover parameters and output fields with
    ``tcepepy.params('Convenios')`` and ``tcepepy.fields('Convenios')``.
    """
    return cached(
        cache_key('Convenios', params),
        lambda: request(
            'Convenios',
            clean_names=clean_names,
            max_tries=max_tries,
            timeout=timeout,
            progress=progress,
            verbose=verbose,
            **params,
        ),
        use_cache=cache,
    )


def bids(
    *,
    cache: bool = True,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """Relação das Licitações

    Endpoint ``LicitacaoUG`` (group: Licitações, Contratos e Convênios). Discover parameters and output fields with
    ``tcepepy.params('LicitacaoUG')`` and ``tcepepy.fields('LicitacaoUG')``.
    """
    return cached(
        cache_key('LicitacaoUG', params),
        lambda: request(
            'LicitacaoUG',
            clean_names=clean_names,
            max_tries=max_tries,
            timeout=timeout,
            progress=progress,
            verbose=verbose,
            **params,
        ),
        use_cache=cache,
    )


def bid_details(
    *,
    cache: bool = True,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """Relação das Licitações com os respectivos Licitantes

    Endpoint ``LicitacoesDetalhes`` (group: Licitações, Contratos e Convênios). Discover parameters and output fields with
    ``tcepepy.params('LicitacoesDetalhes')`` and ``tcepepy.fields('LicitacoesDetalhes')``.
    """
    return cached(
        cache_key('LicitacoesDetalhes', params),
        lambda: request(
            'LicitacoesDetalhes',
            clean_names=clean_names,
            max_tries=max_tries,
            timeout=timeout,
            progress=progress,
            verbose=verbose,
            **params,
        ),
        use_cache=cache,
    )


def bid_documents(
    *,
    cache: bool = True,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """Lista dos documentos de uma licitação

    Endpoint ``LicitacoesDocumentos`` (group: Licitações, Contratos e Convênios). Discover parameters and output fields with
    ``tcepepy.params('LicitacoesDocumentos')`` and ``tcepepy.fields('LicitacoesDocumentos')``.
    """
    return cached(
        cache_key('LicitacoesDocumentos', params),
        lambda: request(
            'LicitacoesDocumentos',
            clean_names=clean_names,
            max_tries=max_tries,
            timeout=timeout,
            progress=progress,
            verbose=verbose,
            **params,
        ),
        use_cache=cache,
    )


def bid_stages(
    *,
    cache: bool = True,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """Listas dos estágios de uma licitação

    Endpoint ``EstagioLicitacao`` (group: Licitações, Contratos e Convênios). Discover parameters and output fields with
    ``tcepepy.params('EstagioLicitacao')`` and ``tcepepy.fields('EstagioLicitacao')``.
    """
    return cached(
        cache_key('EstagioLicitacao', params),
        lambda: request(
            'EstagioLicitacao',
            clean_names=clean_names,
            max_tries=max_tries,
            timeout=timeout,
            progress=progress,
            verbose=verbose,
            **params,
        ),
        use_cache=cache,
    )


def bid_modalities(
    *,
    cache: bool = True,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """Listas dos tipos de modalidade de uma licitação

    Endpoint ``ModalidadeLicitacao`` (group: Licitações, Contratos e Convênios). Discover parameters and output fields with
    ``tcepepy.params('ModalidadeLicitacao')`` and ``tcepepy.fields('ModalidadeLicitacao')``.
    """
    return cached(
        cache_key('ModalidadeLicitacao', params),
        lambda: request(
            'ModalidadeLicitacao',
            clean_names=clean_names,
            max_tries=max_tries,
            timeout=timeout,
            progress=progress,
            verbose=verbose,
            **params,
        ),
        use_cache=cache,
    )


def bid_statuses(
    *,
    cache: bool = True,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """Listas dos tipos de situação de uma licitação

    Endpoint ``SituacaoLicitacao`` (group: Licitações, Contratos e Convênios). Discover parameters and output fields with
    ``tcepepy.params('SituacaoLicitacao')`` and ``tcepepy.fields('SituacaoLicitacao')``.
    """
    return cached(
        cache_key('SituacaoLicitacao', params),
        lambda: request(
            'SituacaoLicitacao',
            clean_names=clean_names,
            max_tries=max_tries,
            timeout=timeout,
            progress=progress,
            verbose=verbose,
            **params,
        ),
        use_cache=cache,
    )


def object_characteristics(
    *,
    cache: bool = True,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """Listas dos tipos de característica de um objeto

    Endpoint ``CaracteristicaObjeto`` (group: Licitações, Contratos e Convênios). Discover parameters and output fields with
    ``tcepepy.params('CaracteristicaObjeto')`` and ``tcepepy.fields('CaracteristicaObjeto')``.
    """
    return cached(
        cache_key('CaracteristicaObjeto', params),
        lambda: request(
            'CaracteristicaObjeto',
            clean_names=clean_names,
            max_tries=max_tries,
            timeout=timeout,
            progress=progress,
            verbose=verbose,
            **params,
        ),
        use_cache=cache,
    )


def object_classifications(
    *,
    cache: bool = True,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """Listas dos tipos de classificação de um objeto

    Endpoint ``ClassificacaoObjeto`` (group: Licitações, Contratos e Convênios). Discover parameters and output fields with
    ``tcepepy.params('ClassificacaoObjeto')`` and ``tcepepy.fields('ClassificacaoObjeto')``.
    """
    return cached(
        cache_key('ClassificacaoObjeto', params),
        lambda: request(
            'ClassificacaoObjeto',
            clean_names=clean_names,
            max_tries=max_tries,
            timeout=timeout,
            progress=progress,
            verbose=verbose,
            **params,
        ),
        use_cache=cache,
    )


def bid_legal_basis(
    *,
    cache: bool = True,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """Lista dos fundamentação legal da licitação

    Endpoint ``FundamentacaoLegalLicitacao`` (group: Licitações, Contratos e Convênios). Discover parameters and output fields with
    ``tcepepy.params('FundamentacaoLegalLicitacao')`` and ``tcepepy.fields('FundamentacaoLegalLicitacao')``.
    """
    return cached(
        cache_key('FundamentacaoLegalLicitacao', params),
        lambda: request(
            'FundamentacaoLegalLicitacao',
            clean_names=clean_names,
            max_tries=max_tries,
            timeout=timeout,
            progress=progress,
            verbose=verbose,
            **params,
        ),
        use_cache=cache,
    )


def object_nature(
    *,
    cache: bool = True,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """Listas dos tipos de natureza de um objeto

    Endpoint ``NaturezaObjeto`` (group: Licitações, Contratos e Convênios). Discover parameters and output fields with
    ``tcepepy.params('NaturezaObjeto')`` and ``tcepepy.fields('NaturezaObjeto')``.
    """
    return cached(
        cache_key('NaturezaObjeto', params),
        lambda: request(
            'NaturezaObjeto',
            clean_names=clean_names,
            max_tries=max_tries,
            timeout=timeout,
            progress=progress,
            verbose=verbose,
            **params,
        ),
        use_cache=cache,
    )


def processes(
    *,
    cache: bool = True,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """Listas dos processos físicos e eletrônicos formalizados

    Endpoint ``Processos`` (group: Processos). Discover parameters and output fields with
    ``tcepepy.params('Processos')`` and ``tcepepy.fields('Processos')``.
    """
    return cached(
        cache_key('Processos', params),
        lambda: request(
            'Processos',
            clean_names=clean_names,
            max_tries=max_tries,
            timeout=timeout,
            progress=progress,
            verbose=verbose,
            **params,
        ),
        use_cache=cache,
    )


def determinations(
    *,
    cache: bool = True,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """Lista das determinações dos processos eletrônicos transitados em julgado

    Endpoint ``Determinacoes`` (group: Processos). Discover parameters and output fields with
    ``tcepepy.params('Determinacoes')`` and ``tcepepy.fields('Determinacoes')``.
    """
    return cached(
        cache_key('Determinacoes', params),
        lambda: request(
            'Determinacoes',
            clean_names=clean_names,
            max_tries=max_tries,
            timeout=timeout,
            progress=progress,
            verbose=verbose,
            **params,
        ),
        use_cache=cache,
    )


def consideranda(
    *,
    cache: bool = True,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """Listas dos considerandos dos processos eletrônicos transitados em julgado

    Endpoint ``Considerandos`` (group: Processos). Discover parameters and output fields with
    ``tcepepy.params('Considerandos')`` and ``tcepepy.fields('Considerandos')``.
    """
    return cached(
        cache_key('Considerandos', params),
        lambda: request(
            'Considerandos',
            clean_names=clean_names,
            max_tries=max_tries,
            timeout=timeout,
            progress=progress,
            verbose=verbose,
            **params,
        ),
        use_cache=cache,
    )


def recommendations(
    *,
    cache: bool = True,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """Listas das recomendações dos processos eletrônicos transitados em julgado

    Endpoint ``Recomendacoes`` (group: Processos). Discover parameters and output fields with
    ``tcepepy.params('Recomendacoes')`` and ``tcepepy.fields('Recomendacoes')``.
    """
    return cached(
        cache_key('Recomendacoes', params),
        lambda: request(
            'Recomendacoes',
            clean_names=clean_names,
            max_tries=max_tries,
            timeout=timeout,
            progress=progress,
            verbose=verbose,
            **params,
        ),
        use_cache=cache,
    )


def outcomes(
    *,
    cache: bool = True,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """Lista dos resultados dos processos eletrônicos transitados em julgado

    Endpoint ``Resultados`` (group: Processos). Discover parameters and output fields with
    ``tcepepy.params('Resultados')`` and ``tcepepy.fields('Resultados')``.
    """
    return cached(
        cache_key('Resultados', params),
        lambda: request(
            'Resultados',
            clean_names=clean_names,
            max_tries=max_tries,
            timeout=timeout,
            progress=progress,
            verbose=verbose,
            **params,
        ),
        use_cache=cache,
    )


def retirement_outcomes(
    *,
    cache: bool = True,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """Lista dos resultados dos processos eletrônicos da modalidade Aposentadoria, Pensão e Reforma

    Endpoint ``ResultadosAPR`` (group: Processos). Discover parameters and output fields with
    ``tcepepy.params('ResultadosAPR')`` and ``tcepepy.fields('ResultadosAPR')``.
    """
    return cached(
        cache_key('ResultadosAPR', params),
        lambda: request(
            'ResultadosAPR',
            clean_names=clean_names,
            max_tries=max_tries,
            timeout=timeout,
            progress=progress,
            verbose=verbose,
            **params,
        ),
        use_cache=cache,
    )


def special_accountability(
    *,
    cache: bool = True,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """ResultadosTomadaContaEspecial

    Endpoint ``ResultadosTomadaContaEspecial`` (group: Processos). Discover parameters and output fields with
    ``tcepepy.params('ResultadosTomadaContaEspecial')`` and ``tcepepy.fields('ResultadosTomadaContaEspecial')``.
    """
    return cached(
        cache_key('ResultadosTomadaContaEspecial', params),
        lambda: request(
            'ResultadosTomadaContaEspecial',
            clean_names=clean_names,
            max_tries=max_tries,
            timeout=timeout,
            progress=progress,
            verbose=verbose,
            **params,
        ),
        use_cache=cache,
    )


def debts_fines(
    *,
    cache: bool = True,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """Relação das débitos e multas

    Endpoint ``DebitosMultas`` (group: Processos). Discover parameters and output fields with
    ``tcepepy.params('DebitosMultas')`` and ``tcepepy.fields('DebitosMultas')``.
    """
    return cached(
        cache_key('DebitosMultas', params),
        lambda: request(
            'DebitosMultas',
            clean_names=clean_names,
            max_tries=max_tries,
            timeout=timeout,
            progress=progress,
            verbose=verbose,
            **params,
        ),
        use_cache=cache,
    )


def spending_limits(
    *,
    cache: bool = True,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """Dados de limites de gastos dos processos julgados de contas de governo

    Endpoint ``DadosLimiteGastos`` (group: Processos). Discover parameters and output fields with
    ``tcepepy.params('DadosLimiteGastos')`` and ``tcepepy.fields('DadosLimiteGastos')``.
    """
    return cached(
        cache_key('DadosLimiteGastos', params),
        lambda: request(
            'DadosLimiteGastos',
            clean_names=clean_names,
            max_tries=max_tries,
            timeout=timeout,
            progress=progress,
            verbose=verbose,
            **params,
        ),
        use_cache=cache,
    )


def public_works(
    *,
    cache: bool = True,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """Obras e serviços de engenharia fiscalizados pelo Tribunal de Contas.

    Endpoint ``Obras`` (group: Obras). Discover parameters and output fields with
    ``tcepepy.params('Obras')`` and ``tcepepy.fields('Obras')``.
    """
    return cached(
        cache_key('Obras', params),
        lambda: request(
            'Obras',
            clean_names=clean_names,
            max_tries=max_tries,
            timeout=timeout,
            progress=progress,
            verbose=verbose,
            **params,
        ),
        use_cache=cache,
    )


def public_works_contractors(
    *,
    cache: bool = True,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """Referem-se aos dados das empresas contratadas para a obra.

    Endpoint ``ObrasDadosContratacao`` (group: Obras). Discover parameters and output fields with
    ``tcepepy.params('ObrasDadosContratacao')`` and ``tcepepy.fields('ObrasDadosContratacao')``.
    """
    return cached(
        cache_key('ObrasDadosContratacao', params),
        lambda: request(
            'ObrasDadosContratacao',
            clean_names=clean_names,
            max_tries=max_tries,
            timeout=timeout,
            progress=progress,
            verbose=verbose,
            **params,
        ),
        use_cache=cache,
    )


def public_works_audits(
    *,
    cache: bool = True,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """Referem-se aos dados das obras

    Endpoint ``DadosObrasAuditoria`` (group: Obras). Discover parameters and output fields with
    ``tcepepy.params('DadosObrasAuditoria')`` and ``tcepepy.fields('DadosObrasAuditoria')``.
    """
    return cached(
        cache_key('DadosObrasAuditoria', params),
        lambda: request(
            'DadosObrasAuditoria',
            clean_names=clean_names,
            max_tries=max_tries,
            timeout=timeout,
            progress=progress,
            verbose=verbose,
            **params,
        ),
        use_cache=cache,
    )


def school_transport(
    *,
    cache: bool = True,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """Serviços de transporte escolar fiscalizados pelo Tribunal de Contas.

    Endpoint ``TransporteEscolar`` (group: Transporte Escolar). Discover parameters and output fields with
    ``tcepepy.params('TransporteEscolar')`` and ``tcepepy.fields('TransporteEscolar')``.
    """
    return cached(
        cache_key('TransporteEscolar', params),
        lambda: request(
            'TransporteEscolar',
            clean_names=clean_names,
            max_tries=max_tries,
            timeout=timeout,
            progress=progress,
            verbose=verbose,
            **params,
        ),
        use_cache=cache,
    )


def servants(
    *,
    cache: bool = True,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """Lista dos servidores municipais e estaduais de Pernambuco (base Sagres Pessoal)

    Endpoint ``ListaServidores`` (group: Pessoal). Discover parameters and output fields with
    ``tcepepy.params('ListaServidores')`` and ``tcepepy.fields('ListaServidores')``.
    """
    return cached(
        cache_key('ListaServidores', params),
        lambda: request(
            'ListaServidores',
            clean_names=clean_names,
            max_tries=max_tries,
            timeout=timeout,
            progress=progress,
            verbose=verbose,
            **params,
        ),
        use_cache=cache,
    )


def municipalities(
    *,
    cache: bool = True,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """Relação dos municípios

    Endpoint ``Municipios`` (group: Informações básicas). Discover parameters and output fields with
    ``tcepepy.params('Municipios')`` and ``tcepepy.fields('Municipios')``.
    """
    return cached(
        cache_key('Municipios', params),
        lambda: request(
            'Municipios',
            clean_names=clean_names,
            max_tries=max_tries,
            timeout=timeout,
            progress=progress,
            verbose=verbose,
            **params,
        ),
        use_cache=cache,
    )


def entities(
    *,
    cache: bool = True,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """Relação das Unidades Jurisdicionadas

    Endpoint ``UnidadesJurisdicionadas`` (group: Informações básicas). Discover parameters and output fields with
    ``tcepepy.params('UnidadesJurisdicionadas')`` and ``tcepepy.fields('UnidadesJurisdicionadas')``.
    """
    return cached(
        cache_key('UnidadesJurisdicionadas', params),
        lambda: request(
            'UnidadesJurisdicionadas',
            clean_names=clean_names,
            max_tries=max_tries,
            timeout=timeout,
            progress=progress,
            verbose=verbose,
            **params,
        ),
        use_cache=cache,
    )


def state_entities(
    *,
    cache: bool = True,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """Relação das Unidades Jurisdicionais Estaduais

    Endpoint ``UnidadesJurisdicionadasEstaduais`` (group: Informações básicas). Discover parameters and output fields with
    ``tcepepy.params('UnidadesJurisdicionadasEstaduais')`` and ``tcepepy.fields('UnidadesJurisdicionadasEstaduais')``.
    """
    return cached(
        cache_key('UnidadesJurisdicionadasEstaduais', params),
        lambda: request(
            'UnidadesJurisdicionadasEstaduais',
            clean_names=clean_names,
            max_tries=max_tries,
            timeout=timeout,
            progress=progress,
            verbose=verbose,
            **params,
        ),
        use_cache=cache,
    )


def municipal_entities(
    *,
    cache: bool = True,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """Relação das Unidades Jurisdicionais Municipais

    Endpoint ``UnidadesJurisdicionadasMunicipais`` (group: Informações básicas). Discover parameters and output fields with
    ``tcepepy.params('UnidadesJurisdicionadasMunicipais')`` and ``tcepepy.fields('UnidadesJurisdicionadasMunicipais')``.
    """
    return cached(
        cache_key('UnidadesJurisdicionadasMunicipais', params),
        lambda: request(
            'UnidadesJurisdicionadasMunicipais',
            clean_names=clean_names,
            max_tries=max_tries,
            timeout=timeout,
            progress=progress,
            verbose=verbose,
            **params,
        ),
        use_cache=cache,
    )


def sub_units(
    *,
    cache: bool = True,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """Relação das Subunidades das Unidades Jurisdicionadas

    Endpoint ``SubunidadesUnidadesJurisdicionadas`` (group: Informações básicas). Discover parameters and output fields with
    ``tcepepy.params('SubunidadesUnidadesJurisdicionadas')`` and ``tcepepy.fields('SubunidadesUnidadesJurisdicionadas')``.
    """
    return cached(
        cache_key('SubunidadesUnidadesJurisdicionadas', params),
        lambda: request(
            'SubunidadesUnidadesJurisdicionadas',
            clean_names=clean_names,
            max_tries=max_tries,
            timeout=timeout,
            progress=progress,
            verbose=verbose,
            **params,
        ),
        use_cache=cache,
    )


def creditor_types(
    *,
    cache: bool = True,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """Relação dos tipos de fornecedores

    Endpoint ``TipoCredor`` (group: Informações básicas). Discover parameters and output fields with
    ``tcepepy.params('TipoCredor')`` and ``tcepepy.fields('TipoCredor')``.
    """
    return cached(
        cache_key('TipoCredor', params),
        lambda: request(
            'TipoCredor',
            clean_names=clean_names,
            max_tries=max_tries,
            timeout=timeout,
            progress=progress,
            verbose=verbose,
            **params,
        ),
        use_cache=cache,
    )


def payroll_types(
    *,
    cache: bool = True,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """Relação dos tipos de folha

    Endpoint ``TipoFolha`` (group: Informações básicas). Discover parameters and output fields with
    ``tcepepy.params('TipoFolha')`` and ``tcepepy.fields('TipoFolha')``.
    """
    return cached(
        cache_key('TipoFolha', params),
        lambda: request(
            'TipoFolha',
            clean_names=clean_names,
            max_tries=max_tries,
            timeout=timeout,
            progress=progress,
            verbose=verbose,
            **params,
        ),
        use_cache=cache,
    )


def funding_sources(
    *,
    cache: bool = True,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """Relação das fontes de recursos

    Endpoint ``TipoFonteRecurso`` (group: Informações básicas). Discover parameters and output fields with
    ``tcepepy.params('TipoFonteRecurso')`` and ``tcepepy.fields('TipoFonteRecurso')``.
    """
    return cached(
        cache_key('TipoFonteRecurso', params),
        lambda: request(
            'TipoFonteRecurso',
            clean_names=clean_names,
            max_tries=max_tries,
            timeout=timeout,
            progress=progress,
            verbose=verbose,
            **params,
        ),
        use_cache=cache,
    )


def inactivation_reasons(
    *,
    cache: bool = True,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """Relação dos tipos de motivo de inativação

    Endpoint ``TipoMotivoInativacao`` (group: Informações básicas). Discover parameters and output fields with
    ``tcepepy.params('TipoMotivoInativacao')`` and ``tcepepy.fields('TipoMotivoInativacao')``.
    """
    return cached(
        cache_key('TipoMotivoInativacao', params),
        lambda: request(
            'TipoMotivoInativacao',
            clean_names=clean_names,
            max_tries=max_tries,
            timeout=timeout,
            progress=progress,
            verbose=verbose,
            **params,
        ),
        use_cache=cache,
    )


def benefit_types(
    *,
    cache: bool = True,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """Tipo de benefício do lote/item

    Endpoint ``TipoBeneficio`` (group: RemessaTCEPE). Discover parameters and output fields with
    ``tcepepy.params('TipoBeneficio')`` and ``tcepepy.fields('TipoBeneficio')``.
    """
    return cached(
        cache_key('TipoBeneficio', params),
        lambda: request(
            'TipoBeneficio',
            clean_names=clean_names,
            max_tries=max_tries,
            timeout=timeout,
            progress=progress,
            verbose=verbose,
            **params,
        ),
        use_cache=cache,
    )


def reference_sources(
    *,
    cache: bool = True,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """Possíveis fontes de referência para importação dos itens do orçamento estimativo

    Endpoint ``FonteReferencia`` (group: RemessaTCEPE). Discover parameters and output fields with
    ``tcepepy.params('FonteReferencia')`` and ``tcepepy.fields('FonteReferencia')``.
    """
    return cached(
        cache_key('FonteReferencia', params),
        lambda: request(
            'FonteReferencia',
            clean_names=clean_names,
            max_tries=max_tries,
            timeout=timeout,
            progress=progress,
            verbose=verbose,
            **params,
        ),
        use_cache=cache,
    )


def reference_dates(
    *,
    cache: bool = True,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """Datas disponíveis para as fontes de referência utilizadas na importação dos itens do orçamento estimativo

    Endpoint ``DataReferencia`` (group: RemessaTCEPE). Discover parameters and output fields with
    ``tcepepy.params('DataReferencia')`` and ``tcepepy.fields('DataReferencia')``.
    """
    return cached(
        cache_key('DataReferencia', params),
        lambda: request(
            'DataReferencia',
            clean_names=clean_names,
            max_tries=max_tries,
            timeout=timeout,
            progress=progress,
            verbose=verbose,
            **params,
        ),
        use_cache=cache,
    )


def reference_codes(
    *,
    cache: bool = True,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """Códigos de referência para importação dos itens do orçamento estimativo

    Endpoint ``CodigoReferencia`` (group: RemessaTCEPE). Discover parameters and output fields with
    ``tcepepy.params('CodigoReferencia')`` and ``tcepepy.fields('CodigoReferencia')``.
    """
    return cached(
        cache_key('CodigoReferencia', params),
        lambda: request(
            'CodigoReferencia',
            clean_names=clean_names,
            max_tries=max_tries,
            timeout=timeout,
            progress=progress,
            verbose=verbose,
            **params,
        ),
        use_cache=cache,
    )


def update_indices(
    *,
    cache: bool = True,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """Índices de atualização que devem ser utilizados na planilha de importação do orçamento estimativo

    Endpoint ``IndiceAtualizacao`` (group: RemessaTCEPE). Discover parameters and output fields with
    ``tcepepy.params('IndiceAtualizacao')`` and ``tcepepy.fields('IndiceAtualizacao')``.
    """
    return cached(
        cache_key('IndiceAtualizacao', params),
        lambda: request(
            'IndiceAtualizacao',
            clean_names=clean_names,
            max_tries=max_tries,
            timeout=timeout,
            progress=progress,
            verbose=verbose,
            **params,
        ),
        use_cache=cache,
    )


def budget_statuses(
    *,
    cache: bool = True,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """Possíveis situações dos itens/lotes do orçamento estimativo

    Endpoint ``OrcamentoSituacao`` (group: RemessaTCEPE). Discover parameters and output fields with
    ``tcepepy.params('OrcamentoSituacao')`` and ``tcepepy.fields('OrcamentoSituacao')``.
    """
    return cached(
        cache_key('OrcamentoSituacao', params),
        lambda: request(
            'OrcamentoSituacao',
            clean_names=clean_names,
            max_tries=max_tries,
            timeout=timeout,
            progress=progress,
            verbose=verbose,
            **params,
        ),
        use_cache=cache,
    )


def legal_instruments(
    *,
    cache: bool = True,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """Dados dos instrumentos jurídicos cadastrados no RemessaTCEPE

    Endpoint ``Remessa_InstrumentoJuridico`` (group: RemessaTCEPE). Discover parameters and output fields with
    ``tcepepy.params('Remessa_InstrumentoJuridico')`` and ``tcepepy.fields('Remessa_InstrumentoJuridico')``.
    """
    return cached(
        cache_key('Remessa_InstrumentoJuridico', params),
        lambda: request(
            'Remessa_InstrumentoJuridico',
            clean_names=clean_names,
            max_tries=max_tries,
            timeout=timeout,
            progress=progress,
            verbose=verbose,
            **params,
        ),
        use_cache=cache,
    )


def legal_instrument_documents(
    *,
    cache: bool = True,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """Documentos de um instrumento jurídico

    Endpoint ``Remessa_InstrumentoJuridicoDocumento`` (group: RemessaTCEPE). Discover parameters and output fields with
    ``tcepepy.params('Remessa_InstrumentoJuridicoDocumento')`` and ``tcepepy.fields('Remessa_InstrumentoJuridicoDocumento')``.
    """
    return cached(
        cache_key('Remessa_InstrumentoJuridicoDocumento', params),
        lambda: request(
            'Remessa_InstrumentoJuridicoDocumento',
            clean_names=clean_names,
            max_tries=max_tries,
            timeout=timeout,
            progress=progress,
            verbose=verbose,
            **params,
        ),
        use_cache=cache,
    )


def legal_instrument_items(
    *,
    cache: bool = True,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """Itens de um instrumento jurídico

    Endpoint ``Remessa_InstrumentoJuridicoItens`` (group: RemessaTCEPE). Discover parameters and output fields with
    ``tcepepy.params('Remessa_InstrumentoJuridicoItens')`` and ``tcepepy.fields('Remessa_InstrumentoJuridicoItens')``.
    """
    return cached(
        cache_key('Remessa_InstrumentoJuridicoItens', params),
        lambda: request(
            'Remessa_InstrumentoJuridicoItens',
            clean_names=clean_names,
            max_tries=max_tries,
            timeout=timeout,
            progress=progress,
            verbose=verbose,
            **params,
        ),
        use_cache=cache,
    )


def legal_instrument_participants(
    *,
    cache: bool = True,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """Partes de um instrumento jurídico

    Endpoint ``Remessa_InstrumentoJuridicoParticipantes`` (group: RemessaTCEPE). Discover parameters and output fields with
    ``tcepepy.params('Remessa_InstrumentoJuridicoParticipantes')`` and ``tcepepy.fields('Remessa_InstrumentoJuridicoParticipantes')``.
    """
    return cached(
        cache_key('Remessa_InstrumentoJuridicoParticipantes', params),
        lambda: request(
            'Remessa_InstrumentoJuridicoParticipantes',
            clean_names=clean_names,
            max_tries=max_tries,
            timeout=timeout,
            progress=progress,
            verbose=verbose,
            **params,
        ),
        use_cache=cache,
    )


def procurement_processes(
    *,
    cache: bool = True,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """Dados dos processos de contratação cadastrados no RemessaTCEPE

    Endpoint ``Remessa_ProcessoContratacao`` (group: RemessaTCEPE). Discover parameters and output fields with
    ``tcepepy.params('Remessa_ProcessoContratacao')`` and ``tcepepy.fields('Remessa_ProcessoContratacao')``.
    """
    return cached(
        cache_key('Remessa_ProcessoContratacao', params),
        lambda: request(
            'Remessa_ProcessoContratacao',
            clean_names=clean_names,
            max_tries=max_tries,
            timeout=timeout,
            progress=progress,
            verbose=verbose,
            **params,
        ),
        use_cache=cache,
    )


def procurement_process_documents(
    *,
    cache: bool = True,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """Documentos de um processo de contratação

    Endpoint ``Remessa_ProcessoContratacaoDocumento`` (group: RemessaTCEPE). Discover parameters and output fields with
    ``tcepepy.params('Remessa_ProcessoContratacaoDocumento')`` and ``tcepepy.fields('Remessa_ProcessoContratacaoDocumento')``.
    """
    return cached(
        cache_key('Remessa_ProcessoContratacaoDocumento', params),
        lambda: request(
            'Remessa_ProcessoContratacaoDocumento',
            clean_names=clean_names,
            max_tries=max_tries,
            timeout=timeout,
            progress=progress,
            verbose=verbose,
            **params,
        ),
        use_cache=cache,
    )


def procurement_process_budget(
    *,
    cache: bool = True,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """Lotes e itens do orçamento de um processo de contratação

    Endpoint ``Remessa_ProcessoContratacaoOrcamento`` (group: RemessaTCEPE). Discover parameters and output fields with
    ``tcepepy.params('Remessa_ProcessoContratacaoOrcamento')`` and ``tcepepy.fields('Remessa_ProcessoContratacaoOrcamento')``.
    """
    return cached(
        cache_key('Remessa_ProcessoContratacaoOrcamento', params),
        lambda: request(
            'Remessa_ProcessoContratacaoOrcamento',
            clean_names=clean_names,
            max_tries=max_tries,
            timeout=timeout,
            progress=progress,
            verbose=verbose,
            **params,
        ),
        use_cache=cache,
    )


def procurement_process_participants(
    *,
    cache: bool = True,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """Lista de licitantes/participantes de um processo de contratação

    Endpoint ``Remessa_ProcessoContratacaoParticipantes`` (group: RemessaTCEPE). Discover parameters and output fields with
    ``tcepepy.params('Remessa_ProcessoContratacaoParticipantes')`` and ``tcepepy.fields('Remessa_ProcessoContratacaoParticipantes')``.
    """
    return cached(
        cache_key('Remessa_ProcessoContratacaoParticipantes', params),
        lambda: request(
            'Remessa_ProcessoContratacaoParticipantes',
            clean_names=clean_names,
            max_tries=max_tries,
            timeout=timeout,
            progress=progress,
            verbose=verbose,
            **params,
        ),
        use_cache=cache,
    )


def remessa_works(
    *,
    cache: bool = True,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """Detalhes das obras públicas recebidas pelo sistema RemessaTCEPE

    Endpoint ``Remessa_Obra`` (group: RemessaTCEPE). Discover parameters and output fields with
    ``tcepepy.params('Remessa_Obra')`` and ``tcepepy.fields('Remessa_Obra')``.
    """
    return cached(
        cache_key('Remessa_Obra', params),
        lambda: request(
            'Remessa_Obra',
            clean_names=clean_names,
            max_tries=max_tries,
            timeout=timeout,
            progress=progress,
            verbose=verbose,
            **params,
        ),
        use_cache=cache,
    )


def remessa_works_execution(
    *,
    cache: bool = True,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """Detalhes das execuções das obras públicas recebidas pelo sistema RemessaTCEPE

    Endpoint ``Remessa_ObraExecucao`` (group: RemessaTCEPE). Discover parameters and output fields with
    ``tcepepy.params('Remessa_ObraExecucao')`` and ``tcepepy.fields('Remessa_ObraExecucao')``.
    """
    return cached(
        cache_key('Remessa_ObraExecucao', params),
        lambda: request(
            'Remessa_ObraExecucao',
            clean_names=clean_names,
            max_tries=max_tries,
            timeout=timeout,
            progress=progress,
            verbose=verbose,
            **params,
        ),
        use_cache=cache,
    )


def remessa_works_geometry(
    *,
    cache: bool = True,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """Detalhes das geometrias das obras públicas recebidas pelo sistema RemessaTCEPE

    Endpoint ``Remessa_ObraGeometria`` (group: RemessaTCEPE). Discover parameters and output fields with
    ``tcepepy.params('Remessa_ObraGeometria')`` and ``tcepepy.fields('Remessa_ObraGeometria')``.
    """
    return cached(
        cache_key('Remessa_ObraGeometria', params),
        lambda: request(
            'Remessa_ObraGeometria',
            clean_names=clean_names,
            max_tries=max_tries,
            timeout=timeout,
            progress=progress,
            verbose=verbose,
            **params,
        ),
        use_cache=cache,
    )


def suppliers(
    *,
    cache: bool = True,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """Relação dos Fornecedores

    Endpoint ``Fornecedores`` (group: Fornecedores). Discover parameters and output fields with
    ``tcepepy.params('Fornecedores')`` and ``tcepepy.fields('Fornecedores')``.
    """
    return cached(
        cache_key('Fornecedores', params),
        lambda: request(
            'Fornecedores',
            clean_names=clean_names,
            max_tries=max_tries,
            timeout=timeout,
            progress=progress,
            verbose=verbose,
            **params,
        ),
        use_cache=cache,
    )


def person_creditor_types(
    *,
    cache: bool = True,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """Lista dos tipos de credores

    Endpoint ``TipoCredorPessoa`` (group: Fornecedores). Discover parameters and output fields with
    ``tcepepy.params('TipoCredorPessoa')`` and ``tcepepy.fields('TipoCredorPessoa')``.
    """
    return cached(
        cache_key('TipoCredorPessoa', params),
        lambda: request(
            'TipoCredorPessoa',
            clean_names=clean_names,
            max_tries=max_tries,
            timeout=timeout,
            progress=progress,
            verbose=verbose,
            **params,
        ),
        use_cache=cache,
    )


def sanctions(
    *,
    cache: bool = True,
    clean_names: bool = True,
    max_tries: int = 3,
    timeout: float = 60.0,
    progress: Optional[bool] = None,
    verbose: Optional[bool] = None,
    **params: Any,
) -> pd.DataFrame:
    """Relação das sanções

    Endpoint ``Sancoes`` (group: Fornecedores). Discover parameters and output fields with
    ``tcepepy.params('Sancoes')`` and ``tcepepy.fields('Sancoes')``.
    """
    return cached(
        cache_key('Sancoes', params),
        lambda: request(
            'Sancoes',
            clean_names=clean_names,
            max_tries=max_tries,
            timeout=timeout,
            progress=progress,
            verbose=verbose,
            **params,
        ),
        use_cache=cache,
    )
