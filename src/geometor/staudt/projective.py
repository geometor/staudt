"""Exact projective coordinates (Abscissen), linear betweenness, cyclic pair separation,
and straightedge-purity verification for von Staudt (1847/1857) and Pasch (1882).
"""

from __future__ import annotations

import sympy as sp
import sympy.geometry as spg
from geometor.model import (
    Model,
    ProofAssertionError,
    clean_expr,
    cross_ratio,
    exact_sign,
    zero_test,
)

__all__ = [
    "assert_straightedge_only",
    "is_between",
    "is_collinear",
    "pair_separates",
    "point_from_abscissa",
    "projective_abscissa",
]


def assert_straightedge_only(model: Model) -> None:
    """Assert that ``model`` contains zero compass circles (:class:`sympy.geometry.Circle`).

    Von Staudt's *Geometrie der Lage* (1847) and *Rechnung mit Würfen* (1857) require that
    every projective construction proceed strictly by unmarked straightedge incidence
    without metric compass transfers or circle intersections.

    Raises:
        ProofAssertionError: If any :class:`sympy.geometry.Circle` exists in ``model``.
    """
    circles = [el for el in model if isinstance(el, spg.Circle)]
    if circles:
        ids = [model[c].ID or str(c) for c in circles]
        raise ProofAssertionError(
            f"Straightedge-only invariant violated: model contains {len(circles)} circle(s): {ids}"
        )


def is_collinear(A: spg.Point, B: spg.Point, C: spg.Point) -> bool:
    """Return ``True`` iff points ``A``, ``B``, ``C`` are collinear in exact SymPy algebra."""
    det2 = (B.x - A.x) * (C.y - A.y) - (B.y - A.y) * (C.x - A.x)
    return zero_test(det2)


def is_between(A: spg.Point, B: spg.Point, C: spg.Point) -> bool:
    """Return ``True`` iff ``C`` lies strictly between ``A`` and ``B`` (Pasch § 1 Grundsatz V–VIII).

    Verifies exact collinearity together with positive inner product of directed segments
    :math:`\\overrightarrow{AC} \\cdot \\overrightarrow{CB} > 0`.
    """
    if not is_collinear(A, B, C):
        return False
    dot = (C.x - A.x) * (B.x - C.x) + (C.y - A.y) * (B.y - C.y)
    return exact_sign(dot) > 0


def pair_separates(
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
    D: spg.Point,
) -> bool:
    """Return ``True`` iff collinear point-pair ``{A, B}`` projectively separates ``{C, D}``.

    In Pasch (*Vorlesungen* § 1 Lehrsätze 19–23 & § 11) and Vailati (1895), four distinct
    collinear points exhibit cyclic pair separation ``AB // CD`` iff the projective
    cross-ratio :math:`(A, B; C, D)` is strictly negative. Every harmonic range satisfies
    :math:`(A, B; C, D) = -1 < 0` and therefore separates conjugate pairs.
    """
    pts = (A, B, C, D)
    for i in range(4):
        for j in range(i + 1, 4):
            if zero_test(pts[i].x - pts[j].x) and zero_test(pts[i].y - pts[j].y):
                return False
    try:
        cr = cross_ratio(A, B, C, D)
    except ValueError:
        return False
    return exact_sign(cr) < 0


def projective_abscissa(
    P0: spg.Point,
    P1: spg.Point,
    Pinf: spg.Point | None,
    X: spg.Point,
) -> sp.Expr:
    """Compute von Staudt's exact projective abscissa (*Beiträge* § 29, art. 404) of ``X``.

    Relative to three distinct collinear reference points :math:`(P_0, P_1, P_\\infty)`:

    * When ``Pinf`` is a **finite projective horizon point** on line :math:`[P_0 P_1]`,
      returns the exact cross-ratio :math:`(P_\\infty, P_0; P_1, X)`, mapping
      :math:`P_0 \\mapsto 0`, :math:`P_1 \\mapsto 1`, and :math:`P_\\infty \\mapsto \\infty`.
    * When ``Pinf is None`` (**ideal point at infinity** along :math:`[P_0 P_1]`),
      returns the exact affine ratio :math:`\\frac{(X - P_0) \\cdot d}{d \\cdot d}` with
      :math:`d = P_1 - P_0`.

    Raises:
        ValueError: If reference points coincide, ``X`` is not collinear with ``[P0 P1]``,
            or ``X`` coincides with ``Pinf``.
    """
    dx, dy = P1.x - P0.x, P1.y - P0.y
    d2 = dx**2 + dy**2
    if zero_test(d2):
        raise ValueError("Reference points P0 and P1 must be distinct.")
    if not is_collinear(P0, P1, X):
        raise ValueError("Target point X is not collinear with [P0 P1].")

    if Pinf is None:
        num = (X.x - P0.x) * dx + (X.y - P0.y) * dy
        return clean_expr(num / d2)

    if not is_collinear(P0, P1, Pinf):
        raise ValueError("Finite horizon point Pinf must be collinear with [P0 P1].")
    if (zero_test(Pinf.x - P0.x) and zero_test(Pinf.y - P0.y)) or (
        zero_test(Pinf.x - P1.x) and zero_test(Pinf.y - P1.y)
    ):
        raise ValueError("Reference triad (P0, P1, Pinf) must consist of three distinct points.")
    if zero_test(X.x - Pinf.x) and zero_test(X.y - Pinf.y):
        raise ValueError("Point X coincides with projective horizon Pinf (infinite abscissa).")
    if zero_test(X.x - P0.x) and zero_test(X.y - P0.y):
        return sp.Integer(0)

    return cross_ratio(Pinf, P0, P1, X)


def point_from_abscissa(
    P0: spg.Point,
    P1: spg.Point,
    Pinf: spg.Point | None,
    coord: sp.Expr | int,
) -> spg.Point:
    """Return the exact collinear :class:`sympy.geometry.Point` whose projective abscissa is ``coord``.

    Used strictly for setting up test inputs and checking closed-form algebraic identities;
    straightedge constructions in :mod:`geometor.staudt.quadrangle` and
    :mod:`geometor.staudt.throws` never invoke coordinate inversion.
    """
    k = sp.sympify(coord)
    if isinstance(k, sp.Float):
        raise TypeError("point_from_abscissa forbids sp.Float; pass exact Integer/Rational/Expr.")

    dx, dy = P1.x - P0.x, P1.y - P0.y
    d2 = dx**2 + dy**2
    if zero_test(d2):
        raise ValueError("Reference points P0 and P1 must be distinct.")

    if Pinf is None:
        return spg.Point(clean_expr(P0.x + k * dx), clean_expr(P0.y + k * dy))

    if not is_collinear(P0, P1, Pinf):
        raise ValueError("Finite horizon point Pinf must be collinear with [P0 P1].")
    t_inf = clean_expr(((Pinf.x - P0.x) * dx + (Pinf.y - P0.y) * dy) / d2)
    denom = clean_expr(k + t_inf - sp.Integer(1))
    if zero_test(denom):
        raise ValueError(f"Coordinate {k} maps to Euclidean infinity on this affine chart.")
    t = clean_expr((k * t_inf) / denom)
    return spg.Point(clean_expr(P0.x + t * dx), clean_expr(P0.y + t * dy))
