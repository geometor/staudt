"""Pure straightedge complete-quadrangle construction of the fourth harmonic point
and Desarguesian uniqueness verification (von Staudt, *Geometrie der Lage*, 1847, §§ 7–8).
"""

from __future__ import annotations

from typing import Any

import sympy as sp
import sympy.geometry as spg
from geometor.model import (
    Model,
    ProofAssertionError,
    clean_expr,
    cross_ratio,
    is_harmonic,
    proposition,
    zero_test,
)

from geometor.staudt.projective import (
    assert_straightedge_only,
    is_collinear,
    pair_separates,
)

__all__ = [
    "construct_harmonic_fourth_straightedge",
    "prove_symbolic_quadrangle_uniqueness",
    "verify_quadrangle_independence",
]


def _default_aux_points(
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
) -> tuple[tuple[sp.Expr, sp.Expr], tuple[sp.Expr, sp.Expr]]:
    """Produce deterministic exact rational/integer coordinates for two off-line auxiliary points."""
    dx, dy = B.x - A.x, B.y - A.y
    nx, ny = -dy, dx
    p_coords = (clean_expr(C.x + 2 * nx), clean_expr(C.y + 2 * ny))
    q_coords = (clean_expr(C.x + nx), clean_expr(C.y + ny))
    return p_coords, q_coords


@proposition(
    "Staudt.1847.art93",
    kind="problem",
    title="Pure straightedge construction of the fourth harmonic point via a complete quadrangle",
)
def construct_harmonic_fourth_straightedge(
    model: Model,
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
    aux_P: spg.Point | None = None,
    aux_Q: spg.Point | None = None,
    *,
    label: str = "D",
) -> spg.Point:
    """Construct the fourth harmonic point ``D`` to ``(A, B; C, D) = -1`` using **only a straightedge**.

    Implements Karl Georg Christian von Staudt's pure-incidence construction (*Geometrie der
    Lage*, 1847, § 8, arts. 93–96):

    1. Join carrier line :math:`\\ell = [AB]` containing collinear points :math:`A, B, C`.
    2. From auxiliary vertex :math:`E = P_{\\text{aux}} \\notin \\ell`, draw lines
       :math:`[AE]`, :math:`[BE]`, and first diagonal :math:`[CE]`.
    3. Select second diagonal vertex :math:`G \\in [CE] \\setminus \\{C, E\\}` (either ``aux_Q``
       directly if incident to :math:`[CE]`, or the straightedge intersection of :math:`[CE]`
       with :math:`[A, Q_{\\text{aux}}]`).
    4. Intersect opposite quadrangle sides :math:`F = [AE] \\cap [BG]` and
       :math:`H = [AG] \\cap [BE]`.
    5. Draw the second diagonal :math:`[FH]` meeting :math:`\\ell` in the fourth harmonic
       conjugate :math:`D`, satisfying :math:`(A, B; C, D) = -1` with **zero circles**.

    Args:
        model: Target :class:`~geometor.model.Model` (recommended ``auto_intersect=False``).
        A: First fundamental point of the harmonic pair ``{A, B}``.
        B: Second fundamental point of the harmonic pair ``{A, B}``.
        C: Given third collinear point (distinct from ``A`` and ``B``).
        aux_P: Optional off-line auxiliary vertex ``E``.
        aux_Q: Optional second auxiliary point determining ``G`` on ``[CE]``.
        label: Point identifier for the constructed harmonic conjugate ``D``.

    Returns:
        Exact :class:`sympy.geometry.Point` ``D`` registered in ``model``.
    """
    if not is_collinear(A, B, C):
        raise ValueError("Points A, B, C must be collinear.")
    for p, q, names in ((A, B, "A, B"), (A, C, "A, C"), (B, C, "B, C")):
        if zero_test(p.x - q.x) and zero_test(p.y - q.y):
            raise ValueError(f"Points {names} must be distinct for a non-degenerate harmonic fourth.")

    base_line = model.construct_line(A, B, by="Staudt.1847.s1")
    model.assert_collinear(A, B, C, by="given")

    if aux_P is None or aux_Q is None:
        def_p, def_q = _default_aux_points(A, B, C)
        if aux_P is None:
            aux_P = model.set_point(def_p[0], def_p[1], label="E_aux", guide=True, by="aux")
        if aux_Q is None:
            aux_Q = model.set_point(def_q[0], def_q[1], label="G_aux", guide=True, by="aux")

    if is_collinear(A, B, aux_P):
        raise ValueError("Auxiliary point aux_P must lie outside carrier line [AB].")
    if is_collinear(A, B, aux_Q):
        raise ValueError("Auxiliary point aux_Q must lie outside carrier line [AB].")
    if zero_test(aux_P.x - aux_Q.x) and zero_test(aux_P.y - aux_Q.y):
        raise ValueError("Auxiliary points aux_P and aux_Q must be distinct.")

    line_ae = model.construct_line(A, aux_P, guide=True, by="Staudt.1847.art93")
    line_be = model.construct_line(B, aux_P, guide=True, by="Staudt.1847.art93")
    diag_ce = model.construct_line(C, aux_P, guide=True, by="Staudt.1847.art93")

    if is_collinear(C, aux_P, aux_Q):
        G = aux_Q
        line_ag = model.construct_line(A, G, guide=True, by="Staudt.1847.art93")
        line_bg = model.construct_line(B, G, guide=True, by="Staudt.1847.art93")
    elif not is_collinear(A, aux_P, aux_Q):
        line_ag = model.construct_line(A, aux_Q, guide=True, by="Staudt.1847.art93")
        G = model.intersect(diag_ce, line_ag, label="G_q", guide=True, by="Staudt.1847.art93")
        line_bg = model.construct_line(B, G, guide=True, by="Staudt.1847.art93")
    else:
        line_bg = model.construct_line(B, aux_Q, guide=True, by="Staudt.1847.art93")
        G = model.intersect(diag_ce, line_bg, label="G_q", guide=True, by="Staudt.1847.art93")
        line_ag = model.construct_line(A, G, guide=True, by="Staudt.1847.art93")

    F = model.intersect(line_ae, line_bg, label="F_q", guide=True, by="Staudt.1847.art79")
    H = model.intersect(line_ag, line_be, label="H_q", guide=True, by="Staudt.1847.art79")

    diag_fh = model.construct_line(F, H, guide=True, by="Staudt.1847.art93")
    D = model.intersect(diag_fh, base_line, label=label, by="Staudt.1847.art93")

    assert_straightedge_only(model)
    model.assert_collinear(A, B, C, D, by="Staudt.1847.art93")
    if not is_harmonic(A, B, C, D):
        cr = cross_ratio(A, B, C, D)
        raise ProofAssertionError(
            f"Expected exact harmonic cross-ratio (A, B; C, D) == -1, got {cr}"
        )
    if not pair_separates(A, B, C, D):
        raise ProofAssertionError("Harmonic conjugate D failed projective pair separation AB // CD.")

    model.conclude(
        D,
        kind="qef",
        by="Staudt.1847.art93",
        label="Fourth harmonic point D constructed solely by straightedge incidence",
    )
    return D


def verify_quadrangle_independence(
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
    quad1: tuple[spg.Point, spg.Point],
    quad2: tuple[spg.Point, spg.Point],
) -> dict[str, Any]:
    """Verify in SymPy that two completely distinct auxiliary quadrangles construct the identical point ``D``.

    In *Geometrie der Lage* (§ 7 arts. 87–92 & § 8 art. 93), von Staudt proves without any
    appeal to metric cross-ratios that two complete quadrangles sharing ``A``, ``B``, and ``C``
    have perspective vertex triangles by Desargues's Theorem, forcing their sixth sides to
    meet ``[AB]`` in the selfsame fourth harmonic point :math:`D_1 = D_2`.
    """
    m1 = Model("quadrangle_1", auto_intersect=False, enable_logging=False)
    a1 = m1.given_point(A.x, A.y, label="A")
    b1 = m1.given_point(B.x, B.y, label="B")
    c1 = m1.given_point(C.x, C.y, label="C")
    p1 = m1.given_point(quad1[0].x, quad1[0].y, label="P1")
    q1 = m1.given_point(quad1[1].x, quad1[1].y, label="Q1")
    d1 = construct_harmonic_fourth_straightedge(m1, a1, b1, c1, p1, q1, label="D1")

    m2 = Model("quadrangle_2", auto_intersect=False, enable_logging=False)
    a2 = m2.given_point(A.x, A.y, label="A")
    b2 = m2.given_point(B.x, B.y, label="B")
    c2 = m2.given_point(C.x, C.y, label="C")
    p2 = m2.given_point(quad2[0].x, quad2[0].y, label="P2")
    q2 = m2.given_point(quad2[1].x, quad2[1].y, label="Q2")
    d2 = construct_harmonic_fourth_straightedge(m2, a2, b2, c2, p2, q2, label="D2")

    assert_straightedge_only(m1)
    assert_straightedge_only(m2)

    same_point = zero_test(d1.x - d2.x) and zero_test(d1.y - d2.y)
    if not same_point:
        raise ProofAssertionError(
            f"Quadrangle independence failed: D1={d1} != D2={d2}"
        )

    cr = cross_ratio(a1, b1, c1, d1)
    return {
        "D1": d1,
        "D2": d2,
        "identical": True,
        "cross_ratio": cr,
        "circles_used": len(m1.circles) + len(m2.circles),
    }


def prove_symbolic_quadrangle_uniqueness() -> dict[str, sp.Expr]:
    """Prove over free symbolic coordinates in ``SymPy`` that ``D`` is independent of the quadrangle.

    Places :math:`A = (0, 0)`, :math:`B = (1, 0)`, :math:`C = (c, 0)` and constructs the
    complete quadrangle from indeterminate parameters :math:`E = (u, v)` and
    :math:`G = ((1 - t) c + t u, t v)` on :math:`[CE]`. Simplifies the algebraic intersection
    :math:`D = [FH] \\cap [AB]` and verifies :math:`D_x = \\frac{c}{2c - 1}` with zero free
    dependence on :math:`(u, v, t)` and exact cross-ratio :math:`(A, B; C, D) = -1`.
    """
    c, u, v, t = sp.symbols("c u v t", real=True)
    e_x, e_y = u, v
    g_x = (1 - t) * c + t * u
    g_y = t * v

    # F = [AE] ∩ [BG]: A=(0,0), B=(1,0)
    # Parametrize F = s * E = (s*u, s*v) on [AE]; collinearity with B=(1,0) and G=(g_x, g_y):
    # (s*u - 1) * g_y - (s*v) * (g_x - 1) = 0
    s_f = sp.simplify(g_y / (u * g_y - v * (g_x - 1)))
    f_x, f_y = sp.simplify(s_f * e_x), sp.simplify(s_f * e_y)

    # H = [AG] ∩ [BE]: H = r * G = (r*g_x, r*g_y); collinearity with B=(1,0) and E=(u,v):
    # (r*g_x - 1) * v - (r*g_y) * (u - 1) = 0
    r_h = sp.simplify(v / (g_x * v - g_y * (u - 1)))
    h_x, h_y = sp.simplify(r_h * g_x), sp.simplify(r_h * g_y)

    # Intersect [FH] with y = 0: x_D = (f_x * h_y - h_x * f_y) / (h_y - f_y)
    d_x = sp.simplify((f_x * h_y - h_x * f_y) / (h_y - f_y))
    expected_dx = sp.simplify(c / (2 * c - 1))
    if sp.simplify(d_x - expected_dx) != 0:
        raise ProofAssertionError(f"Symbolic uniqueness check failed: got {d_x} != {expected_dx}")
    if d_x.free_symbols - {c}:
        raise ProofAssertionError(
            f"Constructed harmonic fourth unexpectedly depends on auxiliary symbols: {d_x.free_symbols - {c}}"
        )

    cr = sp.simplify(((c - 0) * (d_x - 1)) / ((c - 1) * (d_x - 0)))
    if sp.simplify(cr + 1) != 0:
        raise ProofAssertionError(f"Symbolic cross-ratio check failed: {cr} != -1")

    return {
        "D_x": d_x,
        "D_y": sp.Integer(0),
        "cross_ratio": cr,
    }
