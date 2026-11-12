:layout: book

.. _geometrie-unit-2-notes:

Unit 2 Critical Notes: Desargues, Klein's Continuity Gap & Darboux
==================================================================

.. rubric:: Scholarly & Constructive Commentary on *Geometrie der Lage* (1847), §§ 6–8

* **Why Art. 70 Lifts into Three Dimensions (:person:`Hilbert <hilbert>` Chapter V)**: :person:`Von Staudt <staudt>`'s breathtakingly short uniqueness proof in Art. 70 uses three-dimensional spatial incidence! In 1899 (:cite:`Grundlagen Kap. V <hilbert:1899>`, ``geometor/hilbert``), :person:`David Hilbert <hilbert>` proved that in a single plane without 3D space axioms, quadrangle uniqueness is equivalent to **Desargues's Theorem**: in a non-Desarguesian plane (such as the Moulton plane), different quadrangles on the same collinear triad $(A, B, C)$ yield *different* fourth points $D$! In ``geometor.staudt.quadrangle``, ``prove_symbolic_quadrangle_uniqueness()`` proves over $\mathbb{Q}(c, u, v, t)$ that in any Desarguesian coordinate plane $D_x = \frac{c}{2c - 1}$ is algebraically invariant across all off-line parameters $(u, v, t)$.
* **The Klein–Darboux–Pasch History of Art. 96**: In Art. 96, von Staudt concluded that fixing three points $A, B, C$ fixes *every* point of the line because repeated harmonic fourths generate an everywhere dense Möbius net. :person:`Felix Klein <klein>` (:cite:`1873 <klein:1873>`) observed two subtleties:

  1. Density of the rational harmonic scale requires an **order and continuity (Archimedean/Dedekind) axiom**—subsequently supplied by :person:`Moritz Pasch <pasch>` (:cite:`1882 <pasch:1882>`).
  2. Over the complex field $\mathbb{C}$, complex conjugation $z \mapsto \bar{z}$ preserves all harmonic cross-ratios $(-1 = \overline{-1})$ and fixes $0, 1, \infty$ without being projective! Over $\mathbb{R}$, however, :person:`Jean-Gaston Darboux <darboux>` (:cite:`1880 <darboux:1880>`) proved that every harmonic-preserving bijection of $\mathbb{P}^1(\mathbb{R})$ automatically preserves positive squares (hence order and continuity) and is therefore strictly projective—completely vindicating von Staudt over the real line! Over an arbitrary field $\mathbb{F}$, a harmonic-preserving bijection is *semilinear* (projective iff $\operatorname{Aut}(\mathbb{F}) = \{1\}$).

* **Russell's 1897 Critique vs. 1903 Vindication**: In :cite:`*An Essay on the Foundations of Geometry* (1897, §§ 114–120) <russell:1897>` (``geometor/bertrand-russell``), :person:`Bertrand Russell <russell>` initially suspected von Staudt's quadrangle construction of hidden metrical circularity; by :cite:`*The Principles of Mathematics* (1903, Ch. XLV, §§ 365–370) <russell:1903>`, armed with :person:`Pasch <pasch>` and :person:`Veblen <veblen>`'s precursors, Russell retracted his objection and hailed von Staudt's quadrangle reduction as one of the supreme achievements of nineteenth-century logic of relations.
