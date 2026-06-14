# tcepepy

Python client for the [TCE-PE](https://www.tce.pe.gov.br/) (Tribunal de Contas
do Estado de Pernambuco) **Open Data API** — the Python counterpart of the R
package [`tceper`](https://github.com/StrategicProjects/tceper).

`tcepepy` wraps **71 API endpoints** into friendly functions that accept
`snake_case` parameter names and return [`pandas`](https://pandas.pydata.org/)
DataFrames. A built-in catalog lets you discover endpoints and inspect their
parameters and output fields — all offline.

!!! warning "Geo-restriction"
    The API host (`sistemas.tcepe.tc.br`) only accepts connections from
    **Brazilian IP addresses**. From outside Brazil, queries time out. The
    discovery helpers (`catalog()`, `params()`, `fields()`) work offline
    anywhere, as they read from the bundled catalog.

!!! note "Language note"
    Wrapper functions are named in English, but the underlying API is in
    Portuguese — so you pass *parameters* in Portuguese, e.g.
    `state_revenues(AnoReferencia=2025)`.

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

# 3. Query (needs a Brazilian IP) — snake_case or original API names both work
tce.contracts(codigo_efisco_ug="510101")
tce.contracts(CodigoEfiscoUG="510101", ano_contrato="2025")
```

## Where to next

- **[Getting started](guide/getting-started.md)** — install, query, work with results.
- **[Exploring endpoints](guide/exploring-endpoints.md)** — discover endpoints, parameters and fields.
- **[Endpoint reference](guide/endpoints-reference.md)** — the full list of 71 endpoints.
- **[API reference](reference/index.md)** — every function, grouped by topic.
