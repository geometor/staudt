#!/usr/bin/env python3
"""Demo 03 — Von Staudt's Straightedge Multiplication of Throws & Golden Section Over Q(phi).

Corresponds to Karl Georg Christian von Staudt, *Beiträge zur Geometrie der Lage*, Heft 2 (1857),
§ 20 (*Produkte aus Würfen*, arts. 268–275) & § 29 (*Von den Abscissen*, art. 404).
Constructs P2 * P3 = P6, verifies field distributivity, and proves over Q(phi) that straightedge
addition and multiplication satisfy P_phi * P_phi == P_phi + P1 (phi^2 = phi + 1) with zero circles.
"""

from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
for candidate in (REPO_ROOT / "src", REPO_ROOT.parent / "model" / "src"):
    if str(candidate) not in sys.path:
        sys.path.insert(0, str(candidate))

import sympy.geometry as spg
from geometor.model import Model, zero_test
from rich.console import Console

from geometor.staudt import (
    assert_straightedge_only,
    construct_von_staudt_addition,
    construct_von_staudt_multiplication,
    point_from_abscissa,
    projective_abscissa,
    verify_golden_throw_identity,
)


def main() -> None:
    console = Console()
    console.rule("[bold cyan]03 · Von Staudt (1857) § 20 — Straightedge Multiplication & Q(phi) Throws")

    model = Model("demo_multiplication", auto_intersect=False, enable_logging=False)
    P0 = model.given_point(0, 0, label="P0")
    P1 = model.given_point(1, 0, label="P1")
    Pinf = model.given_point(8, 0, label="Pinf")

    p2_raw = point_from_abscissa(P0, P1, Pinf, 2)
    p3_raw = point_from_abscissa(P0, P1, Pinf, 3)
    P2 = model.given_point(p2_raw.x, p2_raw.y, label="P2")
    P3 = model.given_point(p3_raw.x, p3_raw.y, label="P3")

    P6 = construct_von_staudt_multiplication(model, P0, P1, Pinf, P2, P3, label="P6")

    # Verify field distributivity: (P2 + P3) * P2 == P2*P2 + P3*P2 == P10
    P5 = construct_von_staudt_addition(model, P0, P1, Pinf, P2, P3, label="P5")
    lhs = construct_von_staudt_multiplication(model, P0, P1, Pinf, P5, P2, label="LHS_10")
    P4 = construct_von_staudt_multiplication(model, P0, P1, Pinf, P2, P2, label="P4")
    rhs = construct_von_staudt_addition(model, P0, P1, Pinf, P4, P6, label="RHS_10")
    assert_straightedge_only(model)
    assert zero_test(lhs.x - rhs.x) and zero_test(lhs.y - rhs.y)

    console.print(
        f"  Product P2 · P3       : {P6}  (abscissa = {projective_abscissa(P0, P1, Pinf, P6)})"
    )
    console.print(
        f"  Distributivity (2+3)·2: LHS={lhs} == RHS={rhs} (abscissa = {projective_abscissa(P0, P1, Pinf, lhs)})"
    )
    console.print(f"  Compass circles used  : {len(model.circles)}")

    golden = verify_golden_throw_identity(spg.Point(0, 0), spg.Point(1, 0), spg.Point(8, 0))
    console.print("[bold]Golden Throw Identity over Q(phi) on Finite Projective Horizon:[/bold]")
    console.print(f"  P_phi                 : {golden['P_phi']}  (phi = {golden['phi']})")
    console.print(f"  P_phi · P_phi         : {golden['P_phi_squared']}")
    console.print(f"  P_phi + P1            : {golden['P_phi_plus_1']}")
    console.print(
        f"  Exact coincidence     : {golden['points_coincide']}  (abscissa = {golden['abscissa_phi_squared']}, norm = {golden['abscissa_norm']})"
    )


if __name__ == "__main__":
    main()
