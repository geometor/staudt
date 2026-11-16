:layout: book
:canonical_id: § 20
:breadcrumb_title: § 20
:order: 2
:folio: § 20
:tracks: English: index | Deutsch: de | Summary: summary | Notes: notes

.. _beitraege-sec_20-en:
.. _beitraege-sec_20:
.. _beitraege-sec-20-en:
.. _beitraege-sec-20:

.. folio:: § 20
   :page: 174

§ 20. Pure Straightedge Multiplication of Throws (arts. 268–269)
================================================================

.. rubric:: Karl Georg Christian von Staudt — *Beiträge, Zweites Heft* (1857), § 20 (arts. 268–269)

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

.. toctree::
   :hidden:

   de
   summary
   notes
