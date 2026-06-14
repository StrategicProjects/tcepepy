# Getting started

## Install

```bash
pip install tcepepy
```

For prettier console output (status messages, rules), install the optional
`rich` extra:

```bash
pip install "tcepepy[rich]"
```

## The three-step workflow

`tcepepy` is designed around a simple loop: **discover → inspect → query**.

```python
import tcepepy as tce

tce.catalog(search="contrat")   # 1. discover an endpoint
tce.params("Contratos")         # 2. inspect its parameters
tce.contracts(codigo_efisco_ug="510101")   # 3. query it
```

Steps 1 and 2 read a catalog bundled with the package and work **offline,
anywhere**. Step 3 reaches the live API, which is only accessible from a
Brazilian IP address.

## Passing parameters

Every wrapper accepts query parameters as keyword arguments. You may use either
the original API name or its `snake_case` alias — both resolve to the same
parameter:

```python
tce.contracts(CodigoEfiscoUG="510101")        # API name
tce.contracts(codigo_efisco_ug="510101")       # snake_case alias
tce.contracts(codigo_efisco_ug="510101", ano_contrato="2025")  # multiple filters
```

`None` values are dropped automatically, which makes optional filters easy:

```python
ano = None
tce.contracts(codigo_efisco_ug="510101", ano_contrato=ano)  # ano_contrato omitted
```

Unknown parameters raise an error listing the allowed ones:

```python
tce.contracts(xyz="foo")
# UnknownParameterError: Unknown query parameter(s) for endpoint 'Contratos': xyz.
# Allowed parameters:
#   - unidade_gestora (UnidadeGestora)
#   - codigo_efisco_ug (CodigoEfiscoUG)
#   ...
```

## Working with results

Every wrapper returns a `pandas.DataFrame` with `snake_case` column names. An
empty DataFrame means no records matched.

```python
df = tce.contracts(codigo_efisco_ug="510101")
df.head()
df.columns          # snake_case names
df["valor"].sum()
```

To keep the original API column names, pass `clean_names=False`:

```python
tce.contracts(codigo_efisco_ug="510101", clean_names=False)
```

## Caching

Results are cached in memory, keyed by endpoint + parameters (default TTL: one
hour). Repeated identical calls return instantly.

```python
tce.contracts(codigo_efisco_ug="510101")                 # hits the API
tce.contracts(codigo_efisco_ug="510101")                 # cache hit
tce.contracts(codigo_efisco_ug="510101", cache=False)    # force fresh

tce.cache_info()    # inspect cached entries
tce.cache_clear()   # clear all
```

## Configuration

```python
tce.config.verbose = True      # print the final API URL on every call
tce.config.progress = False    # silence status messages
tce.config.cache_ttl = 7200    # cache TTL in seconds
```

Or via environment variables before importing: `TCEPEPY_VERBOSE`,
`TCEPEPY_PROGRESS`, `TCEPEPY_CACHE_TTL`.

## Direct access

To call any endpoint — including those without a dedicated wrapper — use
`request()` with the exact API parameter names:

```python
tce.request("Contratos", CodigoEfiscoUG="510101", AnoContrato="2025")
```
