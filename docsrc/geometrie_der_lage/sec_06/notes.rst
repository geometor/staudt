:layout: book
:canonical_id: § 6
:breadcrumb_title: § 6
:order: 7
:tracks: English: index | Deutsch: de | Summary: summary | Notes: notes

.. _geometrie-sec_06-notes:
.. _geometrie-unit-2-notes:

Critical Notes: § 6. Complete Plane Quadrangles and Harmonic Forms (arts. 66–74)
================================================================================

.. rubric:: Scholarly Commentary — Karl Georg Christian von Staudt — *Geometrie der Lage* (1847), § 6 (arts. 66–74)

* **Why Art. 70 Lifts into Three Dimensions (:person:`Hilbert <hilbert>` Chapter V)**: :person:`Von Staudt <staudt>`'s breathtakingly short uniqueness proof in Art. 70 uses three-dimensional spatial incidence! In 1899 (:cite:`Grundlagen Kap. V <hilbert:1899>`, ``geometor/hilbert``), :person:`David Hilbert <hilbert>` proved that in a single plane without 3D space axioms, quadrangle uniqueness is equivalent to **Desargues's Theorem**: in a non-Desarguesian plane (such as the Moulton plane), different quadrangles on the same collinear triad $(A, B, C)$ yield *different* fourth points $D$! In ``geometor.staudt.quadrangle``, ``prove_symbolic_quadrangle_uniqueness()`` proves over $\mathbb{Q}(c, u, v, t)$ that in any Desarguesian coordinate plane $D_x = \frac{c}{2c - 1}$ is algebraically invariant across all off-line parameters $(u, v, t)$.

* **Russell's 1897 Critique vs. 1903 Vindication**: In :cite:`*An Essay on the Foundations of Geometry* (1897, §§ 114–120) <russell:1897>` (``geometor/bertrand-russell``), :person:`Bertrand Russell <russell>` initially suspected von Staudt's quadrangle construction of hidden metrical circularity; by :cite:`*The Principles of Mathematics* (1903, Ch. XLV, §§ 365–370) <russell:1903>`, armed with :person:`Pasch <pasch>` and :person:`Veblen <veblen>`'s precursors, Russell retracted his objection and hailed von Staudt's quadrangle reduction as one of the supreme achievements of nineteenth-century logic of relations.
