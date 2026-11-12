:layout: book

.. _geometrie-unit-2-en:

Unit 2: The Complete Quadrangle, Harmonic Separation & Projectivity
===================================================================

.. rubric:: Karl Georg Christian von Staudt — *Geometrie der Lage* (1847), §§ 6–8 (arts. 66–98)

.. contents:: In This Unit
   :local:
   :depth: 2
   :backlinks: none

.. folio:: § 6
   :page: 29

§ 6. Complete Plane Quadrangles and Harmonic Forms (arts. 66–74)
----------------------------------------------------------------

**Art. 66.** Four points $E, F, G, H$ lying in one plane, no three of which are collinear, determine six connecting lines called *sides* (*Seiten*), which group into three pairs of *opposite sides*:

.. math::

   ([EF], [GH]), \qquad ([FG], [HE]), \qquad ([EG], [FH]).

Such a configuration is called a :term:`complete plane quadrangle <vollstaendiges-viereck>` (*vollständiges ebenes Viereck*), and the three points in which its three pairs of opposite sides meet are called its **diagonal points** (*Diagonalpunkte*). Dually, four coplanar lines, no three concurrent, form a *complete plane quadrilateral* (*vollständiges ebenes Vierseit*) having six vertices grouped into three opposite pairs joined by three *diagonals*.

**Art. 67.** Let a straight carrier line $\ell$ pass through two diagonal points $A = [EF] \cap [GH]$ and $B = [FG] \cap [HE]$ of a complete plane quadrangle $EFGH$, and let the remaining two opposite sides $[EG]$ and $[FH]$ meet $\ell$ in $C$ and $D$ respectively. Then the four collinear points $A, C, B, D$ are called **four harmonic points** (:term:`harmonisches Gebilde <harmonisches-gebilde>`), and $D$ is called the **fourth harmonic point** (*der vierte harmonische Punkt*) to $A, B, C$, conjugate to $C$ with respect to the pair $(A, B)$.

.. picture:: /_static/figures/unit2_complete_quadrangle_harmonic.svg
   :alt: Complete plane quadrangle EFGH cutting carrier line l in harmonic tetrad (A, B; C, D) = -1.
   :caption: **Pure Straightedge Harmonic Fourth (1847 § 6, art. 67 & § 8, art. 93):** Given collinear $A, B, C$, choose $E$ off $\ell$ and $G$ on $[CE]$, intersect $F = [AE] \cap [BG]$ and $H = [BE] \cap [AG]$, and draw $[FH]$ cutting $\ell$ in the unique harmonic fourth $D$.

**Art. 70 (Spatial Proof of Uniqueness).** *Given three distinct collinear points $A, B, C$, the fourth harmonic point $D$ constructed by a complete plane quadrangle $EFGH$ depends solely upon $A, B, C$ and is entirely independent of the choice of the plane and of the quadrangle.*

*Proof.* Suppose first that a second quadrangle $E'F'G'H'$ lies in a **different plane** $\alpha'$ passing through the same carrier line $\ell = [AB]$, with $[E'F'] \cap [G'H'] = A$, $[F'G'] \cap [H'E'] = B$, and $[E'G']$ passing through $C$. Because $[EG]$ and $[E'G']$ meet at $C$, the lines $[EE']$ and $[GG']$ lie in one plane and meet at a spatial center $S$ outside both $\alpha$ and $\alpha'$. Projecting $\alpha$ onto $\alpha'$ from $S$:

* Plane $SEE'A$ meets $\alpha'$ in $[AE']$, and plane $SGG'B$ meets $\alpha'$ in $[BG']$; since $F = [AE] \cap [BG]$, ray $[SF]$ passes through $F' = [AE'] \cap [BG']$.
* Likewise ray $[SH]$ passes through $H' = [BE'] \cap [AG']$.
* Therefore the plane $SFH$ contains both $[FH]$ and $[F'H']$, so both lines meet the common intersection line $\ell = \alpha \cap \alpha'$ in the **exact same point** $D = D'$.

If a third quadrangle $E''F''G''H''$ lies in the **same** plane $\alpha$ as $EFGH$, both yield the same point $D$ as the auxiliary quadrangle $E'F'G'H'$ in the second plane $\alpha'$, hence $D'' = D' = D$. $\blacksquare$

**Art. 72.** In every harmonic tetrad $(A, B; C, D)$, the roles of the two conjugate pairs $(A, B)$ and $(C, D)$ are completely symmetric, and within each pair the two elements may be interchanged; moreover, $(A, B)$ and $(C, D)$ invariably :term:`separate one another <getrennte-paare>`.

.. folio:: §§ 7–8
   :page: 38

§§ 7–8. Perspectivity, Projectivity & the Fundamental Theorem (arts. 75–98)
---------------------------------------------------------------------------

**Art. 76 (§ 7).** Every perspective projection between a range of points and a flat pencil of rays, or between two ranges, carries every harmonic tetrad into a harmonic tetrad; for the four projecting planes or rays from an external center carry a complete quadrangle directly into a corresponding harmonic configuration.

**Art. 93 (§ 8 — Pure Synthetic Definition of Projectivity).** Two :term:`uniform fundamental forms <grundgebilde>` are called **projectively related** (:term:`projektivisch <projektivisch>`) when their elements are placed in one-to-one correspondence so that **to every four harmonic elements of the one correspond four harmonic elements of the other**.

**Art. 96 (Fundamental Theorem of Projective Geometry).** *A projectivity between two uniform fundamental forms is uniquely and completely determined as soon as three distinct elements $A, B, C$ of the first form are assigned to three arbitrary distinct elements $A', B', C'$ of the second form.*

For from $A, B, C$ the fourth harmonic $D_1$ is uniquely determined by straightedge alone, and from any triad among $\{A, B, C, D_1\}$ further harmonic points $D_2, D_3, \dots$ are generated in an everywhere dense :term:`harmonic net <harmonische-reihe>`, each of whose images $D'_k$ is uniquely forced by the corresponding quadrangle construction on $A', B', C'$. Hence if a projectivity fixes three distinct elements of one and the same carrier, it fixes **every** element of that carrier identically.
