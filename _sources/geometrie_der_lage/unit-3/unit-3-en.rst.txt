:layout: book

.. _geometrie-unit-3-en:

Unit 3: Involutions, Planar Polar Systems & Order Curves (Conics)
=================================================================

.. rubric:: Karl Georg Christian von Staudt — *Geometrie der Lage* (1847), §§ 9 & 18–19 (arts. 103–115, 235–257)

.. contents:: In This Unit
   :local:
   :depth: 2
   :backlinks: none

.. folio:: § 9
   :page: 49

§ 9. Involutions on Uniform Fundamental Forms (arts. 103–115)
-------------------------------------------------------------

**Art. 103.** When a non-identical projectivity of a uniform fundamental form onto itself interchanges even a **single** pair of distinct elements ($A \mapsto A'$ and $A' \mapsto A$), it interchanges **every** element with its image ($X \leftrightarrow X'$) and is called an **involution** (*Involution*).

*Proof.* By the Fundamental Theorem (Art. 96), a projectivity is uniquely determined by three pairs of corresponding elements. Consider the given projectivity $\tau$ sending $(A, A', B) \mapsto (A', A, B')$ together with its inverse $\tau^{-1}$, which sends $(A', A, B') \mapsto (A, A', B)$. On the projective carrier, the ordered tetrad $(A, A', B, B')$ is projectively equivalent to $(A', A, B', B)$ via the quadrangle interchange of conjugate pairs (§ 6, Art. 72)! Hence $(A, A', B) \mapsto (A', A, B')$ also carries $B' \mapsto B$, so $\tau = \tau^{-1}$ everywhere. $\blacksquare$

**Art. 106 ( Quadrangle Theorem of Desargues–Staudt ).** The three pairs of opposite sides of any :term:`complete plane quadrangle <vollstaendiges-viereck>` $EFGH$ are cut by every transversal $\ell$ not passing through a vertex in three pairs of an involution.

**Art. 109 (Hyperbolic and Elliptic Involutions).** Two distinct pairs $(A, A')$ and $(B, B')$ uniquely determine an involution:

1. If $(A, A')$ and $(B, B')$ **do not** :term:`separate one another <getrennte-paare>`, the involution is *hyperbolic* and possesses exactly **two real double elements** (*Ordnungselemente* $M, N$), which are simultaneously harmonic conjugates with respect to **every** conjugate pair $(X, X')$ of the involution: $(M, N; X, X') = -1$.
2. If $(A, A')$ and $(B, B')$ **do** separate one another, corresponding points traverse the closed carrier in the same cyclical sense and never meet; the involution is *elliptic* and possesses **no real double elements** *(in 1856 Beiträge Heft 1, von Staudt represents a pair of conjugate imaginary points synthetically as an elliptic involution equipped with a cyclical sense!)*.

.. folio:: §§ 18–19
   :page: 129

§§ 18–19. Planar Polar Systems and Order Curves (arts. 235–257)
---------------------------------------------------------------

**Art. 235 (§ 18 — Planar Polarity).** A reciprocal correspondence (*Reciprocität* or correlation) in a plane assigns to every point $P$ a unique straight line $p = \pi(P)$ and to every straight line $g$ a unique point $G = \pi(g)$ such that collinear points correspond to concurrent lines and harmonic tetrads of points correspond to harmonic pencils of four rays. When this correspondence is *involutory*—so that whenever $Q$ lies on the line $\pi(P)$, $P$ likewise lies on the line $\pi(Q)$—it is called a **planar polar system** (:term:`ebenes Polarsystem <polarsystem>`), $P$ is the **pole** (*Pol*) of $p$, and $p$ is the **polar** (*Polare*) of $P$.

**Art. 238.** Three points $A, B, C$, each of which is the pole of the opposite side ($a = [BC], b = [CA], c = [AB]$), form a **polar triangle** (*Polardreieck* or self-polar triangle). A planar polar system is uniquely determined by a polar triangle $ABC$ together with one additional pole–polar pair $(P, p)$ in general position.

**Art. 242 (§ 19 — Von Staudt's Intrinsic Definition of Conics).** In a planar polar system $\pi$, either no point lies upon its own polar (*elliptic polar system*), or infinitely many points lie upon their own polars (*hyperbolic polar system*). In the latter case:

* The locus of all points $X$ of the plane that lie upon their own polars ($X \in \pi(X)$) is called a **curve of the second order** or **order curve** (:term:`Ordnungscurve <ordnungscurve>` — a point-conic).
* Dually, the envelope of all straight lines $x$ of the plane that pass through their own poles ($\pi(x) \in x$) is a **curve of the second class** (*Hüllcurve* — the tangent-conic of the exact same curve).

.. picture:: /_static/figures/unit3_polar_conic_self_conjugate.svg
   :alt: Planar polar system defining a conic section as the self-conjugate locus X in pi(X), with exterior pole P, polar p = [T1 T2], and harmonic secant (T_A, T_B; P, Q) = -1.
   :caption: **Von Staudt's Polar Definition of the Conic (§§ 18–19, arts. 235–249):** The conic $\mathcal{C}$ is defined purely as the locus of self-incident points $X \in \pi(X)$. From an exterior pole $P$, the polar $p = [T_1 T_2]$ joins the contact points of the self-conjugate tangents, and every secant through $P$ is cut harmonically: $(T_A, T_B; P, Q) = -1$.

**Art. 245.** Every straight line $g$ in the plane meets an order curve $\mathcal{C}$ in **at most two points** (namely the double points, if real, of the involution of conjugate points induced by $\pi$ upon $g$):

* If the induced involution on $g$ is elliptic, $g$ is an *exterior line* (*Sekantenlose*) meeting $\mathcal{C}$ in zero real points.
* If $g$ lies on its own pole $T = \pi(g)$, the involution degenerates at $T$: $g$ meets $\mathcal{C}$ in the **single contact point** $T$ and is the **tangent** to $\mathcal{C}$ at $T$.
* If the induced involution on $g$ is hyperbolic with double points $T_A, T_B \in \mathcal{C}$, $g$ is a **secant** cutting $\mathcal{C}$ in $T_A$ and $T_B$, and every pair of conjugate points $(P, Q)$ on $g$ divides $(T_A, T_B)$ harmonically: $(T_A, T_B; P, Q) = -1$.

**Art. 253 (Steiner's Generation & Pascal–Brianchon Duality as Corollaries).** Because the pencil of rays joining a variable point $X \in \mathcal{C}$ to two fixed points $A, B \in \mathcal{C}$ corresponds projectively to the range of intersections of the polar $\pi(X)$ (the tangent at $X$) with the fixed tangents at $A$ and $B$, :person:`Steiner <steiner>`'s projective pencil generation of conics, :person:`Pascal <pascal>`'s inscribed Hexagon Theorem, and :person:`Brianchon <brianchon>`'s circumscribed Hexagon Theorem follow immediately without a single cone in three-space or quadratic equation!
