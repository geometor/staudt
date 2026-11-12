#!/usr/bin/env python3
"""Demo 01 — Pure Straightedge Complete-Quadrangle Harmonic Fourth & Desarguesian Uniqueness.

Corresponds to Karl Georg Christian von Staudt, *Geometrie der Lage* (1847), §§ 7–8 (arts. 79–96).
Constructs the fourth harmonic point D to (A, B; C, D) = -1 using ONLY an unmarked straightedge
(zero compass circles), verifies exact invariance across independent quadrangles, and proves
universal uniqueness over free SymPy symbolic parameters.
"""

from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
for candidate in (REPO_ROOT / "src", REPO_ROOT.parent / "model" / "src"):
    if str(candidate) not in sys.path:
        sys.path.insert(0, str(candidate))

import sympy.geometry as spg
from geometor.model import Model, cross_ratio, is_harmonic
from rich.console import Console

from geometor.staudt import (
    assert_straightedge_only,
    construct_harmonic_fourth_straightedge,
    pair_separates,
    prove_symbolic_quadrangle_uniqueness,
    verify_quadrangle_independence,
)


def main() -> None:
    console = Console()
    console.rule("[bold cyan]01 · Von Staudt (1847) § 8 Art. 93 — Straightedge Harmonic Fourth")

    model = Model("demo_harmonic_fourth", auto_intersect=False, enable_logging=False)
    A = model.given_point(0, 0, label="A")
    B = model.given_point(6, 0, label="B")
    C = model.given_point(2, 0, label="C")
    E = model.given_point(2, 4, label="E")
    G = model.given_point(2, 2, label="G")

    D = construct_harmonic_fourth_straightedge(model, A, B, C, E, G, label="D")
    assert_straightedge_only(model)

    console.print(f"  Given collinear triad : A = {A}, B = {B}, C = {C}")
    console.print(f"  Constructed 4th point : D = {D}")
    console.print(f"  Exact cross-ratio     : (A, B; C, D) = {cross_ratio(A, B, C, D)}")
    console.print(f"  Harmonic & separating : is_harmonic={is_harmonic(A, B, C, D)}, AB // CD={pair_separates(A, B, C, D)}")
    console.print(f"  Compass circles used  : {len(model.circles)} (lines={len(model.lines)})")

    ind = verify_quadrangle_independence(
        spg.Point(0, 0),
        spg.Point(6, 0),
        spg.Point(2, 0),
        quad1=(spg.Point(2, 4), spg.Point(2, 2)),
        quad2=(spg.Point(5, -3), spg.Point(-1, -5)),
    )
    console.print(
        f"  Quadrangle invariance : D1 = {ind['D1']} == D2 = {ind['D2']} (identical={ind['identical']})"
    )

    sym_proof = prove_symbolic_quadrangle_uniqueness()
    console.print(
        f"  Symbolic proof ∀(u,v,t): D_x(c) = {sym_proof['D_x']}, cross-ratio = {sym_proof['cross_ratio']}"
    )


if __name__ == "__main__":
    main()
