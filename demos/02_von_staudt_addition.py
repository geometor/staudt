#!/usr/bin/env python3
"""Demo 02 — Von Staudt's Pure Straightedge Addition of Throws (Summen von Würfen).

Corresponds to Karl Georg Christian von Staudt, *Beiträge zur Geometrie der Lage*, Heft 2 (1857),
§ 19 (arts. 256–267) & § 29 (art. 404). Demonstrates exact straightedge addition X + Y both when
P_inf is a FINITE projective horizon point on y = 0 and when P_inf is an IDEAL point at infinity
(using Steiner's pure straightedge trapezoid-parallel construction, zero circles).
"""

from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
for candidate in (REPO_ROOT / "src", REPO_ROOT.parent / "model" / "src"):
    if str(candidate) not in sys.path:
        sys.path.insert(0, str(candidate))

from geometor.model import Model
from rich.console import Console

from geometor.staudt import (
    assert_straightedge_only,
    construct_harmonic_scale,
    construct_von_staudt_addition,
    point_from_abscissa,
    projective_abscissa,
)


def main() -> None:
    console = Console()
    console.rule("[bold cyan]02 · Von Staudt (1857) § 19 — Pure Straightedge Addition of Throws")

    # Part 1: Finite projective horizon point P_inf = (8, 0)
    m_fin = Model("addition_finite_horizon", auto_intersect=False, enable_logging=False)
    P0 = m_fin.given_point(0, 0, label="P0")
    P1 = m_fin.given_point(1, 0, label="P1")
    Pinf = m_fin.given_point(8, 0, label="Pinf")

    P2_add = construct_von_staudt_addition(m_fin, P0, P1, Pinf, P1, P1, label="P2")
    p3_raw = point_from_abscissa(P0, P1, Pinf, 3)
    P3 = m_fin.given_point(p3_raw.x, p3_raw.y, label="P3")
    P5 = construct_von_staudt_addition(m_fin, P0, P1, Pinf, P2_add, P3, label="P5")
    assert_straightedge_only(m_fin)

    console.print("[bold]A. Finite Projective Horizon P_inf = (8, 0)[/bold]")
    console.print(
        f"  P1 + P1 -> {P2_add}  (abscissa = {projective_abscissa(P0, P1, Pinf, P2_add)})"
    )
    console.print(
        f"  P2 + P3 -> {P5}  (abscissa = {projective_abscissa(P0, P1, Pinf, P5)})"
    )
    console.print(f"  Circles used: {len(m_fin.circles)}")

    # Harmonic integer ladder P_{-1} .. P_5
    m_scale = Model("harmonic_scale", auto_intersect=False, enable_logging=False)
    s0 = m_scale.given_point(0, 0, label="P0")
    s1 = m_scale.given_point(1, 0, label="P1")
    sinf = m_scale.given_point(8, 0, label="Pinf")
    scale = construct_harmonic_scale(m_scale, s0, s1, sinf, max_n=5)
    coords_str = ", ".join(
        f"k={k}: ({pt.x}, {pt.y})" for k, pt in sorted(scale.items())
    )
    console.print(f"  Harmonic scale P_k    : {coords_str}")

    # Part 2: Ideal horizon point P_inf = None (affine parallel straightedge specialization)
    m_inf = Model("addition_ideal_horizon", auto_intersect=False, enable_logging=False)
    A0 = m_inf.given_point(0, 0, label="P0")
    A1 = m_inf.given_point(1, 0, label="P1")
    A2 = construct_von_staudt_addition(m_inf, A0, A1, None, A1, A1, label="P2")
    A3 = m_inf.given_point(3, 0, label="P3")
    A5 = construct_von_staudt_addition(m_inf, A0, A1, None, A2, A3, label="P5")
    assert_straightedge_only(m_inf)

    console.print("[bold]B. Ideal Horizon Point at Infinity (P_inf = None, Steiner Straightedge Parallel)[/bold]")
    console.print(
        f"  P1 + P1 -> {A2}  (abscissa = {projective_abscissa(A0, A1, None, A2)})"
    )
    console.print(
        f"  P2 + P3 -> {A5}  (abscissa = {projective_abscissa(A0, A1, None, A5)})"
    )
    console.print(f"  Circles used: {len(m_inf.circles)}")


if __name__ == "__main__":
    main()
