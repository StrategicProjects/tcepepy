# Endpoint reference

All 71 endpoints, with the `tcepepy` wrapper function for each. Use
`tcepepy.params(<endpoint>)` and `tcepepy.fields(<endpoint>)` to inspect
parameters and output fields.

| Function | Endpoint | Group | Description |
| --- | --- | --- | --- |
| `state_revenues()` | `ReceitasEstaduais` | Receitas | Relação das Receitas Estaduais |
| `municipal_revenues()` | `ReceitasMunicipais` | Receitas | Relação das Receitas Municipais |
| `budgeted_revenues()` | `ReceitasPrevistas` | Receitas | Relação das Receitas Previstas (apenas Municipais) |
| `state_expenditures()` | `DespesasEstaduais` | Despesas | Relação das Despesas Estaduais |
| `municipal_expenditures()` | `DespesasMunicipais` | Despesas | Relação das Despesas Municipais - Chave composta (ID_EMPENHO, ANOREFERENCIA, NUMERO_EMPENHO e ID_UNIDADE_GESTORA) |
| `municipal_transfers()` | `TransferenciasConcedidasMunicipais` | Despesas | Relação das transferências concedidas entre unidades juirisdicionadas do mesmo município |
| `municipal_creditor_types()` | `TipoCredorMunicipal` | Despesas | Lista dos tipos de credores Municipal |
| `state_creditor_types()` | `TipoCredorEstadual` | Despesas | Lista dos tipos de credores Estadual |
| `commitment_summary()` | `EmpenhoResumo` | Despesas | Relação dos Valores Originais, Reforços e Estornos dos Empenhos Municipais e Estaduais |
| `commitment_liquidations()` | `EmpenhoLiquidacao` | Despesas | Relação das Liquidações dos Empenhos Municipais e Estaduais |
| `commitment_payments()` | `EmpenhoPagamento` | Despesas | Relação dos Pagamentos dos Empenhos (apenas Municipais) |
| `state_commitment_items()` | `ItemEmpenhoEstadual` | Despesas | Relaçao de cada parte que compõem os empenhos Estaduais |
| `state_price_comparison()` | `ComparativoPrecoEstado` | Despesas | Itens dos empenhos estaduais com valores para comparação de preços |
| `contracts()` | `Contratos` | Licitações, Contratos e Convênios | Listas dos Contratos Estaduais e Municipais |
| `contract_documents()` | `ContratoDocumentos` | Licitações, Contratos e Convênios | Lista dos documentos de um contrato |
| `contract_items()` | `ContratoItemObjeto` | Licitações, Contratos e Convênios | Relaçao de cada parte que compõem o contrato |
| `contract_amendments()` | `TermoAditivo` | Licitações, Contratos e Convênios | Listas dos termos Aditivos dos contratos Estaduais e Municipais |
| `agreements()` | `Convenios` | Licitações, Contratos e Convênios | Listas dos Convênios Estaduais e Municipais |
| `bids()` | `LicitacaoUG` | Licitações, Contratos e Convênios | Relação das Licitações |
| `bid_details()` | `LicitacoesDetalhes` | Licitações, Contratos e Convênios | Relação das Licitações com os respectivos Licitantes |
| `bid_documents()` | `LicitacoesDocumentos` | Licitações, Contratos e Convênios | Lista dos documentos de uma licitação |
| `bid_stages()` | `EstagioLicitacao` | Licitações, Contratos e Convênios | Listas dos estágios de uma licitação |
| `bid_modalities()` | `ModalidadeLicitacao` | Licitações, Contratos e Convênios | Listas dos tipos de modalidade de uma licitação |
| `bid_statuses()` | `SituacaoLicitacao` | Licitações, Contratos e Convênios | Listas dos tipos de situação de uma licitação |
| `object_characteristics()` | `CaracteristicaObjeto` | Licitações, Contratos e Convênios | Listas dos tipos de característica de um objeto |
| `object_classifications()` | `ClassificacaoObjeto` | Licitações, Contratos e Convênios | Listas dos tipos de classificação de um objeto |
| `bid_legal_basis()` | `FundamentacaoLegalLicitacao` | Licitações, Contratos e Convênios | Lista dos fundamentação legal da licitação |
| `object_nature()` | `NaturezaObjeto` | Licitações, Contratos e Convênios | Listas dos tipos de natureza de um objeto |
| `processes()` | `Processos` | Processos | Listas dos processos físicos e eletrônicos formalizados |
| `determinations()` | `Determinacoes` | Processos | Lista das determinações dos processos eletrônicos transitados em julgado |
| `consideranda()` | `Considerandos` | Processos | Listas dos considerandos dos processos eletrônicos transitados em julgado |
| `recommendations()` | `Recomendacoes` | Processos | Listas das recomendações dos processos eletrônicos transitados em julgado |
| `outcomes()` | `Resultados` | Processos | Lista dos resultados dos processos eletrônicos transitados em julgado |
| `retirement_outcomes()` | `ResultadosAPR` | Processos | Lista dos resultados dos processos eletrônicos da modalidade Aposentadoria, Pensão e Reforma |
| `special_accountability()` | `ResultadosTomadaContaEspecial` | Processos | ResultadosTomadaContaEspecial |
| `debts_fines()` | `DebitosMultas` | Processos | Relação das débitos e multas |
| `spending_limits()` | `DadosLimiteGastos` | Processos | Dados de limites de gastos dos processos julgados de contas de governo |
| `public_works()` | `Obras` | Obras | Obras e serviços de engenharia fiscalizados pelo Tribunal de Contas. |
| `public_works_contractors()` | `ObrasDadosContratacao` | Obras | Referem-se aos dados das empresas contratadas para a obra. |
| `public_works_audits()` | `DadosObrasAuditoria` | Obras | Referem-se aos dados das obras |
| `school_transport()` | `TransporteEscolar` | Transporte Escolar | Serviços de transporte escolar fiscalizados pelo Tribunal de Contas. |
| `servants()` | `ListaServidores` | Pessoal | Lista dos servidores municipais e estaduais de Pernambuco (base Sagres Pessoal) |
| `municipalities()` | `Municipios` | Informações básicas | Relação dos municípios |
| `entities()` | `UnidadesJurisdicionadas` | Informações básicas | Relação das Unidades Jurisdicionadas |
| `state_entities()` | `UnidadesJurisdicionadasEstaduais` | Informações básicas | Relação das Unidades Jurisdicionais Estaduais |
| `municipal_entities()` | `UnidadesJurisdicionadasMunicipais` | Informações básicas | Relação das Unidades Jurisdicionais Municipais |
| `sub_units()` | `SubunidadesUnidadesJurisdicionadas` | Informações básicas | Relação das Subunidades das Unidades Jurisdicionadas |
| `creditor_types()` | `TipoCredor` | Informações básicas | Relação dos tipos de fornecedores |
| `payroll_types()` | `TipoFolha` | Informações básicas | Relação dos tipos de folha |
| `funding_sources()` | `TipoFonteRecurso` | Informações básicas | Relação das fontes de recursos |
| `inactivation_reasons()` | `TipoMotivoInativacao` | Informações básicas | Relação dos tipos de motivo de inativação |
| `benefit_types()` | `TipoBeneficio` | RemessaTCEPE | Tipo de benefício do lote/item |
| `reference_sources()` | `FonteReferencia` | RemessaTCEPE | Possíveis fontes de referência para importação dos itens do orçamento estimativo |
| `reference_dates()` | `DataReferencia` | RemessaTCEPE | Datas disponíveis para as fontes de referência utilizadas na importação dos itens do orçamento estimativo |
| `reference_codes()` | `CodigoReferencia` | RemessaTCEPE | Códigos de referência para importação dos itens do orçamento estimativo |
| `update_indices()` | `IndiceAtualizacao` | RemessaTCEPE | Índices de atualização que devem ser utilizados na planilha de importação do orçamento estimativo |
| `budget_statuses()` | `OrcamentoSituacao` | RemessaTCEPE | Possíveis situações dos itens/lotes do orçamento estimativo |
| `legal_instruments()` | `Remessa_InstrumentoJuridico` | RemessaTCEPE | Dados dos instrumentos jurídicos cadastrados no RemessaTCEPE |
| `legal_instrument_documents()` | `Remessa_InstrumentoJuridicoDocumento` | RemessaTCEPE | Documentos de um instrumento jurídico |
| `legal_instrument_items()` | `Remessa_InstrumentoJuridicoItens` | RemessaTCEPE | Itens de um instrumento jurídico |
| `legal_instrument_participants()` | `Remessa_InstrumentoJuridicoParticipantes` | RemessaTCEPE | Partes de um instrumento jurídico |
| `procurement_processes()` | `Remessa_ProcessoContratacao` | RemessaTCEPE | Dados dos processos de contratação cadastrados no RemessaTCEPE |
| `procurement_process_documents()` | `Remessa_ProcessoContratacaoDocumento` | RemessaTCEPE | Documentos de um processo de contratação |
| `procurement_process_budget()` | `Remessa_ProcessoContratacaoOrcamento` | RemessaTCEPE | Lotes e itens do orçamento de um processo de contratação |
| `procurement_process_participants()` | `Remessa_ProcessoContratacaoParticipantes` | RemessaTCEPE | Lista de licitantes/participantes de um processo de contratação |
| `remessa_works()` | `Remessa_Obra` | RemessaTCEPE | Detalhes das obras públicas recebidas pelo sistema RemessaTCEPE |
| `remessa_works_execution()` | `Remessa_ObraExecucao` | RemessaTCEPE | Detalhes das execuções das obras públicas recebidas pelo sistema RemessaTCEPE |
| `remessa_works_geometry()` | `Remessa_ObraGeometria` | RemessaTCEPE | Detalhes das geometrias das obras públicas recebidas pelo sistema RemessaTCEPE |
| `suppliers()` | `Fornecedores` | Fornecedores | Relação dos Fornecedores |
| `person_creditor_types()` | `TipoCredorPessoa` | Fornecedores | Lista dos tipos de credores |
| `sanctions()` | `Sancoes` | Fornecedores | Relação das sanções |
