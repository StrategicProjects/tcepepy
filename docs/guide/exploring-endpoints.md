# Exploring endpoints

All discovery functions read a catalog bundled with the package, so they work
**offline** and never touch the network. Use them to find the right endpoint
and learn exactly which parameters and fields it supports before you query.

## Browse the catalog

`catalog()` lists every endpoint with its group, title and URL:

```python
import tcepepy as tce

tce.catalog()
#             endpoint     group                           title  url
# 0   ReceitasEstaduais  Receitas  Relação das Receitas Estaduais  ...
# 1  ReceitasMunicipais  Receitas         Receitas Municipais      ...
# ...
```

Filter by keyword (case-insensitive, matches name or title):

```python
tce.catalog(search="licit")     # procurement (licitação) endpoints
tce.catalog(search="obra")      # public works
```

## Inspect input parameters

`params()` returns a DataFrame describing the query parameters an endpoint
accepts:

```python
tce.params("Contratos")
#               api_name               r_name  required    type        description
# 0       UnidadeGestora      unidade_gestora     False  string    Unidade Gestora
# 1       CodigoEfiscoUG       codigo_efisco_ug    False  string    ...
# ...
```

- `api_name` — the exact name expected by the API.
- `r_name` — the `snake_case` alias you can pass instead.
- `required`, `type`, `description` — metadata from the catalog.

Either spelling works when querying, so you can copy whichever column you
prefer.

## Inspect output fields

`fields()` returns the columns an endpoint produces:

```python
tce.fields("Contratos")
#          name             r_name    type      description
# 0  CodigoContrato  codigo_contrato  string    ...
# ...
```

The `r_name` column is the `snake_case` column name you get back in the result
DataFrame (when `clean_names=True`, the default).

## Full endpoint metadata

For programmatic access to everything the catalog knows about an endpoint
(raw dict with `entrada` and `saida`):

```python
meta = tce.endpoint("Contratos")
meta["grupo"], meta["descricao"]
len(meta["entrada"]), len(meta["saida"])
```

## A discovery helper

Putting it together, a small helper to preview any endpoint:

```python
def preview(name):
    print(tce.catalog(search=name))
    print("\nParameters:\n", tce.params(name))
    print("\nFields:\n", tce.fields(name))

preview("Obras")
```
