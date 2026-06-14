# Changelog

## 0.1.0 (unreleased)

Initial release — Python port of the R package
[`tceper`](https://github.com/StrategicProjects/tceper).

- 71 endpoint wrapper functions returning `pandas` DataFrames with snake_case
  columns (generated from the bundled catalog).
- Offline discovery: `catalog()`, `endpoint()`, `params()`, `fields()`.
- Low-level `request()` for any endpoint, with parameter validation against the
  catalog and snake_case ↔ API-name mapping.
- Correct handling of the TCE-PE API quirks: literal `!json` Struts2 URLs and
  ISO-8859-1 (Latin-1) request/response encoding.
- In-memory result cache with TTL (`cache_info()`, `cache_clear()`).
- Configuration via `config` object or `TCEPEPY_*` environment variables.
- Optional pretty console output via `rich` (`pip install tcepepy[rich]`).
