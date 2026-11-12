#!/usr/bin/env python3
"""Demo 04 — Moritz Pasch's Planar Separation Axiom (1882) & Euclid's Order Gaps (I.16, I.21).

Corresponds to Moritz Pasch, *Vorlesungen über neuere Geometrie* (Leipzig: B. G. Teubner, 1882),
§ 2 (*IV. Grundsatz* p. 21 & *10. Lehrsatz* p. 25) and § 12 (pp. 98–100).
Audits planar line–triangle separation via exact signed orientations and demonstrates how
Pasch's Axiom closes the unstated diagrammatic order steps in Euclid's *Elements* I.16 and I.21.
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
    demonstrate_euclid_i16_pasch_gap,
    demonstrate_euclid_i21_pasch_gap,
    demonstrate_pasch_axiom,
)


def main() -> None:
    console = Console()
    console.rule("[bold cyan]04 · Moritz Pasch (1882) § 2 — Planar Separation Axiom & Euclid I.16 / I.21")

    model = Model("demo_pasch", auto_intersect=False, enable_logging=False)
    A = model.given_point(0, 0, label="A")
    B = model.given_point(8, 0, label="B")
    C = model.given_point(3, 6, label="C")
    P = model.given_point(0, 2, label="P")
    Q = model.given_point(8, 4, label="Q")

    audit = demonstrate_pasch_axiom(model, A, B, C, P, Q)
    console.print("[bold]A. Pasch § 2 IV. Grundsatz & 10. Lehrsatz on △ABC:[/bold]")
    console.print(f"  Vertex half-plane signs : {audit.vertex_orientations}")
    console.print(f"  Entered/exited sides    : {audit.entered_sides}")
    console.print(f"  Satisfies Pasch's Axiom : {audit.satisfies_pasch}")

    _, i16 = demonstrate_euclid_i16_pasch_gap()
    console.print("[bold]B. Euclid Elements I.16 (Exterior Angle Theorem) Order Audit:[/bold]")
    console.print(
        f"  Betweenness B--C--D={i16['B_C_D_between']}, A--E--C={i16['A_E_C_between']}, B--E--F={i16['B_E_F_between']}"
    )
    console.print(
        f"  Ray CF cuts crossbar AD at K = {i16['crossbar_point_K']} (A--K--D = {i16['K_between_A_and_D']})"
    )

    _, i21 = demonstrate_euclid_i21_pasch_gap()
    console.print("[bold]C. Euclid Elements I.21 Deductive Proof via Pasch on Sub-Triangle △AMC:[/bold]")
    console.print(f"  Auxiliary cevian CM hit : M = {i21['M_on_AB']} on open side AB")
    console.print(
        f"  Pasch forced exit on AC : E = {i21['E_on_AC']} (A--E--C = {i21['E_between_A_and_C']}, B--D--E = {i21['D_between_B_and_E']})"
    )


if __name__ == "__main__":
    main()
