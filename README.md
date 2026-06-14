# tcepepy

Python client for the [TCE-PE](https://www.tce.pe.gov.br/) (Tribunal de Contas
do Estado de Pernambuco) **Open Data API**. It is the Python counterpart of the
R package [`tceper`](https://github.com/StrategicProjects/tceper).

`tcepepy` wraps **71 API endpoints** into friendly functions that accept
`snake_case` parameter names and return `pandas` DataFrames. A built-in catalog
lets you discover endpoints and inspect their parameters and output fields —
all offline, without leaving Python.

> ⚠️ **Geo-restriction.** The API host (`sistemas.tcepe.tc.br`) only accepts
> connections from **Brazilian IP addresses**. From outside Brazil, queries
> time out. The discovery helpers (`catalog()`, `params()`, `fields()`) work
> offline anywhere, as they read from the bundled catalog.

> ❗ **Language note.** Wrapper functions are named in English, but the
> underlying API is in Portuguese — so you pass *parameters* in Portuguese,
> e.g. `state_revenues(AnoReferencia=2025)`. See the
> [official endpoint list](https://sistemas.tcepe.tc.br/DadosAbertos/Exemplo!listar).

## Installation

```bash
pip install tcepepy            # core (httpx + pandas)
pip install "tcepepy[rich]"    # prettier console output
```

## Quick start

```python
import tcepepy as tce

# 1. Discover endpoints (offline)
tce.catalog()
tce.catalog(search="contrat")

# 2. Inspect parameters and output fields (offline)
tce.params("Contratos")
tce.fields("Contratos")

# 3. Query (needs a Brazilian IP) — snake_case or the original API names both work
tce.contracts(codigo_efisco_ug="510101")
tce.contracts(CodigoEfiscoUG="510101", ano_contrato="2025")
```

## Explore the API

```python
tce.catalog()
#       endpoint      group                title  url
# 0  ReceitasEstaduais  Receitas  Relação das Receitas Estaduais  ...

tce.params("Contratos")    # api_name, r_name, required, type, description
tce.fields("Contratos")    # name, r_name, type, description
```

Use `snake_case` (`r_name`) or the original API names — both are accepted.

## Cache

Every wrapper caches results in memory, keyed by endpoint + parameters
(default TTL: 1 hour).

```python
tce.contracts(codigo_efisco_ug="510101")                 # hits the API
tce.contracts(codigo_efisco_ug="510101")                 # cache hit (instant)
tce.contracts(codigo_efisco_ug="510101", cache=False)    # force fresh

tce.cache_info()    # inspect cached entries
tce.cache_clear()   # clear all
```

## Parameter validation

Parameters are validated against the catalog. Passing an unknown parameter
raises an error listing the allowed ones:

```python
tce.contracts(xyz="foo")
# tcepepy.catalog.UnknownParameterError: Unknown query parameter(s) for
# endpoint 'Contratos': xyz.
# Allowed parameters:
#   - unidade_gestora (UnidadeGestora)
#   - codigo_efisco_ug (CodigoEfiscoUG)
#   ...
```

## Configuration

```python
tce.config.verbose = True      # print the final API URL on every call
tce.config.progress = False    # silence status messages
tce.config.cache_ttl = 7200    # cache TTL in seconds
```

Or via environment variables: `TCEPEPY_VERBOSE`, `TCEPEPY_PROGRESS`,
`TCEPEPY_CACHE_TTL`.

## Direct access

To call any endpoint (including ones without a dedicated wrapper) using API
parameter names directly:

```python
tce.request("Contratos", CodigoEfiscoUG="510101", AnoContrato="2025")
```

## API limits

The API returns at most **100,000 records** per request; `tcepepy` warns when
this limit is hit. Use filters to narrow your query.

## License

MIT. This package is an unofficial client; the data belongs to TCE-PE.
