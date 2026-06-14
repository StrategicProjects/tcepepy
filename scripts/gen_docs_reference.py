"""Generate the grouped API-reference pages for the MkDocs site.

Writes one Markdown page per category under ``docs/reference/`` with
mkdocstrings ``:::`` directives. Run after changing the public API::

    python scripts/gen_docs_reference.py

Mirrors the reference grouping of the R package's pkgdown site.
"""

from __future__ import annotations

import os

# (filename, nav title, description, [fully-qualified object paths])
GROUPS = [
    (
        "core",
        "Core",
        "Low-level function for querying any API endpoint.",
        ["tcepepy.request.request"],
    ),
    (
        "catalog",
        "Endpoint catalog",
        "Discover endpoints and inspect input/output fields from the built-in catalog (offline).",
        [
            "tcepepy.catalog.catalog",
            "tcepepy.catalog.endpoint",
            "tcepepy.catalog.params",
            "tcepepy.catalog.fields",
        ],
    ),
    (
        "cache",
        "Cache",
        "Manage the in-memory result cache.",
        ["tcepepy.cache.cache_info", "tcepepy.cache.cache_clear"],
    ),
    (
        "config",
        "Configuration",
        "Runtime settings (also configurable via TCEPEPY_* environment variables).",
        ["tcepepy.config.Config"],
    ),
    (
        "revenues",
        "Revenues",
        "State and municipal revenue data.",
        ["state_revenues", "municipal_revenues", "budgeted_revenues"],
    ),
    (
        "expenditures",
        "Expenditures",
        "State and municipal expenditure data.",
        [
            "state_expenditures",
            "municipal_expenditures",
            "municipal_transfers",
            "municipal_creditor_types",
            "state_creditor_types",
        ],
    ),
    (
        "commitments",
        "Budget commitments",
        "Commitment (empenho) summaries, liquidations, payments and line items.",
        [
            "commitment_summary",
            "commitment_liquidations",
            "commitment_payments",
            "state_commitment_items",
            "state_price_comparison",
        ],
    ),
    (
        "suppliers",
        "Suppliers",
        "Supplier registry and sanctions.",
        ["suppliers", "sanctions", "person_creditor_types"],
    ),
    (
        "procurement",
        "Procurement & contracts",
        "Bids, contracts, amendments, agreements and related lookup tables.",
        [
            "contracts",
            "contract_documents",
            "contract_items",
            "contract_amendments",
            "agreements",
            "bids",
            "bid_details",
            "bid_documents",
            "bid_stages",
            "bid_modalities",
            "bid_statuses",
            "bid_legal_basis",
            "object_characteristics",
            "object_classifications",
            "object_nature",
        ],
    ),
    (
        "public-works",
        "Public works",
        "Engineering works, contractors, audits and school transport.",
        [
            "public_works",
            "public_works_contractors",
            "public_works_audits",
            "school_transport",
        ],
    ),
    (
        "processes",
        "Legal processes",
        "Processes, determinations, recommendations, outcomes, debts, fines and spending limits.",
        [
            "processes",
            "determinations",
            "consideranda",
            "recommendations",
            "outcomes",
            "retirement_outcomes",
            "special_accountability",
            "debts_fines",
            "spending_limits",
        ],
    ),
    (
        "personnel",
        "Personnel",
        "Public servant records.",
        ["servants"],
    ),
    (
        "reference-tables",
        "Reference tables",
        "Municipalities, managed entities, sub-units, creditor types, payroll types, "
        "funding sources and inactivation reasons.",
        [
            "municipalities",
            "entities",
            "state_entities",
            "municipal_entities",
            "sub_units",
            "creditor_types",
            "payroll_types",
            "funding_sources",
            "inactivation_reasons",
        ],
    ),
    (
        "remessa",
        "RemessaTCEPE",
        "Data from the RemessaTCEPE system: benefit types, reference sources/dates/codes, "
        "update indices, budget statuses, legal instruments, procurement processes and works.",
        [
            "benefit_types",
            "reference_sources",
            "reference_dates",
            "reference_codes",
            "update_indices",
            "budget_statuses",
            "legal_instruments",
            "legal_instrument_documents",
            "legal_instrument_items",
            "legal_instrument_participants",
            "procurement_processes",
            "procurement_process_documents",
            "procurement_process_budget",
            "procurement_process_participants",
            "remessa_works",
            "remessa_works_execution",
            "remessa_works_geometry",
        ],
    ),
]

_DIRECTIVE = """::: {path}
    options:
      show_root_heading: true
      show_root_full_path: false
      heading_level: 3

"""


def _resolve(obj: str) -> str:
    """Endpoint wrappers live in tcepepy.endpoints; core objects are fully qualified."""
    return obj if "." in obj else f"tcepepy.endpoints.{obj}"


def _write_endpoint_table(root: str) -> None:
    """Generate guide/endpoints-reference.md as a table from the catalog."""
    import sys

    sys.path.insert(0, os.path.join(root, "src"))
    from tcepepy._generate_endpoints import NAME_TO_ENDPOINT
    from tcepepy.catalog import _find_method

    lines = [
        "# Endpoint reference\n",
        "All 71 endpoints, with the `tcepepy` wrapper function for each. Use",
        "`tcepepy.params(<endpoint>)` and `tcepepy.fields(<endpoint>)` to inspect",
        "parameters and output fields.\n",
        "| Function | Endpoint | Group | Description |",
        "| --- | --- | --- | --- |",
    ]
    for name, endpoint in NAME_TO_ENDPOINT.items():
        m = _find_method(endpoint) or {}
        grupo = (m.get("grupo") or "").strip()
        desc = (m.get("descricao") or "").strip().replace("|", "\\|")
        lines.append(f"| `{name}()` | `{endpoint}` | {grupo} | {desc} |")

    path = os.path.join(root, "docs", "guide", "endpoints-reference.md")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")


def main() -> None:
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    out_dir = os.path.join(root, "docs", "reference")
    os.makedirs(out_dir, exist_ok=True)

    for slug, title, desc, objects in GROUPS:
        lines = [f"# {title}\n", f"{desc}\n"]
        for obj in objects:
            lines.append(_DIRECTIVE.format(path=_resolve(obj)))
        with open(os.path.join(out_dir, f"{slug}.md"), "w", encoding="utf-8") as fh:
            fh.write("\n".join(lines))

    # Reference landing page
    index = ["# API reference\n", "Functions grouped by topic.\n"]
    for slug, title, desc, _ in GROUPS:
        index.append(f"- [{title}]({slug}.md) — {desc}")
    with open(os.path.join(out_dir, "index.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(index) + "\n")

    _write_endpoint_table(root)

    nav = "\n".join(f"      - {title}: reference/{slug}.md" for slug, title, _, _ in GROUPS)
    print(f"Wrote {len(GROUPS)} reference pages to {out_dir}")
    print("\nnav snippet for mkdocs.yml (under 'Reference:'):\n")
    print("      - Overview: reference/index.md")
    print(nav)


if __name__ == "__main__":
    main()
