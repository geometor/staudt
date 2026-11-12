:layout: book

.. _geometrie-unit-4-en:

Unit 4: The Algebra of Throws — Addition, Multiplication & Projective Abscissae
===============================================================================

.. rubric:: Karl Georg Christian von Staudt — *Beiträge zur Geometrie der Lage, Zweites Heft* (1857), §§ 19, 20, 29 (arts. 256–269, 403–404)

.. contents:: In This Unit
   :local:
   :depth: 2
   :backlinks: none

.. folio:: § 19
   :page: 166

§ 19. Throws (*Würfe*) and the Straightedge Addition of Throws (arts. 256–267)
------------------------------------------------------------------------------

**Art. 256 (Concept of a Throw).** Four elements $A, B, C, D$ of any :term:`uniform fundamental form <grundgebilde>`, taken in a definite order, determine what we call a :term:`throw <wurf>` (*einen Wurf*), written $(ABCD)$. Two throws $(ABCD)$ and $(A'B'C'D')$ situated in the same or in distinct uniform fundamental forms are **equal** ($(ABCD) = (A'B'C'D')$) when and only when the two forms can be projectively related so that $A, B, C, D$ correspond in order to $A', B', C', D'$.

* A throw in which the first and third elements are harmonically separated by the second and fourth is a **harmonic throw** (*harmonischer Wurf*).
* A throw in which two elements coincide is called a **neutral** (*unentschiedener* or singular) throw: if we fix three distinct gauge elements $P_0$ (*zero element*), $P_1$ (*unit element*), and $P_\infty$ (*horizon element*) on a straight carrier $\ell$, every element $X \in \ell \setminus \{P_\infty\}$ uniquely represents the throw $(P_\infty P_0 P_1 X)$, with $P_0$ representing the **zero throw** and $P_1$ the **unit throw**.

**Art. 259 (Pure Straightedge Addition of Throws — *Summen von Würfen*).** Let $P_0, P_1, P_\infty$ be three fixed distinct elements on a straight carrier $\ell$, and let $X$ and $Y$ be any two elements of $\ell$ distinct from $P_\infty$. To construct their **sum** $S = X + Y$ on $\ell$ using **only an unmarked straightedge**:

1. Through $P_\infty$ draw an arbitrary auxiliary line $m \neq \ell$ and mark upon $m$ two distinct points $U$ and $V$ outside $\ell$.
2. Join $[U P_0]$ and $[V X]$, meeting in $R = [U P_0] \cap [V X]$.
3. Draw the perspective axis $a = [P_\infty R]$ joining $P_\infty$ and $R$.
4. Join $[U Y]$ meeting $a$ in $T = [U Y] \cap a$, and draw $[V T]$ cutting $\ell$ in the required point $S = X + Y$.

.. picture:: /_static/figures/unit4_addition_of_throws.svg
   :alt: Pure straightedge addition of throws S = X + Y via centers U, V collinear with P_inf and perspective axis a = [P_inf R].
   :caption: **Summen von Würfen (1857 § 19, art. 259):** Center line $m = [P_\infty U V]$ and axis $a = [P_\infty R]$ generate the parabolic projectivity $\ell \xrightarrow{U} a \xrightarrow{V} \ell$ fixing $P_\infty$ with double contact and mapping $P_0 \mapsto X$ and $Y \mapsto S = X + Y$.

**Art. 262 (Uniqueness, Commutativity & Associativity of Addition).** Because the composite projectivity $\ell \xrightarrow{U} a \xrightarrow{V} \ell$ has its center-join $[UV]$ and its axis $a$ intersecting at $P_\infty \in \ell$, it induces a parabolic involution-product on $\ell$ with sole fixed point $P_\infty$, uniquely characterized by $P_0 \mapsto X$. By Desargues's theorem in the plane, $S$ is completely independent of the auxiliary line $m$ and centers $U, V$; moreover:

.. math::

   X + P_0 = X, \qquad X + Y = Y + X, \qquad (X + Y) + Z = X + (Y + Z),

and for every $X \neq P_\infty$ there exists a unique opposite element $-X$ satisfying $X + (-X) = P_0$, namely the fourth harmonic conjugate of $X$ with respect to $(P_0, P_\infty)$! In particular, $P_2 = P_1 + P_1$ is the harmonic conjugate making $(P_0, P_2; P_1, P_\infty) = -1$.

.. folio:: § 20
   :page: 174

§ 20. Pure Straightedge Multiplication of Throws (arts. 268–269)
----------------------------------------------------------------

**Art. 268 (*Produkte aus Würfen*).** Retaining the same three gauge points $(P_0, P_1, P_\infty)$ on $\ell$, let $X$ and $Y$ be any elements of $\ell \setminus \{P_0, P_\infty\}$. To construct their **product** $P = X \cdot Y$ using **only an unmarked straightedge**:

1. Through the **zero point** $P_0$ draw an arbitrary auxiliary line $c \neq \ell$ and mark upon $c$ two distinct points $U$ and $V$ outside $\ell$.
2. Join $[U P_1]$ and $[V X]$, meeting in $W = [U P_1] \cap [V X]$.
3. Draw the perspective axis $a = [P_\infty W]$ through the **horizon point** $P_\infty$ and $W$.
4. Join $[U Y]$ meeting $a$ in $Z = [U Y] \cap a$, and draw $[V Z]$ cutting $\ell$ in the required product $P = X \cdot Y$.

.. picture:: /_static/figures/unit4_multiplication_of_throws.svg
   :alt: Pure straightedge multiplication of throws P = X * Y via centers U, V collinear with P_0 and axis a = [P_inf W].
   :caption: **Produkte aus Würfen (1857 § 20, art. 268):** Center line $c = [P_0 U V]$ and axis $a = [P_\infty W]$ generate the hyperbolic projectivity fixing both $P_0$ and $P_\infty$ while mapping $P_1 \mapsto X$ and $Y \mapsto P = X \cdot Y$.

**Art. 269 (Field Laws of the Algebra of Throws).** Because $[UV]$ passes through $P_0$ while $a$ passes through $P_\infty$, the projectivity $\ell \xrightarrow{U} a \xrightarrow{V} \ell$ fixes **both** $P_0$ and $P_\infty$ and is uniquely determined by $P_1 \mapsto X$. Together with addition (§ 19), multiplication satisfies all laws of ordinary algebra (:term:`Rechnung mit Würfen <rechnung-mit-wuerfen>`):

.. math::

   X \cdot P_1 = X, \qquad X \cdot P_0 = P_0, \qquad X \cdot Y = Y \cdot X, \qquad (X \cdot Y) \cdot Z = X \cdot (Y \cdot Z),

.. math::

   X \cdot (Y + Z) = X \cdot Y + X \cdot Z,

and every $X \notin \{P_0, P_\infty\}$ possesses a unique multiplicative inverse $X^{-1}$ constructed by interchanging $P_1$ and $X$ in step 2 ($W' = [U X] \cap [V P_1]$).

.. folio:: § 29
   :page: 255

§ 29. The Harmonic Scale and Projective Abscissae (arts. 403–404)
-----------------------------------------------------------------

**Art. 403.** Repeated addition of the unit element $P_1$ produces on $\ell$ the :term:`harmonic scale <harmonische-reihe>` $P_1, P_2, P_3, \dots, P_n, \dots$, where each consecutive triad $(P_{n-1}, P_n, P_{n+1})$ forms with $P_\infty$ a harmonic tetrad $(P_{n-1}, P_{n+1}; P_n, P_\infty) = -1$. Taking additive inverses yields $P_{-1}, P_{-2}, \dots$, and straightedge division ($P_p \cdot P_q^{-1}$) assigns a unique point $P_{p/q}$ on $\ell$ to every positive and negative rational number $p/q \in \mathbb{Q}$.

.. picture:: /_static/figures/unit4_harmonic_scale_abscissae.svg
   :alt: Projective harmonic scale P_{-1}, P_0, P_1, P_2, P_3, P_4, P_5 converging projectively toward P_inf via pure straightedge quadrangles.
   :caption: **The Harmonic Scale & Projective Abscissae (1857 § 29, arts. 403–404):** Iterated quadrangle reflections generate the exact integer projective scale $P_n$ converging toward the horizon point $P_\infty$ without a single compass circle or ruler graduation.

**Art. 404 (Intrinsic Projective Coordinates Without Measure).** By Dedekind–Cantor continuity along the ordered carrier $\ell$, every real point $X \in \ell \setminus \{P_\infty\}$ is uniquely determined by the cut it induces in the rational harmonic scale and thereby receives an intrinsic real **projective coordinate** or :term:`abscissa <abscisse>` $x$—constructed from **pure incidence and order alone**, prior to any concept of Euclidean length! When $P_\infty$ is subsequently chosen to be the ideal point at infinity of an affine line, von Staudt's projective abscissa specializes directly to the ordinary Cartesian coordinate $x = \frac{\overline{P_0 X}}{\overline{P_0 P_1}}$.
