:layout: book
:canonical_id: § 19
:breadcrumb_title: § 19
:order: 1
:folio: § 19
:tracks: English: index | German: de | Summary: summary | Notes: notes

.. _beitraege-sec_19-en:
.. _beitraege-sec_19:
.. _beitraege-sec-19-en:
.. _beitraege-sec-19:
.. _geometrie-unit-4-en:

.. folio:: § 19
   :page: 166

§ 19. The Concept and Addition of Throws (arts. 256–267)
========================================================

.. rubric:: Karl Georg Christian von Staudt — *Beiträge, Zweites Heft* (1857), § 19 (arts. 256–267)

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

.. toctree::
   :hidden:

   de
   summary
   notes
