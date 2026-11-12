===============
geometor-staudt
===============

**Synthetic Projective Foundations & Order Axiomatics** — Synchronized 4-track Bilingual Digital Scriptorium Book Codices and exact symbolic straightedge-only constructive library for **Karl Georg Christian von Staudt** (*Geometrie der Lage*, 1847; *Beiträge zur Geometrie der Lage*, 1856–1860) and **Moritz Pasch** (*Vorlesungen über neuere Geometrie*, 1882).

Overview
========

``geometor-staudt`` unites the **two nineteenth-century German pillars of modern synthetic geometry and formal axiomatics** referenced throughout ``geometor/hilbert``, ``geometor/bertrand-russell``, ``geometor/pappus``, ``geometor/altshiller-court``, ``geometor/hoenen``, ``geometor/lemoine``, and ``geometor/codes``:

1. **Codex I — Karl Georg Christian von Staudt**:
   - *Geometrie der Lage* (Nuremberg: Fr. Korn, 1847): Emancipates projective geometry from Poncelet's and Steiner's metric cross-ratios, founding harmonic conjugates purely on the **complete quadrangle** (*vollständiges Viereck*, § 8 art. 93), proving uniqueness via spatial/planar Desargues (§ 7 arts. 87–92), establishing the **Fundamental Theorem of Projective Geometry** (§ 9 arts. 103–115), and defining **conics as the self-conjugate locus of a planar polarity** (§§ 18–19 arts. 234–257), recovering Steiner's generation and Pascal's & Brianchon's theorems without distance or circles.
   - *Beiträge zur Geometrie der Lage* (Nuremberg: Fr. Korn, 1856–1860, §§ 19, 20, 29): **Rechnung mit Würfen** (*The Algebra of Throws*) — fixes three collinear reference points $(P_0, P_1, P_\infty)$ and constructs **projective addition** ($X + Y$) and **projective multiplication** ($X \cdot Y$) purely with an unmarked straightedge, recovering full field arithmetic and projective coordinates (*Abscissen*) directly from incidence.
2. **Codex II — Moritz Pasch**:
   - *Vorlesungen über neuere Geometrie* (Leipzig: B. G. Teubner, 1882): Separates primitive concepts (*Grundbegriffe* / *Kernbegriffe*) and primitive propositions (*Grundsätze* / *Kernsätze*) from empirical intuition, axiomatizes linear betweenness (§ 1), formulates **Pasch's Planar Separation Axiom** (*IV. Grundsatz* in § 2, p. 21 & *10. Lehrsatz*, p. 25) closing the unstated diagrammatic assumptions in Euclid ``I.16`` and ``I.21``, builds ideal points/lines/planes as sheaves, and enunciates the modern **hypothetico-deductive criterion** (§ 12, pp. 98–100).

Exact Symbolic Straightedge-Only Library
========================================

Every constructive routine in ``geometor.staudt`` operates on ``geometor.model.Model(..., auto_intersect=False)`` with **100% exact SymPy arithmetic** and **zero ``construct_circle`` calls**:

- ``construct_harmonic_fourth_straightedge(model, A, B, C, aux_P, aux_Q)`` — Pure straightedge complete-quadrangle construction of $D$ with ``cross_ratio(A, B, C, D) == -1``, plus ``verify_quadrangle_independence`` proving invariance across distinct quadrangles.
- ``construct_von_staudt_addition(model, P0, P1, Pinf, X, Y)`` — Pure straightedge projective addition working for both **finite horizon points** $P_\infty$ and **ideal points at infinity** (``Pinf=None``), verifying $P_1 + P_1 = P_2$ and $P_2 + P_3 = P_5$.
- ``construct_von_staudt_multiplication(model, P0, P1, Pinf, X, Y)`` — Pure straightedge projective multiplication verifying $P_2 \cdot P_3 = P_6$ and the golden-throw identity $P_\phi \cdot P_\phi = P_\phi + P_1$ ($\phi^2 = \phi + 1$) over $\mathbb{Q}(\phi)$.
- ``demonstrate_pasch_axiom(model, A, B, C, line_P, line_Q)`` — Exact signed-orientation and betweenness verification of Pasch's *IV. Grundsatz* on $\triangle ABC$, paired with symbolic audits of Euclid ``I.16`` and ``I.21``.

Verification & Documentation Build
==================================

.. code-block:: bash

   pytest
   ruff check src demos scripts tests
   publish build
