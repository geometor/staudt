"""Comprehensive exact symbolic test suite for ``geometor.staudt``."""

from __future__ import annotations

from pathlib import Path

import pytest
import sympy as sp
import sympy.geometry as spg
from geometor.model import Model
from geometor.model.invariants import cross_ratio

from geometor.staudt import (
    ConcordanceEntry,
    PaschAuditResult,
    SourceWitness,
    __version__,
    assert_straightedge_only,
    construct_harmonic_fourth_straightedge,
    construct_harmonic_scale,
    construct_parallel_straightedge,
    construct_von_staudt_addition,
    construct_von_staudt_multiplication,
    demonstrate_euclid_i16_pasch_gap,
    demonstrate_euclid_i21_pasch_gap,
    demonstrate_pasch_axiom,
    get_repo_root,
    is_between,
    is_collinear,
    load_concordance,
    load_sources_manifest,
    pair_separates,
    point_from_abscissa,
    projective_abscissa,
    prove_symbolic_quadrangle_uniqueness,
    verify_golden_throw_identity,
    verify_quadrangle_independence,
    verify_source_witnesses,
)
from geometor.staudt.cli import main as cli_main
from geometor.staudt.render import build_all_figures

Point = spg.Point


# ---------------------------------------------------------------------------
# 1. Package Version & Straightedge-Only Invariant
# ---------------------------------------------------------------------------


def test_version_and_straightedge_guard() -> None:
    assert __version__ == "0.1.1"
    model = Model("straightedge_test", auto_intersect=False)
    A = model.set_point(0, 0, classes=["given"], label="A")
    B = model.set_point(1, 0, classes=["given"], label="B")
    model.construct_line(A, B)
    assert_straightedge_only(model)

    model.construct_circle(A, B)
    with pytest.raises(AssertionError, match="Straightedge-only"):
        assert_straightedge_only(model)


# ---------------------------------------------------------------------------
# 2. Collinearity, Betweenness, Separation & Projective Abscissae
# ---------------------------------------------------------------------------


def test_collinear_between_and_separation() -> None:
    A = Point(0, 0)
    C = Point(1, 1)
    B = Point(3, 3)
    D = Point(sp.Rational(3, 2), sp.Rational(3, 2))
    E = Point(0, 2)

    assert is_collinear(A, C, B)
    assert not is_collinear(A, B, E)

    # is_between(endpoint_1, endpoint_2, interior_point)
    assert is_between(A, B, C)
    assert is_between(B, A, C)
    assert not is_between(A, B, A)
    assert not is_between(A, C, B)
    assert not is_between(A, B, E)

    F = Point(-3, -3)
    assert pair_separates(A, B, D, F)
    assert pair_separates(B, A, F, D)
    assert not pair_separates(A, D, B, F)
    assert not pair_separates(A, A, D, F)
    assert not pair_separates(A, B, D, E)


def test_projective_abscissa_finite_and_ideal() -> None:
    P0 = Point(1, 2)
    P1 = Point(3, 5)
    for k in [sp.Integer(0), sp.Integer(1), sp.Integer(-2), sp.Rational(7, 3), sp.GoldenRatio]:
        X = point_from_abscissa(P0, P1, None, k)
        assert is_collinear(P0, P1, X)
        recovered = projective_abscissa(P0, P1, None, X)
        assert sp.simplify(recovered - k) == 0

    Q0 = Point(0, 1)
    Q1 = Point(2, 3)
    Qinf = Point(6, 7)
    for k in [sp.Integer(0), sp.Integer(1), sp.Integer(2), sp.Rational(-3, 4), sp.sqrt(2)]:
        X = point_from_abscissa(Q0, Q1, Qinf, k)
        assert is_collinear(Q0, Q1, X)
        recovered = projective_abscissa(Q0, Q1, Qinf, X)
        assert sp.simplify(recovered - k) == 0


def test_projective_abscissa_validation_errors() -> None:
    P0 = Point(0, 0)
    P1 = Point(1, 0)
    Pinf = Point(4, 0)
    off = Point(1, 2)

    with pytest.raises(TypeError, match=r"sp\.Float"):
        point_from_abscissa(P0, P1, Pinf, sp.Float(1.5))

    with pytest.raises(ValueError, match="infinite abscissa"):
        projective_abscissa(P0, P1, Pinf, Pinf)

    with pytest.raises(ValueError, match="distinct"):
        projective_abscissa(P0, P0, None, P1)

    with pytest.raises(ValueError, match="collinear"):
        projective_abscissa(P0, P1, None, off)

    with pytest.raises(ValueError, match="distinct"):
        projective_abscissa(P0, P1, P1, P0)


# ---------------------------------------------------------------------------
# 3. Complete Quadrangle & Harmonic Fourth (1847 §§ 6-8)
# ---------------------------------------------------------------------------


def test_harmonic_fourth_straightedge_horizontal_and_tilted() -> None:
    m1 = Model("quad_horizontal", auto_intersect=False)
    A = m1.set_point(0, 0, classes=["given"], label="A")
    B = m1.set_point(6, 0, classes=["given"], label="B")
    C = m1.set_point(2, 0, classes=["given"], label="C")
    D = construct_harmonic_fourth_straightedge(m1, A, B, C)
    assert_straightedge_only(m1)
    assert D == Point(-6, 0)
    assert cross_ratio(A, B, C, D) == -1
    assert pair_separates(A, B, C, D)

    m2 = Model("quad_tilted", auto_intersect=False)
    At = m2.set_point(1, 1, classes=["given"], label="A")
    Bt = m2.set_point(5, 3, classes=["given"], label="B")
    Ct = m2.set_point(2, sp.Rational(3, 2), classes=["given"], label="C")
    Dt = construct_harmonic_fourth_straightedge(m2, At, Bt, Ct)
    assert_straightedge_only(m2)
    assert is_collinear(At, Bt, Dt)
    assert cross_ratio(At, Bt, Ct, Dt) == -1
    assert pair_separates(At, Bt, Ct, Dt)


def test_quadrangle_independence_and_symbolic_uniqueness() -> None:
    A = Point(0, 0)
    B = Point(4, 0)
    C = Point(1, 0)
    quad_cmp = verify_quadrangle_independence(
        A,
        B,
        C,
        (Point(1, 3), Point(2, 1)),
        (Point(-2, 5), Point(0, 2)),
    )
    assert quad_cmp["D1"] == quad_cmp["D2"] == Point(-2, 0)
    assert quad_cmp["identical"] is True

    sym = prove_symbolic_quadrangle_uniqueness()
    c = sp.Symbol("c", real=True)
    assert sp.simplify(sym["D_x"] - c / (2 * c - 1)) == 0
    assert sym["D_y"] == 0
    assert sym["cross_ratio"] == -1


def test_quadrangle_error_branches() -> None:
    m = Model("quad_err", auto_intersect=False)
    A = m.set_point(0, 0, classes=["given"])
    B = m.set_point(4, 0, classes=["given"])
    off = m.set_point(1, 2, classes=["given"])
    with pytest.raises(ValueError, match="collinear"):
        construct_harmonic_fourth_straightedge(m, A, B, off)
    with pytest.raises(ValueError, match="distinct"):
        construct_harmonic_fourth_straightedge(m, A, A, B)


# ---------------------------------------------------------------------------
# 4. Algebra of Throws: Addition, Multiplication, Scale & Golden Identity
# ---------------------------------------------------------------------------


def test_parallel_straightedge() -> None:
    m = Model("steiner_parallel", auto_intersect=False)
    A = m.set_point(0, 0, classes=["given"])
    B = m.set_point(4, 2, classes=["given"])
    U0 = m.set_point(0, 3, classes=["given"])
    U1 = m.set_point(2, 4, classes=["given"])
    R = m.set_point(1, 6, classes=["given"])
    par = construct_parallel_straightedge(m, A, B, U0, U1, R)
    assert_straightedge_only(m)
    a1, b1, _ = m.construct_line(A, B).coefficients
    a2, b2, c2 = par.coefficients
    assert sp.simplify(a1 * b2 - a2 * b1) == 0
    assert sp.simplify(a2 * R.x + b2 * R.y + c2) == 0


@pytest.mark.parametrize("use_finite_pinf", [True, False])
def test_von_staudt_field_axioms(use_finite_pinf: bool) -> None:
    """Verify addition, multiplication, identities, commutativity, associativity, distributivity."""
    m = Model(f"throws_{use_finite_pinf}", auto_intersect=False)
    P0 = m.set_point(0, 0, classes=["given"], label="P0")
    P1 = m.set_point(1, 0, classes=["given"], label="P1")
    Pinf = m.set_point(12, 0, classes=["given"], label="Pinf") if use_finite_pinf else None
    rail = None
    if not use_finite_pinf:
        r0 = m.set_point(0, 2, classes=["given"], label="R0")
        r1 = m.set_point(3, 2, classes=["given"], label="R1")
        rail = (r0, r1)

    def pt(val: int | sp.Expr, lbl: str) -> spg.Point:
        p = point_from_abscissa(P0, P1, Pinf, sp.sympify(val))
        return m.set_point(p.x, p.y, classes=["given"], label=lbl)

    P2 = pt(2, "P2")
    P3 = pt(3, "P3")
    P4 = pt(4, "P4")

    # 2 + 3 = 5 & commutativity 3 + 2 = 5
    S_2_3 = construct_von_staudt_addition(m, P0, P1, Pinf, P2, P3, parallel_rail=rail)
    assert projective_abscissa(P0, P1, Pinf, S_2_3) == 5
    S_3_2 = construct_von_staudt_addition(m, P0, P1, Pinf, P3, P2, parallel_rail=rail)
    assert S_3_2 == S_2_3

    # Additive identities: 0 + 3 = 3, 3 + 0 = 3, 0 + 0 = 0
    assert construct_von_staudt_addition(m, P0, P1, Pinf, P0, P3, parallel_rail=rail) == P3
    assert construct_von_staudt_addition(m, P0, P1, Pinf, P3, P0, parallel_rail=rail) == P3
    assert construct_von_staudt_addition(m, P0, P1, Pinf, P0, P0, parallel_rail=rail) == P0

    # Associativity of addition: (2 + 3) + 4 == 2 + (3 + 4) == 9
    S_23_4 = construct_von_staudt_addition(m, P0, P1, Pinf, S_2_3, P4, parallel_rail=rail)
    S_3_4 = construct_von_staudt_addition(m, P0, P1, Pinf, P3, P4, parallel_rail=rail)
    S_2_34 = construct_von_staudt_addition(m, P0, P1, Pinf, P2, S_3_4, parallel_rail=rail)
    assert projective_abscissa(P0, P1, Pinf, S_23_4) == 9
    assert S_23_4 == S_2_34

    # 2 * 3 = 6 & commutativity 3 * 2 = 6
    M_2_3 = construct_von_staudt_multiplication(m, P0, P1, Pinf, P2, P3, parallel_rail=rail)
    M_3_2 = construct_von_staudt_multiplication(m, P0, P1, Pinf, P3, P2, parallel_rail=rail)
    assert projective_abscissa(P0, P1, Pinf, M_2_3) == 6
    assert M_2_3 == M_3_2

    # Multiplicative identities & zero annihilation
    assert construct_von_staudt_multiplication(m, P0, P1, Pinf, P1, P3, parallel_rail=rail) == P3
    assert construct_von_staudt_multiplication(m, P0, P1, Pinf, P3, P1, parallel_rail=rail) == P3
    assert construct_von_staudt_multiplication(m, P0, P1, Pinf, P1, P1, parallel_rail=rail) == P1
    assert construct_von_staudt_multiplication(m, P0, P1, Pinf, P0, P3, parallel_rail=rail) == P0
    assert construct_von_staudt_multiplication(m, P0, P1, Pinf, P3, P0, parallel_rail=rail) == P0

    # Distributivity: 2 * (3 + 4) == 2*3 + 2*4 == 14
    lhs = construct_von_staudt_multiplication(m, P0, P1, Pinf, P2, S_3_4, parallel_rail=rail)
    M_2_4 = construct_von_staudt_multiplication(m, P0, P1, Pinf, P2, P4, parallel_rail=rail)
    rhs = construct_von_staudt_addition(m, P0, P1, Pinf, M_2_3, M_2_4, parallel_rail=rail)
    assert projective_abscissa(P0, P1, Pinf, lhs) == 14
    assert lhs == rhs
    assert_straightedge_only(m)


def test_harmonic_scale_and_golden_throw_identity() -> None:
    m = Model("harmonic_scale", auto_intersect=False)
    P0 = m.set_point(0, 0, classes=["given"], label="P0")
    P1 = m.set_point(1, 0, classes=["given"], label="P1")
    Pinf = m.set_point(8, 0, classes=["given"], label="Pinf")
    scale = construct_harmonic_scale(m, P0, P1, Pinf, max_n=5)
    assert_straightedge_only(m)
    for n in range(-1, 6):
        assert projective_abscissa(P0, P1, Pinf, scale[n]) == n

    res_proj = verify_golden_throw_identity(P0, P1, Pinf)
    assert res_proj["P_phi_squared"] == res_proj["P_phi_plus_1"]
    assert res_proj["points_coincide"] is True
    assert res_proj["circles_used"] == 0
    assert sp.simplify(res_proj["abscissa_phi_squared"] - sp.GoldenRatio**2) == 0

    res_aff = verify_golden_throw_identity(Point(0, 0), Point(2, 1), None)
    assert res_aff["P_phi_squared"] == res_aff["P_phi_plus_1"]
    assert res_aff["points_coincide"] is True
    assert res_aff["circles_used"] == 0
    assert sp.simplify(res_aff["abscissa_phi_squared"] - (sp.GoldenRatio + 1)) == 0


# ---------------------------------------------------------------------------
# 5. Moritz Pasch's Planar Separation Axiom & Euclidean Gap Audits
# ---------------------------------------------------------------------------


def test_pasch_axiom_all_configurations() -> None:
    A = Point(0, 0)
    B = Point(6, 0)
    C = Point(2, 5)

    m1 = Model("pasch_ab_bc", auto_intersect=False)
    r1 = demonstrate_pasch_axiom(m1, A, B, C, Point(3, -1), Point(5, 3))
    assert isinstance(r1, PaschAuditResult)
    assert r1.satisfies_pasch
    assert {name for name, _ in r1.entered_sides} == {"AB", "BC"}
    assert_straightedge_only(m1)

    m2 = Model("pasch_ab_ac", auto_intersect=False)
    r2 = demonstrate_pasch_axiom(m2, A, B, C, Point(2, -1), Point(0, 3))
    assert r2.satisfies_pasch
    assert {name for name, _ in r2.entered_sides} == {"AB", "CA"}

    m3 = Model("pasch_ac_bc", auto_intersect=False)
    r3 = demonstrate_pasch_axiom(m3, A, B, C, Point(-1, 2), Point(6, 2))
    assert r3.satisfies_pasch
    assert {name for name, _ in r3.entered_sides} == {"BC", "CA"}

    m4 = Model("pasch_exterior", auto_intersect=False)
    r4 = demonstrate_pasch_axiom(m4, A, B, C, Point(0, -2), Point(6, -1))
    assert r4.satisfies_pasch
    assert r4.entered_sides == ()

    m5 = Model("pasch_vertex", auto_intersect=False)
    r5 = demonstrate_pasch_axiom(m5, A, B, C, C, Point(3, 0))
    assert r5.vertex_hits == ("C",)
    assert r5.satisfies_pasch


def test_euclid_i16_and_i21_pasch_audits() -> None:
    m_i16, i16 = demonstrate_euclid_i16_pasch_gap()
    assert_straightedge_only(m_i16)
    assert i16["B_C_D_between"] is True
    assert i16["A_E_C_between"] is True
    assert i16["B_E_F_between"] is True
    assert i16["K_between_A_and_D"] is True
    assert i16["pasch_audit_ABD"].satisfies_pasch is True

    m_i21, i21 = demonstrate_euclid_i21_pasch_gap()
    assert_straightedge_only(m_i21)
    assert i21["E_between_A_and_C"] is True
    assert i21["D_between_B_and_E"] is True
    assert i21["pasch_audit_AMC"].satisfies_pasch is True


# ---------------------------------------------------------------------------
# 6. Concordance, Source Witnesses, SVG Renderer & CLI
# ---------------------------------------------------------------------------


def test_concordance_and_source_witnesses() -> None:
    root = get_repo_root()
    assert (root / "pyproject.toml").exists()

    entries = load_concordance()
    assert len(entries) >= 12
    assert all(isinstance(e, ConcordanceEntry) for e in entries)

    witnesses = load_sources_manifest()
    assert len(witnesses) == 3
    assert all(isinstance(w, SourceWitness) for w in witnesses)

    checks = verify_source_witnesses()
    assert len(checks) == 3
    assert all(checks.values()), f"Witness check failed: {checks}"


def test_render_and_cli(tmp_path: Path) -> None:
    written = build_all_figures(tmp_path)
    assert len(written) == 8
    for svg_path in written:
        assert svg_path.exists()
        content = svg_path.read_text(encoding="utf-8")
        assert "<svg" in content
        assert "euclid-graphic" in content

    assert cli_main(["summary"]) == 0
    assert cli_main(["verify"]) == 0
