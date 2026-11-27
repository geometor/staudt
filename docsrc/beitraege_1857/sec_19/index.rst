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

**Art. 256 (Concept of a Throw).** Four elements :math:`A, B, C, D` of any :term:`uniform fundamental form <grundgebilde>`, taken in a definite order, determine what we call a :term:`throw <wurf>` (*einen Wurf*), written :math:`(ABCD)`. Two throws :math:`(ABCD)` and :math:`(A'B'C'D')` situated in the same or in distinct uniform fundamental forms are **equal** (:math:`(ABCD) = (A'B'C'D')`) when and only when the two forms can be projectively related so that :math:`A, B, C, D` correspond in order to :math:`A', B', C', D'`.

* A throw in which the first and third elements are harmonically separated by the second and fourth is a **harmonic throw** (*harmonischer Wurf*).
* A throw in which two elements coincide is called a **neutral** (*unentschiedener* or singular) throw: if we fix three distinct gauge elements :math:`P_0` (*zero element*), :math:`P_1` (*unit element*), and :math:`P_\infty` (*horizon element*) on a straight carrier :math:`\ell`, every element :math:`X \in \ell \setminus \{P_\infty\}` uniquely represents the throw :math:`(P_\infty P_0 P_1 X)`, with :math:`P_0` representing the **zero throw** and :math:`P_1` the **unit throw**.

**Art. 259 (Pure Straightedge Addition of Throws — *Summen von Würfen*).** Let :math:`P_0, P_1, P_\infty` be three fixed distinct elements on a straight carrier :math:`\ell`, and let :math:`X` and :math:`Y` be any two elements of :math:`\ell` distinct from :math:`P_\infty`. To construct their **sum** :math:`S = X + Y` on :math:`\ell` using **only an unmarked straightedge**:

1. Through :math:`P_\infty` draw an arbitrary auxiliary line :math:`m \neq \ell` and mark upon :math:`m` two distinct points :math:`U` and :math:`V` outside :math:`\ell`.
2. Join :math:`[U P_0]` and :math:`[V X]`, meeting in :math:`R = [U P_0] \cap [V X]`.
3. Draw the perspective axis :math:`a = [P_\infty R]` joining :math:`P_\infty` and :math:`R`.
4. Join :math:`[U Y]` meeting :math:`a` in :math:`T = [U Y] \cap a`, and draw :math:`[V T]` cutting :math:`\ell` in the required point :math:`S = X + Y`.

.. picture:: /_static/figures/unit4_addition_of_throws.svg
   :alt: Pure straightedge addition of throws S = X + Y via centers U, V collinear with P_inf and perspective axis a = [P_inf R].
   :caption: **Summen von Würfen (1857 § 19, art. 259):** Center line :math:`m = [P_\infty U V]` and axis :math:`a = [P_\infty R]` generate the parabolic projectivity :math:`\ell \xrightarrow{U} a \xrightarrow{V} \ell` fixing :math:`P_\infty` with double contact and mapping :math:`P_0 \mapsto X` and :math:`Y \mapsto S = X + Y`.

**Art. 262 (Uniqueness, Commutativity & Associativity of Addition).** Because the composite projectivity :math:`\ell \xrightarrow{U} a \xrightarrow{V} \ell` has its center-join :math:`[UV]` and its axis :math:`a` intersecting at :math:`P_\infty \in \ell`, it induces a parabolic involution-product on :math:`\ell` with sole fixed point :math:`P_\infty`, uniquely characterized by :math:`P_0 \mapsto X`. By Desargues's theorem in the plane, :math:`S` is completely independent of the auxiliary line :math:`m` and centers :math:`U, V`; moreover:

.. math::

   X + P_0 = X, \qquad X + Y = Y + X, \qquad (X + Y) + Z = X + (Y + Z),

and for every :math:`X \neq P_\infty` there exists a unique opposite element :math:`-X` satisfying :math:`X + (-X) = P_0`, namely the fourth harmonic conjugate of :math:`X` with respect to :math:`(P_0, P_\infty)`! In particular, :math:`P_2 = P_1 + P_1` is the harmonic conjugate making :math:`(P_0, P_2; P_1, P_\infty) = -1`.

.. toctree::
   :hidden:

   de
   summary
   notes
