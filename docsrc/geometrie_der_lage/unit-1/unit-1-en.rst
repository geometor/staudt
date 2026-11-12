:layout: book

.. _geometrie-unit-1-en:

Unit 1: Ideal Elements, Reciprocity & Uniform Fundamental Forms
===============================================================

.. rubric:: Karl Georg Christian von Staudt — *Geometrie der Lage* (1847), *Vorwort* & §§ 1–5 (arts. 1–53)

.. contents:: In This Unit
   :local:
   :depth: 2
   :backlinks: none

.. folio:: Vorwort
   :page: iii

Preface (*Vorwort*, Nuremberg, August 1847)
-------------------------------------------

In modern times :term:`Geometrie der Lage <geometrie-der-lage>` (*Geometry of Position*) has rightly been distinguished from the *Geometry of Magnitude* (*Geometrie des Maßes*); nevertheless, propositions in which no magnitude whatever is mentioned have commonly still been proved by means of considerations of ratio and distance. I have therefore attempted in the present treatise to make the Geometry of Position an autonomous science that stands in no need of measurement.

So that the reader may survey uninterruptedly the genuine nexus among the properties of figures that belong solely to position, I have rigorously excluded every metrical relation—length of a segment, amplitude of an angle, area, or arithmetic cross-ratio—and derived every construction and theorem from pure incidence, continuity of order, and :term:`reciprocity <reciprocitaet>`.

.. folio:: § 1
   :page: 1

§ 1. Space, Surfaces, Lines, and Points (arts. 1–15)
----------------------------------------------------

**Art. 1.** Geometry treats of space and of spatial configurations: bodies, surfaces, lines, and points. Every body is bounded by surfaces; two adjacent portions of a surface meet along a line; two adjacent portions of a line meet in a point. Conversely, a moving point generates a line, a moving line (not sliding strictly along itself) generates a surface, and a moving surface generates a spatial region.

**Art. 4.** Among all lines, the *straight line* (*die Gerade*) is uniquely determined by any two of its points: through two distinct points $A$ and $B$ passes one and only one straight line $[AB]$. Two distinct straight lines cannot have more than one point in common.

**Art. 7.** Among all surfaces, the *plane* (*die Ebene*) possesses the property that every straight line joining any two of its points lies wholly within the surface. Three points $A, B, C$ not lying in one straight line determine one and only one plane $ABC$; equally, a straight line and an external point, or two intersecting straight lines, determine a unique plane.

**Art. 11.** Two distinct planes that meet share an entire straight line in common, for if they share one point they cannot terminate there without cutting across one another along a one-dimensional locus, which by planar flatness lies wholly as a straight line in both planes.

.. folio:: § 2
   :page: 7

§ 2. Parallelism and Infinitely Distant Elements (arts. 16–22)
--------------------------------------------------------------

**Art. 16.** All straight lines in space that are parallel to a given straight line $g$ share a common *direction* (*Richtung*). Two parallel lines lie in a common plane and meet nowhere in finite space; three lines parallel to one and the same line are mutually parallel and form an axial sheaf of parallels (*Parallelstrahlenbündel*).

**Art. 18.** Because all lines of a parallel sheaf behave toward planes and external points in strict analogy with all lines passing through an ordinary point—every external point $P$ determines with the sheaf a unique ray through $P$ belonging to the sheaf, and every non-parallel plane cuts every ray of the sheaf—we adjoin to each parallel sheaf a single :term:`infinitely distant point <unendlich-fernes-element>` (*unendlich ferner Punkt* or ideal point $P_\infty$) through which all lines of that direction pass.

**Art. 20.** All infinitely distant points of the straight lines lying in one plane $\alpha$ constitute a single *infinitely distant straight line* (*unendlich ferne Gerade* $g_\infty$) of $\alpha$; parallel planes share the exact same infinitely distant line. And the totality of all infinitely distant points and lines of three-dimensional space constitutes a single *infinitely distant plane* (*unendlich ferne Ebene* $\omega_\infty$), cut by every ordinary plane along its ideal line.

**Art. 22.** Through this completion of space, every exception arising from parallelism disappears at a stroke:

1. Two distinct points (proper or ideal) determine one and only one straight line.
2. Two distinct coplanar straight lines share one and only one point.
3. Two distinct planes share one and only one straight line.
4. A plane and a straight line not lying in it share one and only one point.

.. picture:: /_static/figures/unit1_ideal_sheaf_perspectivity.svg
   :alt: Central projection from S mapping carrier line l onto tilted line m, sending the ideal point P_inf of l to the finite vanishing point I_m on m.
   :caption: **Ideal Elements Under Perspectivity (1847 §§ 2 & 5):** Central projection from $S$ maps points $A, B, C$ of $\ell$ onto $A', B', C'$ of $m$, while the ray through $S$ parallel to $\ell$ sends $\ell$'s ideal point $P_\infty$ to the ordinary vanishing point $I_m \in m$.

.. folio:: §§ 3–5
   :page: 13

§§ 3–5. The Law of Reciprocity and Uniform Fundamental Forms (arts. 23–53)
--------------------------------------------------------------------------

**Art. 25 (§ 3).** Once ideal elements are adjoined, all fundamental incidence propositions of three-dimensional space exhibit an exact **Law of Reciprocity** (:term:`Gesetz der Reciprocität <reciprocitaet>`): every theorem remains valid when the words *point* and *plane* are interchanged throughout while *straight line* remains unchanged (*join of two points* $\leftrightarrow$ *intersection of two planes*; *collinear points* $\leftrightarrow$ *coaxial planes*). Within a single fixed plane, *point* and *straight line* exchange roles directly.

**Art. 36 (§ 4).** Every closed projective straight line is a single returning cycle (*geschlossene Linie*): a single point $A$ does not divide the projective line into two severed halves, because one may pass from one side of $A$ to the other through $P_\infty$. Two distinct points $A$ and $B$ divide the entire projective line into two complementary segments; two pairs $(A, B)$ and $(C, D)$ are :term:`mutually separating <getrennte-paare>` when each segment bounded by $A, B$ contains one point of $(C, D)$.

**Art. 45 (§ 5).** Geometry builds all higher projective configurations out of three **Uniform Fundamental Forms** (:term:`einförmige Grundgebilde <grundgebilde>`) of the first grade:

1. The **rectilinear range of points** (*gerades Gebilde*): all points incident with a fixed carrier line $\ell$.
2. The **flat pencil of rays** (*ebenes Strahlbüschel*): all coplanar straight lines passing through a fixed vertex $S$ in a plane $\alpha$.
3. The **axial pencil of planes** (*Ebenenbüschel*): all planes passing through a fixed axis $g$.

Two such fundamental forms are in **perspective position** (*perspektivische Lage*) when one is a section or projection of the other—for instance, when every ray of a flat pencil $(S)$ passes through the corresponding point of a range $(\ell)$ not incident with $S$.
