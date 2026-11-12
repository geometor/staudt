"""Command-line interface (``geometor-staudt``) for inspecting the codex concordance,
running exact symbolic projective & order verification suites, and regenerating SVGs.
"""

from __future__ import annotations

import argparse
import sys
from collections.abc import Sequence

import sympy.geometry as spg
from geometor.model import Model
from rich.console import Console
from rich.table import Table

from geometor.staudt import __version__
from geometor.staudt.concordance import (
    load_concordance,
    verify_source_witnesses,
)
from geometor.staudt.pasch import (
    demonstrate_euclid_i16_pasch_gap,
    demonstrate_euclid_i21_pasch_gap,
)
from geometor.staudt.projective import point_from_abscissa, projective_abscissa
from geometor.staudt.quadrangle import (
    prove_symbolic_quadrangle_uniqueness,
    verify_quadrangle_independence,
)
from geometor.staudt.render import build_all_figures
from geometor.staudt.throws import (
    construct_von_staudt_addition,
    construct_von_staudt_multiplication,
    verify_golden_throw_identity,
)

__all__ = ["main"]


def _cmd_summary(console: Console) -> int:
    entries = load_concordance()
    table = Table(title=f"GEOMETOR • staudt v{__version__} — Cross-Corpus Concordance")
    table.add_column("ID", style="cyan", no_wrap=True)
    table.add_column("Treatise & Locus", style="magenta")
    table.add_column("Title", style="bold")
    table.add_column("Linked Sister Repos", style="green")
    for entry in entries:
        repos = ", ".join(sorted(entry.cross_refs.keys()))
        table.add_row(entry.id, f"{entry.treatise} ({entry.locus_de})", entry.title, repos)
    console.print(table)
    return 0


def _cmd_verify(console: Console) -> int:
    witness_report = verify_source_witnesses()
    uniq = prove_symbolic_quadrangle_uniqueness()
    ind = verify_quadrangle_independence(
        spg.Point(0, 0),
        spg.Point(6, 0),
        spg.Point(2, 0),
        (spg.Point(2, 4), spg.Point(2, 2)),
        (spg.Point(3, -3), spg.Point(1, -2)),
    )

    m = Model("cli_throws", auto_intersect=False, enable_logging=False)
    p0 = m.given_point(0, 0, label="P0")
    p1 = m.given_point(1, 0, label="P1")
    pinf = m.given_point(8, 0, label="Pinf")
    p2_raw = point_from_abscissa(p0, p1, pinf, 2)
    p3_raw = point_from_abscissa(p0, p1, pinf, 3)
    p2 = m.given_point(p2_raw.x, p2_raw.y, label="P2")
    p3 = m.given_point(p3_raw.x, p3_raw.y, label="P3")
    s5 = construct_von_staudt_addition(m, p0, p1, pinf, p2, p3, label="P5")
    m6 = construct_von_staudt_multiplication(m, p0, p1, pinf, p2, p3, label="P6")
    golden = verify_golden_throw_identity(spg.Point(0, 0), spg.Point(1, 0), spg.Point(8, 0))
    _, i16 = demonstrate_euclid_i16_pasch_gap()
    _, i21 = demonstrate_euclid_i21_pasch_gap()

    console.print("[bold green]All symbolic & archival checks passed![/bold green]")
    console.print(f"  • Source witnesses verified: {witness_report['count']} (all_ok={witness_report['all_ok']})")
    console.print(f"  • Symbolic quadrangle harmonic 4th: D_x = {uniq['D_x']}, CR = {uniq['cross_ratio']}")
    console.print(f"  • Concrete quadrangle independence: D1 == D2 == {ind['D1']} (circles={ind['circles_used']})")
    console.print(
        f"  • Algebra of Throws: P2 + P3 abscissa = {projective_abscissa(p0, p1, pinf, s5)}, "
        f"P2 * P3 abscissa = {projective_abscissa(p0, p1, pinf, m6)}"
    )
    console.print(
        f"  • Golden Throw over Q(phi): P_phi^2 == P_phi + P1 -> {golden['points_coincide']} "
        f"(abscissa = {golden['abscissa_phi_squared']})"
    )
    console.print(
        f"  • Pasch Axiom audits: Euclid I.16 crossbar={i16['K_between_A_and_D']}, "
        f"Euclid I.21 exit E={i21['E_on_AC']}"
    )
    return 0 if witness_report["all_ok"] else 1


def _cmd_build_figures(console: Console) -> int:
    paths = build_all_figures()
    for p in paths:
        console.print(f"[green]Generated[/green] {p}")
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    """Entry point for ``geometor-staudt``."""
    parser = argparse.ArgumentParser(
        prog="geometor-staudt",
        description="GEOMETOR • staudt CLI (von Staudt 1847/1857 & Pasch 1882)",
    )
    sub = parser.add_subparsers(dest="command")
    sub.add_parser("summary", help="Display cross-corpus concordance table")
    sub.add_parser("verify", help="Run exact SymPy straightedge & Pasch verification suite")
    sub.add_parser("build-figures", help="Regenerate all 8 .euclid-graphic SVG diagrams")

    args = parser.parse_args(list(argv) if argv is not None else None)
    console = Console()
    cmd = args.command or "summary"
    if cmd == "summary":
        return _cmd_summary(console)
    if cmd == "verify":
        return _cmd_verify(console)
    if cmd == "build-figures":
        return _cmd_build_figures(console)
    return 1


if __name__ == "__main__":
    sys.exit(main())
