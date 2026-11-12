:layout: book

.. _pasch-unit-2-en:

Unit 2: Pasch's Planar Separation Axiom, Ideal Sheaves & the Deductive Manifesto
================================================================================

.. rubric:: Moritz Pasch — *Vorlesungen über neuere Geometrie* (1882), § 2 (pp. 17–27), §§ 8–11 (pp. 58–93) & § 12 (pp. 93–100)

.. contents:: In This Unit
   :local:
   :depth: 2
   :backlinks: none

.. folio:: § 2
   :page: 17

§ 2. On the Plane and Pasch's Planar Separation Axiom (pp. 17–27)
-----------------------------------------------------------------

**Grundsatz I.** *Through any three points one can always lay a planar surface.*

**Grundsatz II.** *If two points of a straight segment belong to a planar surface (appropriately prolonged), then every interior point of the straight segment belongs to the planar surface.*

**Grundsatz III.** *If two planar surfaces share a common point, one can always specify at least a second point common to both.*

**Grundsatz IV (Pasch's Planar Separation Axiom, p. 21).** *Let $A, B, C$ be three points not lying in one straight line, and let $a$ be a straight line lying in the plane $ABC$ that passes through none of the points $A, B, C$: if the straight line $a$ passes through a point inside the segment $AB$, then it always passes also either through a point inside the segment $AC$ or through a point inside the segment $BC$.*

.. picture:: /_static/figures/pasch_unit2_planar_axiom_euclid_gaps.svg
   :alt: Pasch's IV. Grundsatz (1882 p. 21) on triangle ABC and deductive proof of Euclid I.21 ray exit E on AC.
   :caption: **Pasch's IV. Grundsatz (1882 § 2, p. 21) & 10. Lehrsatz (p. 25):** Left: Any coplanar line $\ell$ entering $\triangle ABC$ along open segment $AB$ without meeting $A, B, C$ must exit through open segment $AC$ or $BC$ (never both). Right: Applying *Grundsatz IV* to sub-triangle $\triangle AMC$ proves Euclid ``I.21``'s interior ray exit $E \in AC$.

**10. Lehrsatz (Exclusivity — A Line Cannot Cut All Three Open Sides, p. 25).** *In the configuration of Grundsatz IV, the straight line $a$ cannot pass simultaneously through a point inside $AB$, a point inside $BC$, and a point inside $AC$.*

*Proof.* Suppose for contradiction that $a$ met open segments $AB$, $BC$, and $AC$ in interior points $D, E, F$ respectively. Being three distinct collinear points on $a$, one of them—say $F$—must by § 1 lie inside the segment $DE$ bounded by the other two ($D\text{--}F\text{--}E$). Now consider triangle $\triangle BDE$ and the straight line $g = [AC]$:

* Line $g$ passes through none of the vertices $B, D, E$ (since $D$ is interior to $AB$ and $E$ is interior to $BC$).
* Line $g$ passes through $F$, which lies **inside** side $DE$ of $\triangle BDE$.
* Therefore, by **Grundsatz IV** applied to $\triangle BDE$, line $g = [AC]$ would have to meet either segment $BD$ internally (impossible, since $[AC] \cap [AB] = A$ lies *outside* $BD$ by § 1 Grundsatz III) or segment $BE$ internally (equally impossible, since $[AC] \cap [BC] = C$ lies *outside* $BE$)!

Hence a line avoiding $A, B, C$ that enters one open side of $\triangle ABC$ exits through **one and only one** of the other two open sides, and every straight line $a$ in a plane $\alpha$ partitions $\alpha \setminus a$ into **two** disjoint convex half-planes (*Halbebenen*): $P, Q \notin a$ lie on the *same side* of $a$ iff segment $PQ$ misses $a$, and on *opposite sides* iff $a$ meets segment $PQ$ internally. $\blacksquare$

.. folio:: §§ 8–11
   :page: 58

§§ 8–11. Ideal Sheaves Without Infinity & Harmonic Figures (pp. 58–93)
----------------------------------------------------------------------

**§ 8. Sheaves of Lines and Ideal Points (*Strahlenbündel und uneigentliche Punkte*).** In :person:`von Staudt <staudt>`'s *Geometrie der Lage* (§ 2), infinitely distant points were introduced by invoking Euclidean parallel directions—thereby relying on Euclid's Parallel Postulate and speaking figuratively of points "at infinity." Yet in actual observation we operate only within a **bounded spatial region**, where two coplanar lines $g, h$ may fail to intersect inside our region whether they are Euclidean parallels or merely converge far outside our region!

We therefore replace "points at infinity" by a rigorous finite construction:

1. Two coplanar lines $g, h$ together with any external point $S$ outside their plane determine two planes $(S, g)$ and $(S, h)$ intersecting along a unique ray $k$ through $S$. The totality of all such lines $k$ determined across space forms a **sheaf of rays** (*Strahlenbündel*).
2. If $g$ and $h$ meet in an ordinary point $P$, the sheaf consists simply of all lines through $P$ (*eigentliches Bündel*). If $g$ and $h$ do not meet, the sheaf is still completely determined by finite plane intersections (*uneigentliches Bündel*)—without ever assuming whether parallels are unique!
3. Calling **every** sheaf of rays a *projective point* (*Punkt im weiteren Sinne*), every planar flat pencil a *projective line*, and every planar sheaf a *projective plane*, all incidence axioms of three-dimensional projective geometry hold **unconditionally and without appeal to infinity**.

**§§ 10–11. Complete Quadrangle & Harmonic Separation Grounded on Order.** Armed with ideal sheaves (§§ 8–9) and planar separation (§ 2), :person:`von Staudt <staudt>`'s :term:`complete quadrangle <vollstaendiges-viereck>` construction (§ 6) now rests on complete logical foundations: using *Grundsatz IV* repeatedly across the four sub-triangles of quadrangle $EFGH$, one proves **purely deductively** (without glancing at a figure!) that the harmonic conjugates $(A, B)$ and $(C, D)$ invariably :term:`separate one another <getrennte-paare>` on the projective line.

.. folio:: § 12
   :page: 93

§ 12. The Hypothetico-Deductive Manifesto (pp. 93–100)
------------------------------------------------------

Looking back over the edifice erected from §§ 1–11, we recognize the strict logical law that governs every genuinely deductive mathematical science (*p. 98*):

.. pull-quote::

   *"Indeed, if geometry is to be genuinely deductive, the process of inference must everywhere be independent of the meaning of the geometrical concepts, just as it must be independent of the diagrams; only the relations among the geometrical concepts laid down in the propositions and definitions employed may be taken into account. During the deduction it is certainly permissible and useful, though in no way necessary, to think of the meaning of the geometrical concepts appearing therein; in fact, precisely when this becomes necessary does a gap become manifest in the deduction and, when the gap cannot be eliminated by modifying the reasoning, the insufficiency of the propositions invoked as tools of proof."*

Whenever a classical proof appears to succeed only when we picture what "straight segment" or "interior" looks like in a drawing, an **unstated axiom** is hiding in our visual intuition. Once all :term:`nuclear propositions <stammsaetze>` (*Stammsätze*) are explicitly recorded at the threshold of the science:

* Every mathematical proof reduces to purely formal logical transformation of the stated relational hypotheses; and
* Every valid theorem admits an immediate **dual or structural reinterpretation** (such as projective :term:`reciprocity <reciprocitaet>` between points and planes, or algebraic coordinate models) simply by substituting any new system of objects that satisfies the exact same formal relations!
