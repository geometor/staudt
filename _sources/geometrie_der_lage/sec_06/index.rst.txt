:layout: book
:canonical_id: § 6
:breadcrumb_title: § 6
:order: 7
:folio: § 6
:tracks: English: index | German: de | Summary: summary | Notes: notes

.. _geometrie-sec_06-en:
.. _geometrie-sec_06:
.. _geometrie-sec-06-en:
.. _geometrie-sec-06:
.. _geometrie-unit-2-en:

.. folio:: § 6
   :page: 29

§ 6. Complete Plane Quadrangles and Harmonic Forms (arts. 66–74)
================================================================

.. rubric:: Karl Georg Christian von Staudt — *Geometrie der Lage* (1847), § 6 (arts. 66–74)

**Art. 66.** Four points :math:`E, F, G, H` lying in one plane, no three of which are collinear, determine six connecting lines called *sides* (*Seiten*), which group into three pairs of *opposite sides*:

.. math::

   ([EF], [GH]), \qquad ([FG], [HE]), \qquad ([EG], [FH]).

Such a configuration is called a :term:`complete plane quadrangle <vollstaendiges-viereck>` (*vollständiges ebenes Viereck*), and the three points in which its three pairs of opposite sides meet are called its **diagonal points** (*Diagonalpunkte*). Dually, four coplanar lines, no three concurrent, form a *complete plane quadrilateral* (*vollständiges ebenes Vierseit*) having six vertices grouped into three opposite pairs joined by three *diagonals*.

**Art. 67.** Let a straight carrier line :math:`\ell` pass through two diagonal points :math:`A = [EF] \cap [GH]` and :math:`B = [FG] \cap [HE]` of a complete plane quadrangle :math:`EFGH`, and let the remaining two opposite sides :math:`[EG]` and :math:`[FH]` meet :math:`\ell` in :math:`C` and :math:`D` respectively. Then the four collinear points :math:`A, C, B, D` are called **four harmonic points** (:term:`harmonisches Gebilde <harmonisches-gebilde>`), and :math:`D` is called the **fourth harmonic point** (*der vierte harmonische Punkt*) to :math:`A, B, C`, conjugate to :math:`C` with respect to the pair :math:`(A, B)`.

.. picture:: /_static/figures/unit2_complete_quadrangle_harmonic.svg
   :alt: Complete plane quadrangle EFGH cutting carrier line l in harmonic tetrad (A, B; C, D) = -1.
   :caption: **Pure Straightedge Harmonic Fourth (1847 § 6, art. 67 & § 8, art. 93):** Given collinear :math:`A, B, C`, choose :math:`E` off :math:`\ell` and :math:`G` on :math:`[CE]`, intersect :math:`F = [AE] \cap [BG]` and :math:`H = [BE] \cap [AG]`, and draw :math:`[FH]` cutting :math:`\ell` in the unique harmonic fourth :math:`D`.

**Art. 70 (Spatial Proof of Uniqueness).** *Given three distinct collinear points* :math:`A, B, C`, *the fourth harmonic point* :math:`D` *constructed by a complete plane quadrangle* :math:`EFGH` *depends solely upon* :math:`A, B, C` *and is entirely independent of the choice of the plane and of the quadrangle*.

*Proof.* Suppose first that a second quadrangle :math:`E'F'G'H'` lies in a **different plane** :math:`\alpha'` passing through the same carrier line :math:`\ell = [AB]`, with :math:`[E'F'] \cap [G'H'] = A`, :math:`[F'G'] \cap [H'E'] = B`, and :math:`[E'G']` passing through :math:`C`. Because :math:`[EG]` and :math:`[E'G']` meet at :math:`C`, the lines :math:`[EE']` and :math:`[GG']` lie in one plane and meet at a spatial center :math:`S` outside both :math:`\alpha` and :math:`\alpha'`. Projecting :math:`\alpha` onto :math:`\alpha'` from :math:`S`:

* Plane :math:`SEE'A` meets :math:`\alpha'` in :math:`[AE']`, and plane :math:`SGG'B` meets :math:`\alpha'` in :math:`[BG']`; since :math:`F = [AE] \cap [BG]`, ray :math:`[SF]` passes through :math:`F' = [AE'] \cap [BG']`.
* Likewise ray :math:`[SH]` passes through :math:`H' = [BE'] \cap [AG']`.
* Therefore the plane :math:`SFH` contains both :math:`[FH]` and :math:`[F'H']`, so both lines meet the common intersection line :math:`\ell = \alpha \cap \alpha'` in the **exact same point** :math:`D = D'`.

If a third quadrangle :math:`E''F''G''H''` lies in the **same** plane :math:`\alpha` as :math:`EFGH`, both yield the same point :math:`D` as the auxiliary quadrangle :math:`E'F'G'H'` in the second plane :math:`\alpha'`, hence :math:`D'' = D' = D`. :math:`\blacksquare`

**Art. 72.** In every harmonic tetrad :math:`(A, B; C, D)`, the roles of the two conjugate pairs :math:`(A, B)` and :math:`(C, D)` are completely symmetric, and within each pair the two elements may be interchanged; moreover, :math:`(A, B)` and :math:`(C, D)` invariably :term:`separate one another <getrennte-paare>`.

.. toctree::
   :hidden:

   de
   summary
   notes
