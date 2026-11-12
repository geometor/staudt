"""Von Staudt's *Rechnung mit Würfen* (*Algebra of Throws*, *Beiträge zur Geometrie der Lage*,
Heft 2, 1857, §§ 19, 20, 29): pure straightedge addition, multiplication, harmonic scales,
and golden-section throw arithmetic over Q(phi) without compass or ruler scale.
"""

from __future__ import annotations

from typing import Any

import sympy as sp
import sympy.geometry as spg
from geometor.model import (
    Model,
    ProofAssertionError,
    clean_expr,
    intersect_2d,
    proposition,
    zero_test,
)

from geometor.staudt.projective import (
    assert_straightedge_only,
    is_collinear,
    point_from_abscissa,
    projective_abscissa,
)
from geometor.staudt.quadrangle import construct_harmonic_fourth_straightedge

__all__ = [
    "construct_harmonic_scale",
    "construct_parallel_straightedge",
    "construct_von_staudt_addition",
    "construct_von_staudt_multiplication",
    "verify_golden_throw_identity",
]


def _points_equal(P: spg.Point, Q: spg.Point) -> bool:
    return zero_test(P.x - Q.x) and zero_test(P.y - Q.y)


def _steiner_stage2_points(
    A: spg.Point,
    B: spg.Point,
    pt_m: spg.Point,
    rail_line: spg.Line,
    R: spg.Point,
) -> bool:
    """Return True iff Stage 2 of Steiner's straightedge parallel avoids accidental parallelisms."""
    q_hits = intersect_2d(spg.Line(A, R), rail_line)
    if not q_hits or q_hits[0] == pt_m or q_hits[0] == B:
        return False
    pt_q = q_hits[0]
    k_hits = intersect_2d(spg.Line(B, R), spg.Line(pt_q, pt_m))
    if not k_hits or k_hits[0] == A:
        return False
    l_hits = intersect_2d(spg.Line(A, k_hits[0]), spg.Line(pt_q, B))
    return bool(l_hits and l_hits[0] != R)


def construct_parallel_straightedge(
    model: Model,
    A: spg.Point,
    B: spg.Point,
    rail_U0: spg.Point,
    rail_U1: spg.Point,
    R: spg.Point,
    *,
    guide: bool = True,
) -> spg.Line:
    """Construct the line through ``R`` parallel to ``[AB]`` using **only an unmarked straightedge**.

    Given carrier line :math:`\\ell = [AB]` and a single auxiliary parallel rail
    :math:`m = [U_0 U_1] \\parallel \\ell` (representing the shared ideal point :math:`P_\\infty`
    at infinity, with :math:`|AB| \\neq |U_0 U_1|`), executes the two-stage Steiner–Poncelet
    pure-incidence construction:

    1. **Affine midpoint via trapezoid quadrangle**: :math:`O = [A U_0] \\cap [B U_1]` and
       :math:`K_0 = [A U_1] \\cap [B U_0]`; line :math:`[O K_0]` meets :math:`\\ell` in the
       exact harmonic conjugate :math:`M` of :math:`P_\\infty`, i.e., the midpoint of :math:`AB`.
    2. **Parallel through R via Steiner harmonic cevian**: join :math:`[AR]` meeting :math:`m`
       at :math:`Q` (if :math:`R \\in m`, :math:`m` itself is already the required parallel);
       intersect :math:`K = [BR] \\cap [QM]` and :math:`L = [AK] \\cap [QB]`. Then
       :math:`[RL] \\parallel [AB]` with **zero circles** and **zero coordinate helpers**.
    """
    for pt, lbl in (
        (A, "A_par"),
        (B, "B_par"),
        (rail_U0, "U0_rail"),
        (rail_U1, "U1_rail"),
        (R, "R_par"),
    ):
        if pt not in model:
            model.set_point(pt.x, pt.y, label=lbl, guide=True, by="aux")

    base_line = model.construct_line(A, B, guide=guide, by="Staudt.1847.s1")
    rail_line = model.construct_line(rail_U0, rail_U1, guide=True, by="given")

    if is_collinear(rail_U0, rail_U1, R):
        return rail_line
    if is_collinear(A, B, R):
        return base_line

    u0, u1 = rail_U0, rail_U1
    if not intersect_2d(spg.Line(A, u0), spg.Line(B, u1)) or not intersect_2d(
        spg.Line(A, u1), spg.Line(B, u0)
    ):
        u0, u1 = u1, u0
    if not intersect_2d(spg.Line(A, u0), spg.Line(B, u1)) or not intersect_2d(
        spg.Line(A, u1), spg.Line(B, u0)
    ):
        raise ValueError(
            "Parallel rail segment [U0 U1] has equal span to [A B]; choose unequal span."
        )

    l_au0 = model.construct_line(A, u0, guide=True, by="Steiner.1833")
    l_bu1 = model.construct_line(B, u1, guide=True, by="Steiner.1833")
    pt_o = model.intersect(l_au0, l_bu1, guide=True, by="Steiner.1833")
    l_au1 = model.construct_line(A, u1, guide=True, by="Steiner.1833")
    l_bu0 = model.construct_line(B, u0, guide=True, by="Steiner.1833")
    pt_k0 = model.intersect(l_au1, l_bu0, guide=True, by="Steiner.1833")
    l_ok0 = model.construct_line(pt_o, pt_k0, guide=True, by="Steiner.1833")
    pt_m = model.intersect(l_ok0, base_line, guide=True, by="Steiner.1833")

    if _steiner_stage2_points(A, B, pt_m, rail_line, R):
        sA, sB, sM, aux_line = A, B, pt_m, rail_line
    else:
        # Midline locus (rail lies halfway between R and base_line, so QM // BR):
        # l_ok0 also bisects [u0, u1] on rail_line, where R cannot lie on the dual midline!
        pt_m_rail = model.intersect(l_ok0, rail_line, guide=True, by="Steiner.1833")
        sA, sB, sM, aux_line = u0, u1, pt_m_rail, base_line

    l_ar = model.construct_line(sA, R, guide=True, by="Steiner.1833")
    pt_q = model.intersect(l_ar, aux_line, guide=True, by="Steiner.1833")
    l_qm = model.construct_line(pt_q, sM, guide=True, by="Steiner.1833")
    l_br = model.construct_line(sB, R, guide=True, by="Steiner.1833")
    pt_k = model.intersect(l_br, l_qm, guide=True, by="Steiner.1833")
    l_ak = model.construct_line(sA, pt_k, guide=True, by="Steiner.1833")
    l_qb = model.construct_line(pt_q, sB, guide=True, by="Steiner.1833")
    pt_l = model.intersect(l_ak, l_qb, guide=True, by="Steiner.1833")

    par_line = model.construct_line(R, pt_l, guide=guide, by="Steiner.1833")
    assert_straightedge_only(model)
    return par_line


def _choose_addition_centers_finite(
    model: Model,
    P0: spg.Point,
    P1: spg.Point,
    Pinf: spg.Point,
    X: spg.Point,
    Y: spg.Point,
    aux_U: spg.Point | None,
    aux_V: spg.Point | None,
) -> tuple[spg.Point, spg.Point]:
    """Select exact rational centers ``(U, V)`` collinear with ``Pinf`` avoiding parallel accidents."""
    if aux_U is not None and aux_V is not None:
        if not is_collinear(Pinf, aux_U, aux_V):
            raise ValueError("Finite-horizon addition centers aux_U and aux_V must be collinear with Pinf.")
        return aux_U, aux_V

    dx, dy = P1.x - P0.x, P1.y - P0.y
    nx, ny = -dy, dx

    candidates = [
        (sp.Integer(1), sp.Integer(2), sp.Rational(1, 2)),
        (sp.Integer(0), sp.Integer(3), sp.Rational(1, 3)),
        (sp.Integer(2), sp.Integer(3), sp.Rational(2, 3)),
        (sp.Integer(-1), sp.Integer(2), sp.Rational(3, 5)),
    ]
    for alpha, beta, lam in candidates:
        ux = clean_expr(P0.x + alpha * dx + beta * nx)
        uy = clean_expr(P0.y + alpha * dy + beta * ny)
        u_pt = spg.Point(ux, uy)
        vx = clean_expr((1 - lam) * Pinf.x + lam * ux)
        vy = clean_expr((1 - lam) * Pinf.y + lam * uy)
        v_pt = spg.Point(vx, vy)
        r_hits = intersect_2d(spg.Line(u_pt, P0), spg.Line(v_pt, X))
        if not r_hits:
            continue
        axis = spg.Line(Pinf, r_hits[0])
        t_hits = intersect_2d(spg.Line(u_pt, Y), axis)
        if not t_hits:
            continue
        s_hits = intersect_2d(spg.Line(v_pt, t_hits[0]), spg.Line(P0, P1))
        if s_hits:
            u_reg = model.set_point(ux, uy, label="U_add", guide=True, by="aux")
            v_reg = model.set_point(vx, vy, label="V_add", guide=True, by="aux")
            return u_reg, v_reg

    raise ProofAssertionError("Could not find finite perspective centers for addition.")


@proposition(
    "Staudt.1857.art256",
    kind="problem",
    title="Von Staudt's pure straightedge addition of throws (Summen von Wuerfen)",
)
def construct_von_staudt_addition(
    model: Model,
    P0: spg.Point,
    P1: spg.Point,
    Pinf: spg.Point | None,
    X: spg.Point,
    Y: spg.Point,
    *,
    aux_U: spg.Point | None = None,
    aux_V: spg.Point | None = None,
    parallel_rail: tuple[spg.Point, spg.Point] | None = None,
    label: str = "S",
) -> spg.Point:
    """Construct the projective sum ``S = X + Y`` on ``(P0, P1, Pinf)`` using **only a straightedge**.

    Implements Karl Georg Christian von Staudt's *Summen von Würfen* (*Beiträge zur Geometrie
    der Lage*, Heft 2, 1857, § 19, arts. 256–267): the parabolic projectivity fixing
    :math:`P_\\infty` with double contact (conjugate to :math:`P_0` in the involution
    :math:`P_\\infty P_\\infty \\cdot X Y`) realized as a composition of two perspectivities
    :math:`\\ell \\xrightarrow{U} a \\xrightarrow{V} \\ell` whose center join :math:`[UV]`
    and perspective axis :math:`a` both pass through :math:`P_\\infty`:

    1. Draw horizon carrier :math:`m` through :math:`P_\\infty` containing distinct off-line
       centers :math:`U` and :math:`V` (when ``Pinf is None``, :math:`m = [U V]` is a parallel
       rail to :math:`\\ell = [P_0 P_1]`).
    2. Intersect :math:`R = [U P_0] \\cap [V X]` so that :math:`P_0 \\mapsto X`.
    3. Construct perspective axis :math:`a` joining :math:`P_\\infty` and :math:`R` (when
       ``Pinf is None``, construct :math:`a \\parallel \\ell` through :math:`R` purely by
       straightedge via :func:`construct_parallel_straightedge`).
    4. Intersect :math:`T = [U Y] \\cap a` and project :math:`S = [V T] \\cap \\ell`.

    Verifies in SymPy that ``projective_abscissa(P0, P1, Pinf, S)`` equals
    ``projective_abscissa(P0, P1, Pinf, X) + projective_abscissa(P0, P1, Pinf, Y)`` and
    that **zero circles** exist in ``model``.
    """
    x_coord = projective_abscissa(P0, P1, Pinf, X)
    y_coord = projective_abscissa(P0, P1, Pinf, Y)
    base_line = model.construct_line(P0, P1, by="Staudt.1857.art256")

    # Handle zero identity X == P0 cleanly (swap to Y + P0 if Y != P0 so construction runs!)
    if _points_equal(X, P0) and _points_equal(Y, P0):
        assert_straightedge_only(model)
        model.conclude(P0, kind="qef", by="Staudt.1857.art256", label="0 + 0 = 0")
        return P0
    if _points_equal(X, P0):
        X, Y = Y, X

    if Pinf is not None:
        U, V = _choose_addition_centers_finite(model, P0, P1, Pinf, X, Y, aux_U, aux_V)
        model.construct_line(Pinf, U, guide=True, by="Staudt.1857.art256")
        l_up0 = model.construct_line(U, P0, guide=True, by="Staudt.1857.art256")
        l_vx = model.construct_line(V, X, guide=True, by="Staudt.1857.art256")
        R = model.intersect(l_up0, l_vx, label="R_add", guide=True, by="Staudt.1857.art256")
        axis_a = model.construct_line(Pinf, R, guide=True, by="Staudt.1857.art256")
    else:
        dx, dy = P1.x - P0.x, P1.y - P0.y
        nx, ny = -dy, dx
        if parallel_rail is not None:
            U, V = parallel_rail
            if not intersect_2d(spg.Line(U, P0), spg.Line(V, X)):
                U, V = V, U
        elif aux_U is not None and aux_V is not None:
            U, V = aux_U, aux_V
            if not intersect_2d(spg.Line(U, P0), spg.Line(V, X)):
                U, V = V, U
        else:
            u_pt = spg.Point(clean_expr(P0.x + 2 * nx), clean_expr(P0.y + 2 * ny))
            span_k = sp.Integer(2)
            for cand_k in (sp.Integer(2), sp.Integer(3), sp.Integer(5)):
                v_cand = spg.Point(
                    clean_expr(P0.x + cand_k * dx + 2 * nx),
                    clean_expr(P0.y + cand_k * dy + 2 * ny),
                )
                if intersect_2d(spg.Line(u_pt, P0), spg.Line(v_cand, X)):
                    span_k = cand_k
                    break
            U = model.set_point(u_pt.x, u_pt.y, label="U_add", guide=True, by="aux")
            V = model.set_point(
                clean_expr(P0.x + span_k * dx + 2 * nx),
                clean_expr(P0.y + span_k * dy + 2 * ny),
                label="V_add",
                guide=True,
                by="aux",
            )
        model.construct_line(U, V, guide=True, by="Staudt.1857.art256")
        l_up0 = model.construct_line(U, P0, guide=True, by="Staudt.1857.art256")
        l_vx = model.construct_line(V, X, guide=True, by="Staudt.1857.art256")
        R = model.intersect(l_up0, l_vx, label="R_add", guide=True, by="Staudt.1857.art256")
        axis_a = construct_parallel_straightedge(model, P0, P1, U, V, R, guide=True)

    l_uy = model.construct_line(U, Y, guide=True, by="Staudt.1857.art256")
    T = model.intersect(l_uy, axis_a, label="T_add", guide=True, by="Staudt.1857.art256")
    l_vt = model.construct_line(V, T, guide=True, by="Staudt.1857.art256")
    S = model.intersect(l_vt, base_line, label=label, by="Staudt.1857.art256")

    assert_straightedge_only(model)
    s_coord = projective_abscissa(P0, P1, Pinf, S)
    if not zero_test(s_coord - (x_coord + y_coord)):
        raise ProofAssertionError(
            f"Von Staudt addition mismatch: got abscissa {s_coord}, expected {x_coord + y_coord}"
        )

    model.conclude(
        S,
        kind="qef",
        by="Staudt.1857.art256",
        label=f"Projective sum {label} constructed by pure straightedge",
    )
    return S


def _choose_multiplication_centers(
    model: Model,
    P0: spg.Point,
    P1: spg.Point,
    Pinf: spg.Point | None,
    X: spg.Point,
    Y: spg.Point,
    aux_U: spg.Point | None,
    aux_V: spg.Point | None,
) -> tuple[spg.Point, spg.Point]:
    """Select exact centers ``(U, V)`` collinear with ``P0`` avoiding Euclidean parallel accidents."""
    if aux_U is not None and aux_V is not None:
        if not is_collinear(P0, aux_U, aux_V):
            raise ValueError("Multiplication centers aux_U and aux_V must be collinear with P0.")
        return aux_U, aux_V

    dx, dy = P1.x - P0.x, P1.y - P0.y
    nx, ny = -dy, dx

    candidates = [
        (sp.Integer(1), sp.Integer(2), sp.Integer(-1)),
        (sp.Integer(1), sp.Integer(3), sp.Rational(1, 2)),
        (sp.Integer(0), sp.Integer(2), sp.Rational(3, 5)),
        (sp.Integer(-1), sp.Integer(2), sp.Rational(2, 3)),
    ]
    for alpha, beta, lam in candidates:
        ux = clean_expr(P0.x + alpha * dx + beta * nx)
        uy = clean_expr(P0.y + alpha * dy + beta * ny)
        u_pt = spg.Point(ux, uy)
        vx = clean_expr(P0.x + lam * (ux - P0.x))
        vy = clean_expr(P0.y + lam * (uy - P0.y))
        v_pt = spg.Point(vx, vy)
        w_hits = intersect_2d(spg.Line(u_pt, P1), spg.Line(v_pt, X))
        if not w_hits:
            continue
        w_pt = w_hits[0]
        axis = (
            spg.Line(Pinf, w_pt)
            if Pinf is not None
            else spg.Line(w_pt, spg.Point(w_pt.x + dx, w_pt.y + dy))
        )
        z_hits = intersect_2d(spg.Line(u_pt, Y), axis)
        if not z_hits:
            continue
        p_hits = intersect_2d(spg.Line(v_pt, z_hits[0]), spg.Line(P0, P1))
        if p_hits:
            u_reg = model.set_point(ux, uy, label="U_mul", guide=True, by="aux")
            v_reg = model.set_point(vx, vy, label="V_mul", guide=True, by="aux")
            return u_reg, v_reg

    raise ProofAssertionError("Could not find finite perspective centers for multiplication.")


@proposition(
    "Staudt.1857.art268",
    kind="problem",
    title="Von Staudt's pure straightedge multiplication of throws (Produkte aus Wuerfen)",
)
def construct_von_staudt_multiplication(
    model: Model,
    P0: spg.Point,
    P1: spg.Point,
    Pinf: spg.Point | None,
    X: spg.Point,
    Y: spg.Point,
    *,
    aux_U: spg.Point | None = None,
    aux_V: spg.Point | None = None,
    parallel_rail: tuple[spg.Point, spg.Point] | None = None,
    label: str = "P",
) -> spg.Point:
    """Construct the projective product ``P = X * Y`` on ``(P0, P1, Pinf)`` using **only a straightedge**.

    Implements Karl Georg Christian von Staudt's *Produkte aus Würfen* (*Beiträge zur Geometrie
    der Lage*, Heft 2, 1857, § 20, arts. 268–275): the hyperbolic projectivity fixing both
    :math:`P_0` and :math:`P_\\infty` while mapping :math:`P_1 \\mapsto X`, realized by two
    perspectivities :math:`\\ell \\xrightarrow{U} a \\xrightarrow{V} \\ell` whose center line
    :math:`[UV]` passes through :math:`P_0` and whose axis :math:`a` passes through :math:`P_\\infty`:

    1. Choose distinct off-line centers :math:`U, V` collinear with :math:`P_0`.
    2. Intersect :math:`W = [U P_1] \\cap [V X]` so that :math:`P_1 \\mapsto X`.
    3. Draw axis :math:`a` through :math:`P_\\infty` and :math:`W` (or parallel to :math:`\\ell`
       via :func:`construct_parallel_straightedge` when ``Pinf is None``).
    4. Intersect :math:`Z = [U Y] \\cap a` and project :math:`P = [V Z] \\cap \\ell`.

    Verifies in SymPy that ``projective_abscissa(P0, P1, Pinf, P)`` equals
    ``projective_abscissa(P0, P1, Pinf, X) * projective_abscissa(P0, P1, Pinf, Y)`` and
    that **zero circles** exist in ``model``.
    """
    x_coord = projective_abscissa(P0, P1, Pinf, X)
    y_coord = projective_abscissa(P0, P1, Pinf, Y)
    base_line = model.construct_line(P0, P1, by="Staudt.1857.art268")

    # Multiplicative annihilator P0 and multiplicative unit P1
    if _points_equal(X, P0) or _points_equal(Y, P0):
        assert_straightedge_only(model)
        model.conclude(P0, kind="qef", by="Staudt.1857.art268", label="Zero throw product")
        return P0
    if _points_equal(X, P1) and _points_equal(Y, P1):
        assert_straightedge_only(model)
        model.conclude(P1, kind="qef", by="Staudt.1857.art268", label="1 * 1 = 1")
        return P1
    if _points_equal(X, P1):
        X, Y = Y, X

    U, V = _choose_multiplication_centers(model, P0, P1, Pinf, X, Y, aux_U, aux_V)
    model.construct_line(P0, U, guide=True, by="Staudt.1857.art268")

    l_up1 = model.construct_line(U, P1, guide=True, by="Staudt.1857.art268")
    l_vx = model.construct_line(V, X, guide=True, by="Staudt.1857.art268")
    W = model.intersect(l_up1, l_vx, label="W_mul", guide=True, by="Staudt.1857.art268")

    if Pinf is not None:
        axis_a = model.construct_line(Pinf, W, guide=True, by="Staudt.1857.art268")
    else:
        if parallel_rail is None:
            dx, dy = P1.x - P0.x, P1.y - P0.y
            nx, ny = -dy, dx
            r0 = model.set_point(
                clean_expr(P0.x - 3 * nx),
                clean_expr(P0.y - 3 * ny),
                label="R0_par",
                guide=True,
                by="aux",
            )
            r1 = model.set_point(
                clean_expr(P0.x + 2 * dx - 3 * nx),
                clean_expr(P0.y + 2 * dy - 3 * ny),
                label="R1_par",
                guide=True,
                by="aux",
            )
            parallel_rail = (r0, r1)
        axis_a = construct_parallel_straightedge(
            model, P0, P1, parallel_rail[0], parallel_rail[1], W, guide=True
        )

    l_uy = model.construct_line(U, Y, guide=True, by="Staudt.1857.art268")
    Z = model.intersect(l_uy, axis_a, label="Z_mul", guide=True, by="Staudt.1857.art268")
    l_vz = model.construct_line(V, Z, guide=True, by="Staudt.1857.art268")
    P = model.intersect(l_vz, base_line, label=label, by="Staudt.1857.art268")

    assert_straightedge_only(model)
    p_coord = projective_abscissa(P0, P1, Pinf, P)
    if not zero_test(p_coord - (x_coord * y_coord)):
        raise ProofAssertionError(
            f"Von Staudt multiplication mismatch: got abscissa {p_coord}, expected {x_coord * y_coord}"
        )

    model.conclude(
        P,
        kind="qef",
        by="Staudt.1857.art268",
        label=f"Projective product {label} constructed by pure straightedge",
    )
    return P


def construct_harmonic_scale(
    model: Model,
    P0: spg.Point,
    P1: spg.Point,
    Pinf: spg.Point,
    max_n: int = 5,
) -> dict[int, spg.Point]:
    """Construct the Möbius–von Staudt harmonic integer scale ``P_{-1}, P_0, P_1, ..., P_n`` by straightedge.

    In *Beiträge* § 19 art. 267, von Staudt observes that :math:`(P_{k-1}, P_{k+1}; P_k, P_\\infty) = -1`
    for every integer :math:`k`, so each successive integer mark :math:`P_{k+1}` is the fourth
    harmonic conjugate to :math:`(P_{k-1}, P_{k+1}; P_k, P_\\infty) = -1` — equivalently
    :math:`(P_k, P_\\infty; P_{k-1}, P_{k+1}) = -1`! Constructs ``P_{-1}`` and ``P_2 .. P_{max_n}``
    exclusively via :func:`construct_harmonic_fourth_straightedge`.
    """
    if max_n < 1:
        raise ValueError("max_n must be >= 1.")
    scale: dict[int, spg.Point] = {0: P0, 1: P1}
    scale[-1] = construct_harmonic_fourth_straightedge(
        model, P0, Pinf, P1, label="P_-1"
    )
    for k in range(1, max_n):
        p_next = construct_harmonic_fourth_straightedge(
            model,
            scale[k],
            Pinf,
            scale[k - 1],
            label=f"P_{k + 1}",
        )
        coord = projective_abscissa(P0, P1, Pinf, p_next)
        if not zero_test(coord - sp.Integer(k + 1)):
            raise ProofAssertionError(
                f"Harmonic scale step P_{k + 1} failed: got {coord}, expected {k + 1}"
            )
        scale[k + 1] = p_next

    assert_straightedge_only(model)
    return scale


def verify_golden_throw_identity(
    P0: spg.Point,
    P1: spg.Point,
    Pinf: spg.Point | None,
) -> dict[str, Any]:
    """Verify over :math:`\\mathbb{Q}(\\phi)` that von Staudt's straightedge product & sum satisfy :math:`P_\\phi \\cdot P_\\phi = P_\\phi + P_1`.

    With :math:`\\phi = \\frac{1 + \\sqrt{5}}{2}`, constructs both :math:`P_{\\phi^2} = P_\\phi \\cdot P_\\phi`
    and :math:`P_{\\phi + 1} = P_\\phi + P_1` purely by straightedge incidence on the projective
    line :math:`(P_0, P_1, P_\\infty)` and proves exact coincidence of the two constructed points,
    plus exact conjugate throw relations :math:`P_\\phi + P_{\\hat{\\phi}} = P_1` and
    :math:`P_\\phi \\cdot P_{\\hat{\\phi}} = P_{-1}` where :math:`\\hat{\\phi} = 1 - \\phi = -1/\\phi`.
    """
    phi = (sp.Integer(1) + sp.sqrt(5)) / sp.Integer(2)
    phi_conj = sp.Integer(1) - phi

    pt_phi_raw = point_from_abscissa(P0, P1, Pinf, phi)
    pt_conj_raw = point_from_abscissa(P0, P1, Pinf, phi_conj)

    model = Model("golden_throw_identity", auto_intersect=False, enable_logging=False)
    p0 = model.given_point(P0.x, P0.y, label="P0")
    p1 = model.given_point(P1.x, P1.y, label="P1")
    pinf = model.given_point(Pinf.x, Pinf.y, label="Pinf") if Pinf is not None else None
    p_phi = model.given_point(pt_phi_raw.x, pt_phi_raw.y, label="P_phi")
    p_conj = model.given_point(pt_conj_raw.x, pt_conj_raw.y, label="P_phibar")

    p_sq = construct_von_staudt_multiplication(
        model, p0, p1, pinf, p_phi, p_phi, label="P_phi_sq"
    )
    p_plus_1 = construct_von_staudt_addition(
        model, p0, p1, pinf, p_phi, p1, label="P_phi_plus_1"
    )
    p_trace = construct_von_staudt_addition(
        model, p0, p1, pinf, p_phi, p_conj, label="P_trace"
    )
    p_norm = construct_von_staudt_multiplication(
        model, p0, p1, pinf, p_phi, p_conj, label="P_norm"
    )

    assert_straightedge_only(model)

    if not _points_equal(p_sq, p_plus_1):
        raise ProofAssertionError(f"Golden throw identity failed: P_phi^2={p_sq} != P_phi+P1={p_plus_1}")
    if not _points_equal(p_trace, p1):
        raise ProofAssertionError(f"Golden trace throw failed: P_phi + P_phibar = {p_trace} != P1={p1}")

    norm_abscissa = projective_abscissa(p0, p1, pinf, p_norm)
    if not zero_test(norm_abscissa + 1):
        raise ProofAssertionError(f"Golden norm throw expected -1, got {norm_abscissa}")

    sq_abscissa = projective_abscissa(p0, p1, pinf, p_sq)
    return {
        "phi": phi,
        "P_phi": p_phi,
        "P_phi_squared": p_sq,
        "P_phi_plus_1": p_plus_1,
        "abscissa_phi_squared": sq_abscissa,
        "abscissa_norm": norm_abscissa,
        "points_coincide": True,
        "circles_used": len(model.circles),
    }
