"""Moritz Pasch's Planar Separation Axiom (*Vorlesungen über neuere Geometrie*, 1882,
§ 2 *IV. Grundsatz* p. 21 & *10. Lehrsatz* p. 25) and symbolic order audits of
Euclid's *Elements* ``I.16`` and ``I.21``.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import sympy.geometry as spg
from geometor.model import (
    Model,
    ProofAssertionError,
    orientation,
    zero_test,
)

from geometor.staudt.projective import assert_straightedge_only, is_between

__all__ = [
    "PaschAuditResult",
    "demonstrate_euclid_i16_pasch_gap",
    "demonstrate_euclid_i21_pasch_gap",
    "demonstrate_pasch_axiom",
]


@dataclass(frozen=True)
class PaschAuditResult:
    """Exact symbolic audit of Pasch's planar transversal axiom on :math:`\\triangle ABC`."""

    triangle: tuple[spg.Point, spg.Point, spg.Point]
    transversal: spg.Line
    passes_through_vertex: bool
    vertex_hits: tuple[str, ...]
    entered_sides: tuple[tuple[str, spg.Point], ...]
    vertex_orientations: dict[str, int]
    satisfies_pasch: bool


def demonstrate_pasch_axiom(
    model: Model,
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
    line_P: spg.Point,
    line_Q: spg.Point,
) -> PaschAuditResult:
    """Audit and verify Pasch's *IV. Grundsatz* (1882, § 2, p. 21) & *10. Lehrsatz* (p. 25) on :math:`\\triangle ABC`.

    Given non-collinear vertices :math:`A, B, C` in the plane and a straight line
    :math:`\\ell = [P Q]`:

    * Computes exact signed half-plane orientations :math:`\\operatorname{orient}(P, Q, V) \\in \\{-1, 0, +1\\}`
      for each vertex :math:`V \\in \\{A, B, C\\}`.
    * When :math:`\\ell` passes through **no vertex** (:math:`\\operatorname{orient} \\neq 0` for all three):
      if :math:`\\ell` meets any open triangle side strictly between its endpoints
      (:func:`~geometor.staudt.projective.is_between`), it **must** exit strictly through
      **one and only one** of the remaining two sides (*10. Lehrsatz*, p. 25: it cannot meet
      all three open sides, nor meet only one).
    """
    if orientation(A, B, C) == 0:
        raise ValueError("Vertices A, B, C must form a non-degenerate triangle.")
    if zero_test(line_P.x - line_Q.x) and zero_test(line_P.y - line_Q.y):
        raise ValueError("Transversal endpoints line_P and line_Q must be distinct.")

    for pt, lbl in ((A, "A"), (B, "B"), (C, "C"), (line_P, "P_pasch"), (line_Q, "Q_pasch")):
        if pt not in model:
            model.given_point(pt.x, pt.y, label=lbl)

    side_ab = model.construct_line(A, B, by="Pasch.1882.s1.G1")
    side_bc = model.construct_line(B, C, by="Pasch.1882.s1.G1")
    side_ca = model.construct_line(C, A, by="Pasch.1882.s1.G1")
    transversal = model.construct_line(line_P, line_Q, by="Pasch.1882.s2.G4")

    id_a = model[A].ID or "A"
    id_b = model[B].ID or "B"
    id_c = model[C].ID or "C"

    orients = {
        id_a: orientation(line_P, line_Q, A),
        id_b: orientation(line_P, line_Q, B),
        id_c: orientation(line_P, line_Q, C),
    }
    vertex_hits = tuple(vid for vid, sgn in orients.items() if sgn == 0)
    passes_vertex = len(vertex_hits) > 0

    entered: list[tuple[str, spg.Point]] = []
    sides = (
        (f"{id_a}{id_b}", A, B, side_ab, orients[id_a], orients[id_b]),
        (f"{id_b}{id_c}", B, C, side_bc, orients[id_b], orients[id_c]),
        (f"{id_c}{id_a}", C, A, side_ca, orients[id_c], orients[id_a]),
    )
    for side_name, u_pt, w_pt, side_line, s_u, s_w in sides:
        if s_u * s_w == -1:
            hit = model.intersect(
                transversal,
                side_line,
                label=f"X_{side_name}",
                by="Pasch.1882.s2.G4",
            )
            if not is_between(u_pt, w_pt, hit):
                raise ProofAssertionError(
                    f"Opposite half-plane signs on side {side_name}, yet intersection {hit} "
                    f"failed linear betweenness."
                )
            model.assert_collinear(u_pt, hit, w_pt, by="Pasch.1882.s1")
            entered.append((side_name, hit))

    if not passes_vertex:
        satisfies = len(entered) in (0, 2)
        if not satisfies:
            raise ProofAssertionError(
                f"Pasch's Grundsatz IV / Lehrsatz 10 violated: vertex-free line cut {len(entered)} sides!"
            )
        if len(entered) == 2:
            model.conclude(
                entered[0][1],
                entered[1][1],
                kind="qed",
                by="Pasch.1882.s2.G4",
                label=(
                    f"Line enters side {entered[0][0]} and exits uniquely via side {entered[1][0]}"
                ),
            )
    else:
        satisfies = len(entered) <= 1

    assert_straightedge_only(model)
    return PaschAuditResult(
        triangle=(A, B, C),
        transversal=transversal,
        passes_through_vertex=passes_vertex,
        vertex_hits=vertex_hits,
        entered_sides=tuple(entered),
        vertex_orientations=orients,
        satisfies_pasch=satisfies,
    )


def demonstrate_euclid_i16_pasch_gap() -> tuple[Model, dict[str, Any]]:
    """Construct Euclid ``I.16`` (Exterior Angle Theorem) and verify the Pasch order step.

    In ``Elements`` Book I Prop. 16, Euclid bisects :math:`AC` at :math:`E`, prolongs median
    :math:`BE` to :math:`F` with :math:`BE = EF`, joins :math:`CF`, and infers from visual
    inspection of the diagram that :math:`F` lies inside exterior angle :math:`\\angle ACD`
    so that :math:`\\angle ACD > \\angle ECF` (Common Notion 5). On a sphere (elliptic plane)
    where straight lines are closed geodesics lacking open linear betweenness, :math:`F` can
    wrap past the antipode and violate ``I.16``.

    Using Pasch's linear betweenness (§ 1) and planar separation (*IV. Grundsatz*, § 2):
    since :math:`C` lies between :math:`B` and :math:`D` (:math:`B\\text{--}C\\text{--}D`),
    :math:`E` lies between :math:`A` and :math:`C` (:math:`A\\text{--}E\\text{--}C`), and
    :math:`E` lies between :math:`B` and :math:`F` (:math:`B\\text{--}E\\text{--}F`),
    ray :math:`CF` lies strictly inside :math:`\\angle ACD` (i.e., any segment joining
    :math:`A_1 \\in CA_{\\text{ext}}` or :math:`D \\in BC_{\\text{ext}}` to :math:`A` is cut
    internally by ray :math:`CF` via Pasch's Axiom on :math:`\\triangle ABD`).
    """
    model = Model("euclid_i16_pasch", auto_intersect=False, enable_logging=False)
    A = model.given_point(0, 4, label="A")
    B = model.given_point(0, 0, label="B")
    C = model.given_point(6, 0, label="C")
    D = model.given_point(10, 0, label="D")
    E = model.given_point(3, 2, label="E")
    F = model.given_point(6, 4, label="F")

    model.construct_line(A, B, by="Euclid.I.16")
    model.construct_line(B, D, by="Euclid.I.16")
    model.construct_line(A, C, by="Euclid.I.16")
    model.construct_line(B, F, by="Euclid.I.16")
    line_cf = model.construct_line(C, F, by="Euclid.I.16")
    line_ad = model.construct_line(A, D, guide=True, by="Pasch.1882.s2.G4")

    # Verify Euclid's tacit betweenness hypotheses
    bcd_between = is_between(B, D, C)
    aec_between = is_between(A, C, E)
    bef_between = is_between(B, F, E)
    if not (bcd_between and aec_between and bef_between):
        raise ProofAssertionError("Euclid I.16 betweenness setup failed.")

    # Apply Pasch's Axiom to triangle BCD? B, C, D are collinear!
    # Apply Pasch's Axiom to triangle ABD with transversal line CF? Wait: C lies on side BD!
    # Line CF enters triangle ABD strictly through side BD at C (since B--C--D) and misses A, B, D!
    # Can line CF exit side AB? [CF] meets [BF] at F with B--E--F, and [AC] meets [BF] at E with A--E--C.
    # Let's run demonstrate_pasch_axiom directly on triangle ABD with transversal [C, F]!
    audit_abd = demonstrate_pasch_axiom(model, A, B, D, C, F)
    crossbar_hit = model.intersect(line_cf, line_ad, label="K_bar", by="Pasch.1882.s2.G4")
    cf_cuts_ad_internally = is_between(A, D, crossbar_hit)
    if not cf_cuts_ad_internally:
        raise ProofAssertionError(
            "Ray CF failed to cut crossbar AD internally inside exterior angle <ACD."
        )

    return model, {
        "B_C_D_between": bcd_between,
        "A_E_C_between": aec_between,
        "B_E_F_between": bef_between,
        "pasch_audit_ABD": audit_abd,
        "crossbar_point_K": crossbar_hit,
        "K_between_A_and_D": cf_cuts_ad_internally,
    }


def demonstrate_euclid_i21_pasch_gap() -> tuple[Model, dict[str, Any]]:
    """Prove Euclid ``I.21``'s unstated ray-exit assumption directly from Pasch's *IV. Grundsatz*.

    In ``Elements`` Book I Prop. 21, given :math:`\\triangle ABC` and an interior point :math:`D`,
    Euclid writes *"let BD be drawn through to E [on AC]"* without proving that prolonging
    :math:`BD` must intersect open side :math:`AC` between :math:`A` and :math:`C`.

    **Deductive proof via Pasch's Axiom** (*Vorlesungen* § 2, p. 21):

    1. For interior point :math:`D` of :math:`\\triangle ABC`, line :math:`[CD]` meets open side
       :math:`AB` at :math:`M` strictly between :math:`A` and :math:`B`, with :math:`D` strictly
       between :math:`C` and :math:`M`.
    2. Apply :func:`demonstrate_pasch_axiom` to sub-triangle :math:`\\triangle AMC` and
       transversal :math:`\\ell = [BD]`:

       - :math:`\\ell` misses all three vertices :math:`A, M, C` (since :math:`A\\text{--}M\\text{--}B`).
       - :math:`\\ell` enters side :math:`CM` strictly at :math:`D`.
       - :math:`\\ell` cannot exit side :math:`AM`, because :math:`\\ell \\cap [AM] = B` lies
         outside segment :math:`AM`.
       - Therefore, by **Pasch's Grundsatz IV**, :math:`\\ell = [BD]` **must** exit side
         :math:`AC` at an interior point :math:`E` strictly between :math:`A` and :math:`C`!
    """
    model = Model("euclid_i21_pasch", auto_intersect=False, enable_logging=False)
    A = model.given_point(0, 0, label="A")
    B = model.given_point(8, 0, label="B")
    C = model.given_point(3, 6, label="C")
    D = model.given_point(3, 2, label="D")

    line_ab = model.construct_line(A, B, by="Euclid.I.21")
    model.construct_line(B, C, by="Euclid.I.21")
    line_ca = model.construct_line(C, A, by="Euclid.I.21")
    line_cd = model.construct_line(C, D, guide=True, by="Pasch.1882.s1.G1")

    M = model.intersect(line_cd, line_ab, label="M", guide=True, by="Pasch.1882.s2")
    if not is_between(A, B, M) or not is_between(C, M, D):
        raise ProofAssertionError("Interior point D setup for Euclid I.21 failed.")

    audit_amc = demonstrate_pasch_axiom(model, A, M, C, B, D)
    line_bd = model.construct_line(B, D, by="Euclid.I.21")
    E = model.intersect(line_bd, line_ca, label="E", by="Pasch.1882.s2.G4")
    e_between_ac = is_between(A, C, E)
    d_between_be = is_between(B, E, D)
    if not (e_between_ac and d_between_be):
        raise ProofAssertionError("Pasch proof of Euclid I.21 crossbar exit E on AC failed.")

    return model, {
        "M_on_AB": M,
        "E_on_AC": E,
        "pasch_audit_AMC": audit_amc,
        "E_between_A_and_C": e_between_ac,
        "D_between_B_and_E": d_between_be,
    }
