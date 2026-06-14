"""Thin messaging layer: pretty output via ``rich`` when available, plain
``print``/``warnings`` otherwise. Mirrors the role of the ``cli`` package in
the R ``tceper`` client.
"""

from __future__ import annotations

import warnings

try:  # pragma: no cover - exercised indirectly
    from rich.console import Console as _RichConsole

    _console = _RichConsole(stderr=True)
    _HAS_RICH = True
except Exception:  # pragma: no cover
    _console = None
    _HAS_RICH = False

__all__ = ["info", "success", "warn", "rule", "has_rich"]


def has_rich() -> bool:
    return _HAS_RICH


def info(message: str) -> None:
    if _HAS_RICH:
        _console.print(f"[cyan]ℹ[/cyan] {message}")
    else:
        print(message)


def success(message: str) -> None:
    if _HAS_RICH:
        _console.print(f"[green]✔[/green] {message}")
    else:
        print(message)


def rule(label: str) -> None:
    if _HAS_RICH:
        _console.rule(f"[bold]{label}[/bold]", align="left")
    else:
        print(f"-- {label} " + "-" * max(0, 60 - len(label)))


def warn(message: str) -> None:
    """Emit a Python warning (always), pretty-printed when rich is present."""
    if _HAS_RICH:
        _console.print(f"[yellow]![/yellow] {message}")
    warnings.warn(message, stacklevel=3)
