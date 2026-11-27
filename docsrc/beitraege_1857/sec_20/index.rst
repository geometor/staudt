:layout: book
:canonical_id: § 20
:breadcrumb_title: § 20
:order: 2
:folio: § 20
:tracks: English: index | German: de | Summary: summary | Notes: notes

.. _beitraege-sec_20-en:
.. _beitraege-sec_20:
.. _beitraege-sec-20-en:
.. _beitraege-sec-20:

.. folio:: § 20
   :page: 174

§ 20. Pure Straightedge Multiplication of Throws (arts. 268–269)
================================================================

.. rubric:: Karl Georg Christian von Staudt — *Beiträge, Zweites Heft* (1857), § 20 (arts. 268–269)

**Art. 268 (*Produkte aus Würfen*).** Retaining the same three gauge points :math:`(P_0, P_1, P_\infty)` on :math:`\ell`, let :math:`X` and :math:`Y` be any elements of :math:`\ell \setminus \{P_0, P_\infty\}`. To construct their **product** :math:`P = X \cdot Y` using **only an unmarked straightedge**:

1. Through the **zero point** :math:`P_0` draw an arbitrary auxiliary line :math:`c \neq \ell` and mark upon :math:`c` two distinct points :math:`U` and :math:`V` outside :math:`\ell`.
2. Join :math:`[U P_1]` and :math:`[V X]`, meeting in :math:`W = [U P_1] \cap [V X]`.
3. Draw the perspective axis :math:`a = [P_\infty W]` through the **horizon point** :math:`P_\infty` and :math:`W`.
4. Join :math:`[U Y]` meeting :math:`a` in :math:`Z = [U Y] \cap a`, and draw :math:`[V Z]` cutting :math:`\ell` in the required product :math:`P = X \cdot Y`.

.. picture:: /_static/figures/unit4_multiplication_of_throws.svg
   :alt: Pure straightedge multiplication of throws P = X * Y via centers U, V collinear with P_0 and axis a = [P_inf W].
   :caption: **Produkte aus Würfen (1857 § 20, art. 268):** Center line :math:`c = [P_0 U V]` and axis :math:`a = [P_\infty W]` generate the hyperbolic projectivity fixing both :math:`P_0` and :math:`P_\infty` while mapping :math:`P_1 \mapsto X` and :math:`Y \mapsto P = X \cdot Y`.

**Art. 269 (Field Laws of the Algebra of Throws).** Because :math:`[UV]` passes through :math:`P_0` while :math:`a` passes through :math:`P_\infty`, the projectivity :math:`\ell \xrightarrow{U} a \xrightarrow{V} \ell` fixes **both** :math:`P_0` and :math:`P_\infty` and is uniquely determined by :math:`P_1 \mapsto X`. Together with addition (§ 19), multiplication satisfies all laws of ordinary algebra (:term:`Rechnung mit Würfen <rechnung-mit-wuerfen>`):

.. math::

   X \cdot P_1 = X, \qquad X \cdot P_0 = P_0, \qquad X \cdot Y = Y \cdot X, \qquad (X \cdot Y) \cdot Z = X \cdot (Y \cdot Z),

.. math::

   X \cdot (Y + Z) = X \cdot Y + X \cdot Z,

and every :math:`X \notin \{P_0, P_\infty\}` possesses a unique multiplicative inverse :math:`X^{-1}` constructed by interchanging :math:`P_1` and :math:`X` in step 2 (:math:`W' = [U X] \cap [V P_1]`).

.. toctree::
   :hidden:

   de
   summary
   notes
