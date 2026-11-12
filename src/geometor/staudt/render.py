"""Exact SymPy-driven SVG figure builder generating the 8 standalone ``.euclid-graphic``
diagrams for ``geometor/staudt``.

All geometric intersections are computed symbolically via :mod:`geometor.model` and
:mod:`geometor.staudt`; floating-point evaluation ``float(expr.evalf())`` occurs strictly
at final SVG viewport projection time and never enters any :class:`~geometor.model.Model`.
"""

from __future__ import annotations

from dataclasses import dataclass
from html import escape
from pathlib import Path

import sympy as sp
import sympy.geometry as spg
from geometor.model import Model, intersect_2d

from geometor.staudt.concordance import get_repo_root
from geometor.staudt.pasch import demonstrate_euclid_i21_pasch_gap, demonstrate_pasch_axiom
from geometor.staudt.projective import point_from_abscissa
from geometor.staudt.quadrangle import construct_harmonic_fourth_straightedge
from geometor.staudt.throws import (
    construct_harmonic_scale,
    construct_von_staudt_addition,
    construct_von_staudt_multiplication,
)

__all__ = ["build_all_figures"]


@dataclass
class _SvgCanvas:
    """Lightweight theme-adaptive ``.euclid-graphic`` SVG composer."""

    width: int
    height: int
    x_min: float
    x_max: float
    y_min: float
    y_max: float
    title: str
    desc: str

    def __post_init__(self) -> None:
        self.elements: list[str] = []
        pad = 44.0
        sx = (self.width - 2 * pad) / (self.x_max - self.x_min)
        sy = (self.height - 2 * pad) / (self.y_max - self.y_min)
        self.scale = min(sx, sy)
        used_w = (self.x_max - self.x_min) * self.scale
        used_h = (self.y_max - self.y_min) * self.scale
        self.ox = (self.width - used_w) / 2.0
        self.oy = (self.height - used_h) / 2.0

    def map_pt(self, pt: spg.Point | tuple[float | sp.Expr, float | sp.Expr]) -> tuple[float, float]:
        if isinstance(pt, spg.Point):
            px, py = float(pt.x.evalf()), float(pt.y.evalf())
        else:
            px = float(sp.sympify(pt[0]).evalf())
            py = float(sp.sympify(pt[1]).evalf())
        sx = self.ox + (px - self.x_min) * self.scale
        sy = self.height - (self.oy + (py - self.y_min) * self.scale)
        return sx, sy

    def seg(
        self,
        p1: spg.Point | tuple[float | sp.Expr, float | sp.Expr],
        p2: spg.Point | tuple[float | sp.Expr, float | sp.Expr],
        *,
        cls: str = "line-primary",
    ) -> None:
        x1, y1 = self.map_pt(p1)
        x2, y2 = self.map_pt(p2)
        self.elements.append(
            f'  <line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" class="{cls}" />'
        )

    def poly(
        self,
        pts: list[spg.Point | tuple[float | sp.Expr, float | sp.Expr]],
        *,
        cls: str = "poly-fill",
    ) -> None:
        coords = " ".join(f"{x:.2f},{y:.2f}" for x, y in (self.map_pt(p) for p in pts))
        self.elements.append(f'  <polygon points="{coords}" class="{cls}" />')

    def ellipse_world(
        self,
        cx: float,
        cy: float,
        rx: float,
        ry: float,
        *,
        cls: str = "conic-locus",
    ) -> None:
        scx, scy = self.map_pt((cx, cy))
        srx = rx * self.scale
        sry = ry * self.scale
        self.elements.append(
            f'  <ellipse cx="{scx:.2f}" cy="{scy:.2f}" rx="{srx:.2f}" ry="{sry:.2f}" class="{cls}" />'
        )

    def dot(
        self,
        pt: spg.Point | tuple[float | sp.Expr, float | sp.Expr],
        label: str = "",
        *,
        dx: float = 8.0,
        dy: float = -8.0,
        cls: str = "pt-given",
        r: float = 4.2,
        anchor: str = "start",
    ) -> None:
        sx, sy = self.map_pt(pt)
        self.elements.append(
            f'  <circle cx="{sx:.2f}" cy="{sy:.2f}" r="{r:.1f}" class="{cls}" />'
        )
        if label:
            lx = sx + dx
            ly = sy + dy
            self.elements.append(
                f'  <text x="{lx:.2f}" y="{ly:.2f}" text-anchor="{anchor}" class="glyph-label">{escape(label)}</text>'
            )

    def caption(self, x_px: float, y_px: float, text: str, *, anchor: str = "middle") -> None:
        self.elements.append(
            f'  <text x="{x_px:.2f}" y="{y_px:.2f}" text-anchor="{anchor}" class="diagram-caption">{escape(text)}</text>'
        )

    def render(self) -> str:
        header = f"""<svg xmlns="http://www.w3.org/2000/svg" class="euclid-graphic" viewBox="0 0 {self.width} {self.height}" role="img" aria-label="{escape(self.title)}">
  <title>{escape(self.title)}</title>
  <desc>{escape(self.desc)}</desc>
  <style>
    .euclid-graphic {{ width: 100%; height: auto; max-width: {self.width}px; display: block; margin: 1.25rem auto; color: currentColor; }}
    .line-primary {{ stroke: currentColor; stroke-width: 2.0; stroke-linecap: round; fill: none; opacity: 0.92; }}
    .line-guide {{ stroke: currentColor; stroke-width: 1.15; stroke-dasharray: 5 4; fill: none; opacity: 0.52; }}
    .line-secondary {{ stroke: #2b7bba; stroke-width: 1.45; stroke-dasharray: 3 3; fill: none; opacity: 0.78; }}
    .line-accent {{ stroke: #d95f02; stroke-width: 2.25; stroke-linecap: round; fill: none; }}
    .line-result {{ stroke: #1b9e77; stroke-width: 2.4; stroke-linecap: round; fill: none; }}
    .conic-locus {{ stroke: #d95f02; stroke-width: 2.3; fill: none; }}
    .poly-fill {{ fill: currentColor; fill-opacity: 0.06; stroke: currentColor; stroke-width: 1.8; stroke-linejoin: round; }}
    .poly-accent {{ fill: #2b7bba; fill-opacity: 0.09; stroke: #2b7bba; stroke-width: 1.5; stroke-linejoin: round; }}
    .pt-given {{ fill: currentColor; stroke: #ffffff; stroke-width: 1.3; }}
    .pt-aux {{ fill: #2b7bba; stroke: #ffffff; stroke-width: 1.2; }}
    .pt-result {{ fill: #d95f02; stroke: #ffffff; stroke-width: 1.6; }}
    .pt-emerald {{ fill: #1b9e77; stroke: #ffffff; stroke-width: 1.5; }}
    .glyph-label {{ font-family: "Libertinus Serif", "STIX Two Text", Georgia, serif; font-size: 15px; font-style: italic; fill: currentColor; paint-order: stroke; stroke: rgba(255,255,255,0.82); stroke-width: 3.2px; stroke-linejoin: round; }}
    .diagram-caption {{ font-family: "Libertinus Sans", system-ui, sans-serif; font-size: 13px; fill: currentColor; opacity: 0.82; }}
    @media (prefers-color-scheme: dark) {{
      .glyph-label {{ stroke: rgba(20,22,26,0.88); }}
      .pt-given, .pt-aux, .pt-result, .pt-emerald {{ stroke: #181a1f; }}
    }}
  </style>
"""
        body = "\n".join(self.elements)
        return f"{header}{body}\n</svg>\n"


def _fig1_ideal_sheaf_perspectivity() -> str:
    """Codex I Unit 1: Perspectivity sending a parallel ray to the horizon point P_inf."""
    S = spg.Point(2, 5)
    # Line l: y = 0; Line m (tilted screen): through (4, -1) and (7, 5) -> slope 2: y = 2x - 9.
    # Better: S = (0, 4), carrier l: y = 0 with A=(-1,0), B=(2,0), C=(5,0), and ideal P_inf -> right!
    # Tilted line m through (-1, -0.5) and (5, 5.5): slope 1 -> y = x + 0.5!
    # Horizontal ray from S=(0,4) parallel to l: y = 4 meets m (y = x + 0.5) at I_m = (7/2, 4)!
    S = spg.Point(0, 4)
    l_base = spg.Line(spg.Point(-2, 0), spg.Point(7, 0))
    m_proj = spg.Line(spg.Point(-2, sp.Rational(-3, 2)), spg.Point(6, sp.Rational(13, 2)))
    A = spg.Point(-1, 0)
    B = spg.Point(1, 0)
    C = spg.Point(3, 0)
    A_p = intersect_2d(spg.Line(S, A), m_proj)[0]
    B_p = intersect_2d(spg.Line(S, B), m_proj)[0]
    C_p = intersect_2d(spg.Line(S, C), m_proj)[0]
    ray_par = spg.Line(S, spg.Point(6, 4))
    P_inf_m = intersect_2d(ray_par, m_proj)[0]
    O_meet = intersect_2d(l_base, m_proj)[0]

    cv = _SvgCanvas(
        width=760,
        height=430,
        x_min=-2.4,
        x_max=7.2,
        y_min=-1.3,
        y_max=5.8,
        title="Von Staudt §§ 1–5: Ideal Point at Infinity Unified by Central Perspectivity",
        desc="Central projection from S mapping finite points A, B, C and the parallel direction P_inf of line l onto finite points A', B', C', J' of transversal m.",
    )
    cv.seg((-2.1, 0), (6.8, 0), cls="line-primary")
    cv.seg((-1.8, -1.3), (4.9, 5.4), cls="line-primary")
    # Parallel sheaf lines horizontal (showing parallel pencil sharing ideal point P_inf)
    cv.seg((-2.1, -0.8), (6.8, -0.8), cls="line-guide")
    cv.seg((-1.5, 4.0), (6.8, 4.0), cls="line-accent")
    # Projecting rays from S
    for tgt, t_p in ((A, A_p), (B, B_p), (C, C_p)):
        cv.seg(S, tgt, cls="line-secondary")
        cv.seg(S, t_p, cls="line-secondary")

    cv.dot(O_meet, "O = l ∩ m", dx=-14, dy=18, anchor="middle")
    cv.dot(S, "S", dx=-14, dy=-8, cls="pt-aux", anchor="end")
    cv.dot(A, "A", dx=0, dy=19, anchor="middle")
    cv.dot(B, "B", dx=0, dy=19, anchor="middle")
    cv.dot(C, "C", dx=0, dy=19, anchor="middle")
    cv.dot(A_p, "A'", dx=-10, dy=-8, cls="pt-aux", anchor="end")
    cv.dot(B_p, "B'", dx=-10, dy=-8, cls="pt-aux", anchor="end")
    cv.dot(C_p, "C'", dx=9, dy=4, cls="pt-aux")
    cv.dot(P_inf_m, "P'∞ (vanishing point)", dx=10, dy=-8, cls="pt-result", r=5.0)
    cv.caption(590, 298, "to ideal point P∞ along parallel sheaf →", anchor="middle")
    cv.caption(
        380,
        412,
        "Geometrie der Lage §§ 1–5: Parallel ray [S P∞] ∥ l projects the ideal point of l to the finite vanishing point P'∞ on m",
    )
    return cv.render()


def _fig2_complete_quadrangle_harmonic() -> str:
    """Codex I Unit 2: Two independent complete quadrangles constructing the identical harmonic 4th D."""
    m = Model("fig2", auto_intersect=False, enable_logging=False)
    A = m.given_point(0, 0, label="A")
    B = m.given_point(6, 0, label="B")
    C = m.given_point(2, 0, label="C")
    E1 = m.given_point(2, 4, label="E")
    G1 = m.given_point(2, 2, label="G")
    D = construct_harmonic_fourth_straightedge(m, A, B, C, E1, G1, label="D")
    F1 = intersect_2d(spg.Line(A, E1), spg.Line(B, G1))[0]
    H1 = intersect_2d(spg.Line(A, G1), spg.Line(B, E1))[0]

    # Second quadrangle below the axis proving Desarguesian uniqueness!
    m2 = Model("fig2_alt", auto_intersect=False, enable_logging=False)
    a2 = m2.given_point(0, 0, label="A")
    b2 = m2.given_point(6, 0, label="B")
    c2 = m2.given_point(2, 0, label="C")
    E2 = m2.given_point(3, -3, label="E'")
    G2 = m2.given_point(sp.Rational(5, 2), sp.Rational(-3, 2), label="G'")
    _ = construct_harmonic_fourth_straightedge(m2, a2, b2, c2, E2, G2, label="D'")
    F2 = intersect_2d(spg.Line(A, E2), spg.Line(B, G2))[0]
    H2 = intersect_2d(spg.Line(A, G2), spg.Line(B, E2))[0]

    cv = _SvgCanvas(
        width=780,
        height=460,
        x_min=-6.8,
        x_max=6.9,
        y_min=-3.6,
        y_max=4.6,
        title="Von Staudt §§ 7–8 (Art. 93): Complete Quadrangle Harmonic Fourth & Desarguesian Uniqueness",
        desc="Upper quadrangle EFGH and lower quadrangle E'F'G'H' sharing A, B, C both intersect line AB in the unique fourth harmonic conjugate D = (-6, 0).",
    )
    cv.seg((-6.5, 0), (6.6, 0), cls="line-primary")
    # Upper quadrangle EFGH
    for p, q in ((A, E1), (B, E1), (A, G1), (B, G1)):
        cv.seg(p, q, cls="line-guide")
    cv.seg(E1, C, cls="line-secondary")
    cv.seg(H1, D, cls="line-accent")
    # Lower quadrangle E'F'G'H'
    for p, q in ((A, E2), (B, E2), (A, G2), (B, G2)):
        cv.seg(p, q, cls="line-guide")
    cv.seg(E2, C, cls="line-secondary")
    cv.seg(H2, D, cls="line-result")

    cv.dot(A, "A", dx=-4, dy=18, anchor="middle")
    cv.dot(B, "B", dx=4, dy=18, anchor="middle")
    cv.dot(C, "C", dx=5, dy=18, anchor="start")
    cv.dot(D, "D", dx=0, dy=-12, cls="pt-result", r=5.2, anchor="middle")
    cv.dot(E1, "E", dx=0, dy=-10, cls="pt-aux", anchor="middle")
    cv.dot(G1, "G", dx=8, dy=3, cls="pt-aux")
    cv.dot(F1, "F", dx=-10, dy=-5, cls="pt-aux", anchor="end")
    cv.dot(H1, "H", dx=8, dy=-6, cls="pt-aux")
    cv.dot(E2, "E'", dx=6, dy=15, cls="pt-emerald")
    cv.dot(G2, "G'", dx=9, dy=5, cls="pt-emerald")
    cv.dot(F2, "F'", dx=-10, dy=12, cls="pt-emerald", anchor="end")
    cv.dot(H2, "H'", dx=10, dy=10, cls="pt-emerald")
    cv.caption(
        390,
        442,
        "Geometrie der Lage §§ 7–8 (Art. 93): Independent quadrangles EFGH and E'F'G'H' determine the identical harmonic fourth D with (A, B; C, D) = −1",
    )
    return cv.render()


def _fig3_polar_conic_self_conjugate() -> str:
    """Codex I Unit 3: Von Staudt's polar definition of a conic & Pascal's Hexagrammum Mysticum."""
    # Exact rational points on circle/conic x^2 + y^2 = 25 (drawn purely as locus of x*x0 + y*y0 = 25 polarity!)
    # Rational points: P1=(-5,0), P2=(-3,4), P3=(3,4), P4=(5,0), P5=(4,-3), P6=(-4,-3)
    P1 = spg.Point(-5, 0)
    P2 = spg.Point(-3, 4)
    P3 = spg.Point(3, 4)
    P4 = spg.Point(5, 0)
    P5 = spg.Point(4, -3)
    P6 = spg.Point(-4, -3)
    # Pole Q = (0, 25/4): its polar pi(Q) is y = 4, passing through self-conjugate points P2=(-3,4) and P3=(3,4)!
    Q_pole = spg.Point(0, sp.Rational(25, 4))

    # Pascal hexagon P1-P2-P5-P4-P3-P6 (cross-laced so opposite intersections lie compactly inside viewport!):
    # Opposite pairs: (P1 P2) & (P4 P3); (P2 P5) & (P3 P6); (P5 P4) & (P6 P1)
    X_pas = intersect_2d(spg.Line(P1, P2), spg.Line(P4, P3))[0]  # (0, 25/2)? Wait: P1=(-5,0)->P2=(-3,4) slope 2, y=2(x+5)=2x+10 -> (0,10); let's use P1=(-5,0), P3=(3,4), P5=(4,-3), P2=(-3,4), P4=(5,0), P6=(-4,-3)!
    # Check hexagon H = [P1, P3, P5, P2, P4, P6]:
    # Side 1 [P1 P3] & Side 4 [P2 P4]: (-5,0)-(3,4) and (-3,4)-(5,0) -> meet at (0, 5/2)!
    # Side 2 [P3 P5] & Side 5 [P4 P6]: (3,4)-(4,-3) and (5,0)-(-4,-3) -> compact inside circle!
    # Side 3 [P5 P2] & Side 6 [P6 P1]: (4,-3)-(-3,4) and (-4,-3)-(-5,0) -> compact!
    M1 = intersect_2d(spg.Line(P1, P3), spg.Line(P2, P4))[0]
    M2 = intersect_2d(spg.Line(P3, P5), spg.Line(P4, P6))[0]
    M3 = intersect_2d(spg.Line(P5, P2), spg.Line(P6, P1))[0]
    _ = X_pas

    cv = _SvgCanvas(
        width=760,
        height=480,
        x_min=-7.2,
        x_max=7.2,
        y_min=-4.8,
        y_max=7.2,
        title="Von Staudt §§ 18–19 (Arts. 246–257): Conic as Self-Conjugate Locus of a Polarity & Pascal's Line",
        desc="Curve of the second order defined as P in pi(P) with pole Q, chord polar pi(Q) = [P2 P3], tangents pi(P2), pi(P3), and collinear Pascal points M1, M2, M3.",
    )
    cv.ellipse_world(0.0, 0.0, 5.0, 5.0, cls="conic-locus")
    # Tangents pi(P2) and pi(P3) meeting at pole Q = (0, 25/4) and polar chord pi(Q) = y=4
    cv.seg((-6.4, 4.0), (6.4, 4.0), cls="line-secondary")
    cv.seg(Q_pole, (-6.2, 1.6), cls="line-guide")
    cv.seg(Q_pole, (6.2, 1.6), cls="line-guide")

    # Inscribed Pascal hexagram [P1, P3, P5, P2, P4, P6]
    hex_seq = [P1, P3, P5, P2, P4, P6]
    for i in range(6):
        cv.seg(hex_seq[i], hex_seq[(i + 1) % 6], cls="line-primary")
    # Extend [P6 P1] slightly to M3 if needed
    cv.seg(P6, M3, cls="line-guide")
    cv.seg(P2, M3, cls="line-guide")
    # Pascal line through M1, M2, M3
    p_dir_x = float((M3.x - M2.x).evalf())
    p_dir_y = float((M3.y - M2.y).evalf())
    m2x, m2y = float(M2.x.evalf()), float(M2.y.evalf())
    cv.seg(
        (m2x - 0.35 * p_dir_x, m2y - 0.35 * p_dir_y),
        (m2x + 1.25 * p_dir_x, m2y + 1.25 * p_dir_y),
        cls="line-result",
    )

    cv.dot(Q_pole, "Q (pole of [P₂P₃])", dx=10, dy=-2, cls="pt-aux")
    cv.dot(P1, "P₁", dx=-10, dy=-6, anchor="end")
    cv.dot(P2, "P₂ ∈ π(P₂)", dx=-10, dy=-8, anchor="end")
    cv.dot(P3, "P₃ ∈ π(P₃)", dx=10, dy=-8)
    cv.dot(P4, "P₄", dx=10, dy=-4)
    cv.dot(P5, "P₅", dx=10, dy=12)
    cv.dot(P6, "P₆", dx=-10, dy=14, anchor="end")
    cv.dot(M1, "M₁", dx=0, dy=-10, cls="pt-result", r=4.8, anchor="middle")
    cv.dot(M2, "M₂", dx=9, dy=12, cls="pt-result", r=4.8)
    cv.dot(M3, "M₃", dx=-10, dy=-6, cls="pt-result", r=4.8, anchor="end")
    cv.caption(
        380,
        462,
        "Geometrie der Lage §§ 18–19: Conic defined purely as self-conjugate locus P ∈ π(P), yielding tangents [Q P₂], [Q P₃] and Pascal line [M₁ M₂ M₃]",
    )
    return cv.render()


def _fig4_addition_of_throws() -> str:
    """Codex I Unit 4a: Von Staudt's pure straightedge addition P2 + P3 = P5 on finite horizon P_inf."""
    m = Model("fig4_add", auto_intersect=False, enable_logging=False)
    P0 = m.given_point(0, 0, label="P0")
    P1 = m.given_point(1, 0, label="P1")
    Pinf = m.given_point(8, 0, label="Pinf")
    p2_raw = point_from_abscissa(P0, P1, Pinf, 2)
    p3_raw = point_from_abscissa(P0, P1, Pinf, 3)
    X = m.given_point(p2_raw.x, p2_raw.y, label="P2")
    Y = m.given_point(p3_raw.x, p3_raw.y, label="P3")
    U = m.given_point(1, 3, label="U")
    V = m.given_point(sp.Rational(9, 2), sp.Rational(3, 2), label="V")
    S = construct_von_staudt_addition(m, P0, P1, Pinf, X, Y, aux_U=U, aux_V=V, label="P5")

    R = intersect_2d(spg.Line(U, P0), spg.Line(V, X))[0]
    axis_a = spg.Line(Pinf, R)
    T = intersect_2d(spg.Line(U, Y), axis_a)[0]

    cv = _SvgCanvas(
        width=780,
        height=450,
        x_min=-0.9,
        x_max=8.7,
        y_min=-2.4,
        y_max=3.6,
        title="Von Staudt Beiträge § 19 (Arts. 256–267): Pure Straightedge Addition of Throws (P2 + P3 = P5)",
        desc="Straightedge addition on carrier line (P0, P1, P_inf) using horizon centers U, V on [P_inf U] and perspective axis a = [P_inf R].",
    )
    cv.seg((-0.6, 0), (8.4, 0), cls="line-primary")
    cv.seg(Pinf, U, cls="line-secondary")
    a_left = intersect_2d(
        axis_a,
        spg.Line(spg.Point(sp.Rational(-1, 2), -5), spg.Point(sp.Rational(-1, 2), 5)),
    )[0]
    cv.seg(a_left, Pinf, cls="line-accent")
    cv.seg(U, R, cls="line-guide")
    cv.seg(V, R, cls="line-guide")
    cv.seg(U, Y, cls="line-guide")
    cv.seg(U, T, cls="line-guide")
    cv.seg(V, S, cls="line-result")
    cv.seg(V, T, cls="line-result")

    cv.dot(P0, "P₀ (0)", dx=-4, dy=18, anchor="middle")
    cv.dot(P1, "P₁ (1)", dx=0, dy=18, anchor="middle")
    cv.dot(X, "P₂ (2)", dx=0, dy=-11, anchor="middle")
    cv.dot(Y, "P₃ (3)", dx=4, dy=18, anchor="middle")
    cv.dot(S, "P₅ = P₂ + P₃", dx=0, dy=-12, cls="pt-result", r=5.2, anchor="middle")
    cv.dot(Pinf, "P∞", dx=8, dy=-6, cls="pt-aux")
    cv.dot(U, "U", dx=-8, dy=-6, cls="pt-aux", anchor="end")
    cv.dot(V, "V", dx=8, dy=-6, cls="pt-aux")
    cv.dot(R, "R = [UP₀] ∩ [VP₂]", dx=10, dy=12, cls="pt-aux")
    cv.dot(T, "T = [UP₃] ∩ a", dx=-10, dy=14, cls="pt-emerald", anchor="end")
    cv.caption(
        390,
        432,
        "Beiträge § 19: Centers U, V ∈ [P∞ U] and axis a = [P∞ R] construct P₂ + P₃ = P₅ purely by straightedge with zero circles",
    )
    return cv.render()


def _fig5_multiplication_of_throws() -> str:
    """Codex I Unit 4b: Von Staudt's pure straightedge multiplication P2 * P3 = P6."""
    m = Model("fig5_mul", auto_intersect=False, enable_logging=False)
    P0 = m.given_point(0, 0, label="P0")
    P1 = m.given_point(1, 0, label="P1")
    Pinf = m.given_point(8, 0, label="Pinf")
    p2_raw = point_from_abscissa(P0, P1, Pinf, 2)
    p3_raw = point_from_abscissa(P0, P1, Pinf, 3)
    X = m.given_point(p2_raw.x, p2_raw.y, label="P2")
    Y = m.given_point(p3_raw.x, p3_raw.y, label="P3")
    U = m.given_point(1, 3, label="U")
    V = m.given_point(sp.Rational(-2, 3), -2, label="V")
    P_prod = construct_von_staudt_multiplication(m, P0, P1, Pinf, X, Y, aux_U=U, aux_V=V, label="P6")

    W = intersect_2d(spg.Line(U, P1), spg.Line(V, X))[0]
    axis_a = spg.Line(Pinf, W)
    Z = intersect_2d(spg.Line(U, Y), axis_a)[0]
    a_left = intersect_2d(axis_a, spg.Line(spg.Point(0, -5), spg.Point(0, 5)))[0]

    cv = _SvgCanvas(
        width=780,
        height=450,
        x_min=-1.2,
        x_max=8.7,
        y_min=-2.5,
        y_max=3.5,
        title="Von Staudt Beiträge § 20 (Arts. 268–275): Pure Straightedge Multiplication of Throws (P2 · P3 = P6)",
        desc="Straightedge multiplication on (P0, P1, P_inf) using centers U, V collinear with P0 and perspective axis a = [P_inf W].",
    )
    cv.seg((-1.0, 0), (8.4, 0), cls="line-primary")
    cv.seg(U, V, cls="line-secondary")
    cv.seg(a_left, Pinf, cls="line-accent")
    cv.seg(U, W, cls="line-guide")
    cv.seg(V, X, cls="line-guide")
    cv.seg(U, Y, cls="line-guide")
    cv.seg(V, P_prod, cls="line-result")

    cv.dot(P0, "P₀ (0)", dx=-10, dy=-8, anchor="end")
    cv.dot(P1, "P₁ (1)", dx=-4, dy=18, anchor="middle")
    cv.dot(X, "P₂ (2)", dx=0, dy=-11, anchor="middle")
    cv.dot(Y, "P₃ (3)", dx=2, dy=18, anchor="middle")
    cv.dot(P_prod, "P₆ = P₂ · P₃", dx=6, dy=-12, cls="pt-result", r=5.2, anchor="start")
    cv.dot(Pinf, "P∞", dx=8, dy=-6, cls="pt-aux")
    cv.dot(U, "U", dx=8, dy=-4, cls="pt-aux")
    cv.dot(V, "V ∈ [P₀U]", dx=10, dy=6, cls="pt-aux")
    cv.dot(W, "W = [UP₁] ∩ [VP₂]", dx=-10, dy=-8, cls="pt-aux", anchor="end")
    cv.dot(Z, "Z = [UP₃] ∩ a", dx=10, dy=-6, cls="pt-emerald")
    cv.caption(
        390,
        432,
        "Beiträge § 20: Centers U, V ∈ [P₀ U] and axis a = [P∞ W] construct P₂ · P₃ = P₆ purely by straightedge incidence",
    )
    return cv.render()


def _fig6_harmonic_scale_abscissae() -> str:
    """Codex I Unit 4c: Möbius–von Staudt harmonic integer scale converging to horizon P_inf."""
    m = Model("fig6_scale", auto_intersect=False, enable_logging=False)
    P0 = m.given_point(0, 0, label="P0")
    P1 = m.given_point(2, 0, label="P1")
    Pinf = m.given_point(10, 0, label="Pinf")
    scale = construct_harmonic_scale(m, P0, P1, Pinf, max_n=5)

    # Illustrate explicit quadrangle ladder above y = 0 through horizon Pinf
    U = spg.Point(0, 3)
    V = spg.Point(5, sp.Rational(3, 2))  # on [Pinf U]: y = 3 - (3/10)x -> at x=5, y=3/2

    cv = _SvgCanvas(
        width=780,
        height=390,
        x_min=-3.4,
        x_max=10.8,
        y_min=-0.9,
        y_max=3.6,
        title="Von Staudt Beiträge §§ 19 & 29 (Arts. 267, 404): Harmonic Scale & Projective Abscissae",
        desc="Projective integer scale P_-1, P_0, P_1, P_2, P_3, P_4, P_5 generated by iterated harmonic quadrangles accumulating toward finite horizon P_inf.",
    )
    cv.seg((-3.1, 0), (10.4, 0), cls="line-primary")
    cv.seg(U, Pinf, cls="line-secondary")

    # Show harmonic ladder steps between [U P_k], [V P_{k+1}], and horizon axis
    R1 = intersect_2d(spg.Line(U, P0), spg.Line(V, P1))[0]
    axis = spg.Line(Pinf, R1)
    a_left = intersect_2d(axis, spg.Line(spg.Point(-3, -2), spg.Point(-3, 5)))[0]
    cv.seg(a_left, Pinf, cls="line-accent")
    for k in range(5):
        pk = scale[k]
        pk1 = scale[k + 1]
        tk = intersect_2d(spg.Line(U, pk), axis)[0]
        cv.seg(U, pk, cls="line-guide")
        cv.seg(V, tk, cls="line-guide")
        cv.seg(V, pk1, cls="line-guide")

    cv.dot(U, "U", dx=-8, dy=-6, cls="pt-aux", anchor="end")
    cv.dot(V, "V", dx=8, dy=-6, cls="pt-aux")
    for k, pt in sorted(scale.items()):
        dy = 20 if k % 2 == 0 else -12
        cls = "pt-result" if k >= 2 or k < 0 else "pt-given"
        lbl = f"P_{k}" if k < 0 else f"P{k}"
        cv.dot(pt, lbl, dx=0, dy=dy, cls=cls, anchor="middle")
    cv.dot(Pinf, "P∞ (∞)", dx=6, dy=16, cls="pt-emerald", r=5.0)
    cv.caption(
        390,
        372,
        "Beiträge §§ 19 & 29: Each triple (P_{k−1}, P_k, P_{k+1}) is harmonic with P∞, assigning exact projective abscissae (P∞, P₀; P₁, P_k) = k",
    )
    return cv.render()


def _fig7_pasch_linear_betweenness_separation() -> str:
    """Codex II Unit 1: Pasch linear betweenness (§ 1) vs. 4-point projective pair separation (§ 11)."""
    S = spg.Point(0, 4)
    A = spg.Point(-4, 0)
    C = spg.Point(-1, 0)
    B = spg.Point(2, 0)
    D = spg.Point(5, 0)

    m_line = spg.Line(spg.Point(-4, 2), spg.Point(5, sp.Rational(7, 2)))
    Ap = intersect_2d(spg.Line(S, A), m_line)[0]
    Cp = intersect_2d(spg.Line(S, C), m_line)[0]
    Bp = intersect_2d(spg.Line(S, B), m_line)[0]
    Dp = intersect_2d(spg.Line(S, D), m_line)[0]

    cv = _SvgCanvas(
        width=760,
        height=400,
        x_min=-5.0,
        x_max=6.0,
        y_min=-0.9,
        y_max=4.7,
        title="Moritz Pasch (1882) §§ 1 & 11: Open Linear Betweenness vs. 4-Point Projective Separation",
        desc="Segment interior points C between A and B vs. exterior point D, showing pair separation AB // CD preserved across perspective section.",
    )
    m_left = intersect_2d(
        m_line, spg.Line(spg.Point(sp.Rational(-9, 2), -5), spg.Point(sp.Rational(-9, 2), 5))
    )[0]
    m_right = intersect_2d(
        m_line, spg.Line(spg.Point(sp.Rational(11, 2), -5), spg.Point(sp.Rational(11, 2), 5))
    )[0]
    cv.seg((-4.7, 0), (5.6, 0), cls="line-primary")
    cv.seg(A, B, cls="line-accent")
    cv.seg(m_left, m_right, cls="line-secondary")
    for p in (A, C, B, D):
        cv.seg(S, p, cls="line-guide")

    cv.dot(S, "S", dx=0, dy=-10, cls="pt-aux", anchor="middle")
    cv.dot(A, "A", dx=0, dy=19, anchor="middle")
    cv.dot(C, "C (inside AB)", dx=0, dy=19, cls="pt-result", anchor="middle")
    cv.dot(B, "B", dx=0, dy=19, anchor="middle")
    cv.dot(D, "D (outside AB)", dx=0, dy=19, cls="pt-emerald", anchor="middle")

    cv.dot(Ap, "A'", dx=-8, dy=-8, cls="pt-aux", anchor="end")
    cv.dot(Cp, "C'", dx=-4, dy=-10, cls="pt-result", anchor="middle")
    cv.dot(Bp, "B'", dx=6, dy=-10, cls="pt-aux")
    cv.dot(Dp, "D'", dx=8, dy=-8, cls="pt-emerald")
    cv.caption(
        380,
        382,
        "Pasch (1882) § 1 Grundsätze V–VIII & Lehrsätze 19–23: C lies between A and B while D lies outside AB, yielding invariant pair separation AB // CD",
    )
    return cv.render()


def _fig8_pasch_planar_axiom_euclid_gaps() -> str:
    """Codex II Unit 2: Pasch's Grundsatz IV (§ 2 p. 21) & Crossbar Proof of Euclid I.21."""
    # Left panel in world x in [-8, -1]: Pasch Grundsatz IV on triangle A0 B0 C0
    m_left = Model("fig8_left", auto_intersect=False, enable_logging=False)
    A0 = m_left.given_point(-8, 0, label="A")
    B0 = m_left.given_point(-2, 0, label="B")
    C0 = m_left.given_point(-5, 5, label="C")
    P0 = m_left.given_point(-8, 1, label="P")
    Q0 = m_left.given_point(-1, 3, label="Q")
    audit = demonstrate_pasch_axiom(m_left, A0, B0, C0, P0, Q0)
    hit1 = audit.entered_sides[0][1]
    hit2 = audit.entered_sides[1][1]

    # Right panel in world x in [1, 9]: Euclid I.21 resolved by Pasch on sub-triangle AMC
    _, i21 = demonstrate_euclid_i21_pasch_gap()
    sh = sp.Integer(1)
    A1 = spg.Point(0 + sh, 0)
    B1 = spg.Point(8 + sh, 0)
    C1 = spg.Point(3 + sh, 6)
    D1 = spg.Point(3 + sh, 2)
    M1 = spg.Point(i21["M_on_AB"].x + sh, i21["M_on_AB"].y)
    E1 = spg.Point(i21["E_on_AC"].x + sh, i21["E_on_AC"].y)

    cv = _SvgCanvas(
        width=820,
        height=430,
        x_min=-8.8,
        x_max=9.8,
        y_min=-1.0,
        y_max=6.7,
        title="Moritz Pasch (1882) § 2 IV. Grundsatz (p. 21) & Resolution of Euclid I.21",
        desc="Left: Pasch's planar line-triangle separation axiom. Right: Deductive proof of Euclid I.21 ray exit E on AC by applying Pasch's Axiom to sub-triangle AMC.",
    )
    # Left panel: Pasch Grundsatz IV
    cv.poly([A0, B0, C0], cls="poly-fill")
    cv.seg(P0, Q0, cls="line-accent")
    cv.dot(A0, "A", dx=-8, dy=16, anchor="end")
    cv.dot(B0, "B", dx=8, dy=16)
    cv.dot(C0, "C", dx=0, dy=-10, anchor="middle")
    cv.dot(hit1, "X₁ (entry)", dx=-10, dy=-8, cls="pt-result", r=4.8, anchor="end")
    cv.dot(hit2, "X₂ (forced exit)", dx=10, dy=6, cls="pt-result", r=4.8)

    # Right panel: Euclid I.21 via Pasch on triangle AMC
    cv.poly([A1, B1, C1], cls="poly-fill")
    cv.poly([A1, M1, C1], cls="poly-accent")
    cv.seg(C1, M1, cls="line-secondary")
    cv.seg(B1, (float((E1.x - (B1.x - E1.x) * sp.Rational(1, 6)).evalf()), float((E1.y - (B1.y - E1.y) * sp.Rational(1, 6)).evalf())), cls="line-result")
    cv.dot(A1, "A", dx=-8, dy=16, anchor="end")
    cv.dot(B1, "B", dx=8, dy=16)
    cv.dot(C1, "C", dx=0, dy=-10, anchor="middle")
    cv.dot(M1, "M", dx=0, dy=18, cls="pt-aux", anchor="middle")
    cv.dot(D1, "D", dx=9, dy=-4, cls="pt-result")
    cv.dot(E1, "E ∈ AC", dx=-10, dy=-6, cls="pt-emerald", r=5.0, anchor="end")

    cv.caption(205, 412, "(a) Pasch § 2 IV. Grundsatz: Entry X₁ forces exit X₂")
    cv.caption(605, 412, "(b) Euclid I.21: Pasch on △AMC forces ray BD to exit AC at E")
    return cv.render()


def build_all_figures(output_dir: Path | None = None) -> list[Path]:
    """Generate all 8 standalone ``.euclid-graphic`` SVG figures in ``docsrc/_static/figures/``."""
    target_dir = output_dir or (get_repo_root() / "docsrc" / "_static" / "figures")
    target_dir.mkdir(parents=True, exist_ok=True)

    specs = [
        ("unit1_ideal_sheaf_perspectivity.svg", _fig1_ideal_sheaf_perspectivity),
        ("unit2_complete_quadrangle_harmonic.svg", _fig2_complete_quadrangle_harmonic),
        ("unit3_polar_conic_self_conjugate.svg", _fig3_polar_conic_self_conjugate),
        ("unit4_addition_of_throws.svg", _fig4_addition_of_throws),
        ("unit4_multiplication_of_throws.svg", _fig5_multiplication_of_throws),
        ("unit4_harmonic_scale_abscissae.svg", _fig6_harmonic_scale_abscissae),
        ("pasch_unit1_linear_betweenness_separation.svg", _fig7_pasch_linear_betweenness_separation),
        ("pasch_unit2_planar_axiom_euclid_gaps.svg", _fig8_pasch_planar_axiom_euclid_gaps),
    ]

    written: list[Path] = []
    for filename, builder in specs:
        svg_text = builder()
        out_path = target_dir / filename
        out_path.write_text(svg_text, encoding="utf-8")
        written.append(out_path)
    return written
