:layout: book

.. _pasch-unit-1-en:

Unit 1: Grounding Geometry & Linear Betweenness
===============================================

.. rubric:: Moritz Pasch — *Vorlesungen über neuere Geometrie* (1882), *Vorwort*, *Einleitung* & § 1 (pp. 1–17)

.. contents:: In This Unit
   :local:
   :depth: 2
   :backlinks: none

.. folio:: Vorwort & Einleitung
   :page: 1

Preface & Introduction (*Vorwort & Einleitung*, Giessen, 1882)
--------------------------------------------------------------

Modern projective geometry—elevated by :person:`Karl Georg Christian von Staudt <staudt>` into an autonomous science independent of measurement—still leaves unexamined a multitude of elementary assumptions concerning the relative order of points on a straight line and the separation of regions in a plane. Even in :person:`Euclid <euclid>`'s :cite:`*Elements* <euclid:elements>`, proofs continually rely upon facts read tacitly off a drawn figure rather than deduced from explicitly stated principles.

To place geometry upon an unassailable deductive foundation, we must separate two tasks strictly:

1. First, isolate the irreducible :term:`primitive concepts <stammbegriffe>` (*Stammbegriffe*: **point**, **straight segment** *gerade Strecke*, **planar surface** *ebene Fläche*, and later congruence) and state **every** empirical observation required of them in a closed list of :term:`nuclear propositions <stammsaetze>` (*Grundsätze* or *Stammsätze*).
2. Second, derive every subsequent concept (such as the full straight line, the ray, the entire plane, and ideal projective sheaves) and every theorem (*Lehrsatz*) by pure logical inference alone, without ever consulting sensible intuition or figures again.

Notice that in immediate physical observation we never encounter an infinite straight line, but only a bounded **straight segment** joining two endpoints $A$ and $B$, together with **points lying interior to the segment** (*Punkte innerhalb der Strecke*, i.e., points lying :term:`between <zwischen>` $A$ and $B$).

.. folio:: § 1
   :page: 4

§ 1. On the Straight Line (*Von der geraden Linie*, pp. 4–17)
-------------------------------------------------------------

**Grundsatz I.** *Between two distinct points one can always draw a straight segment, and indeed only one.*

We denote the straight segment joining $A$ and $B$ by $AB$ or $BA$; $A$ and $B$ are its *endpoints* (*Endpunkte*). A statement "$C$ lies within segment $AB$" means that $C$ lies **between** (:term:`zwischen <zwischen>`) $A$ and $B$.

**Grundsatz II.** *One can always specify a point that lies inside a given straight segment.*

**Grundsatz III.** *If the point $C$ lies inside the segment $AB$, then the point $A$ lies outside the segment $BC$.*

**Grundsatz IV.** *If the point $C$ lies inside the segment $AB$, then all points of the segment $AC$ belong also to the segment $AB$.*

**Grundsatz V.** *If the point $C$ lies inside the segment $AB$, then a point belonging to neither segment $AC$ nor segment $BC$ cannot belong to segment $AB$ (save $C$ itself).*

*(From Grundsätze I–V follow immediately the partition and transitivity laws of open interior segments: if $C$ lies between $A$ and $B$, and $D$ lies between $A$ and $C$, then $D$ lies between $A$ and $B$ while $C$ lies between $D$ and $B$.)*

**Grundsatz VI (Segment Prolongation).** *If $A$ and $B$ are arbitrary distinct points, one can always choose a point $C$ in such a way that $B$ lies inside the segment $AC$.*

**Grundsatz VII (Uniqueness of Prolongation).** *If the point $B$ lies inside both the segment $AC$ and the segment $AD$, then either $C$ coincides with $D$, or $C$ lies inside $BD$, or $D$ lies inside $BC$.*

**Grundsatz VIII (Disjointness of Distinct Lines).** *If $B$ lies inside $AC$ and $A$ lies inside $B'C$, while $B$ and $B'$ do not belong to the same straight line with $A$, no contradiction arises; on a single straight line, two distinct straight lines cannot share two distinct points.*

.. picture:: /_static/figures/pasch_unit1_linear_betweenness_separation.svg
   :alt: Moritz Pasch's linear betweenness axioms (Grundsaetze I-VIII) for open segments AB and four-point separation of collinear pairs.
   :caption: **Pasch's Nuclear Axioms of Linear Betweenness (1882 § 1, pp. 4–16):** Bounded segments $AB$, interior density ($C$ between $A$ and $B$), prolongation ($B$ between $A$ and $D$), and linear partition of four collinear points into a unique ordered quadruple $A\text{--}C\text{--}B\text{--}D$.

**Definition of the Full Straight Line (*Gerade*).** Given two distinct points $A$ and $B$, the **straight line** $[AB]$ consists of:

1. the endpoints $A$ and $B$,
2. all points $X$ lying *inside* segment $AB$ ($A\text{--}X\text{--}B$),
3. all points $Y$ such that $B$ lies inside $AY$ ($A\text{--}B\text{--}Y$), and
4. all points $Z$ such that $A$ lies inside $ZB$ ($Z\text{--}A\text{--}B$).

**Lehrsätze 1–23 (Selected Deductive Consequences on the Line).**

* **Lehrsatz 4.** Every straight line $[AB]$ is uniquely determined by **any two** distinct points lying upon it.
* **Lehrsatz 12 (Ray Separation by a Single Point).** Any point $O$ on a straight line $g$ divides all remaining points of $g$ into **two** non-empty classes (*Halbstrahlen* or opposite rays): two points $P, Q \neq O$ lie on the *same side* of $O$ when $O$ does **not** lie inside $PQ$, and on *opposite sides* of $O$ when $O$ **does** lie inside $PQ$.
* **Lehrsatz 19 (Four-Point Linear Order Theorem).** Given any **four** distinct collinear points, they can always be lettered in a unique way (up to reversal) as $A, B, C, D$ such that $B$ lies both between $A, C$ and between $A, D$, while $C$ lies both between $A, D$ and between $B, D$.
