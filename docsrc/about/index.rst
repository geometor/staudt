:navigation: header
:order: 20
:nav_title: About

.. _about:
.. _about-index:
.. _about-staudt:

About
=====

.. rubric:: Extracting Historical Semantic Knowledge & Repurposing It for Exact Symbolic Reasoning

About This Edition
------------------

The GEOMETOR edition of :person:`Karl Georg Christian von Staudt <staudt>` presents the foundational treatises that resolved synthetic geometry's nineteenth-century foundational crises and created pure projective geometry without measurement:

* **Karl Georg Christian von Staudt** (*Geometrie der Lage*, :cite:`1847 <staudt:1847>`; *Beiträge zur Geometrie der Lage*, :cite:`1857 <staudt:1857>`):
  Liberates harmonic division, conics, and projective coordinates (:term:`Rechnung mit Würfen <rechnung-mit-wuerfen>`) from metrical length and numerical cross-ratios. By constructing the harmonic fourth :math:`D` of three collinear points purely by unmarked straightedge via the :term:`complete plane quadrangle <vollstaendiges-viereck>` and erecting the synthetic Algebra of Throws, von Staudt proved that projective geometry generates intrinsic numerical coordinates over any commutative field before a single distance is measured or compass opened.

The linear order and planar separation axioms that complete von Staudt's foundation are unbundled into the standalone sister codex :doc:`Moritz Pasch: Vorlesungen über neuere Geometrie (1882) <pasch:index>`.

This critical edition extracts the implicit deductive architecture of von Staudt's masterpieces into an addressable, machine-readable semantic corpus. Every proposition, definition, throw operation, and harmonic step is indexed with stable anchors, linked to synchronized four-track codices (*English translation, original German print witness, conceptual summary, and scholarly notes*), and connected to sister GEOMETOR repositories: classical compass-and-straightedge antecedents in :cite:`Euclid's Elements <euclid:elements>`, projective pole-polar antecedents in :cite:`Pappus's Synagoge <pappus:synagoge>`, axiomatic foundations in :cite:`Hilbert's Grundlagen <hilbert:1899>`, and modern algebraic foundations in ``geometor.model``.

The GEOMETOR Mission
--------------------

GEOMETOR is an ongoing research initiative founded by **phi ARCHITECT** dedicated to recovering, formalizing, and revitalizing the world's mathematical and geometric heritage through three foundational pillars:

1. **Extracting Historical Semantic Knowledge**:
   Moving beyond passive page scans and OCR to recover the living deductive structure of 2,300+ years of geometric, axiomatic, and philosophical treatises—elevating prose, marginal citations, primary-source folios (via ``publish folio``), and calibrated Ink-to-Vector ``.euclid-graphic`` diagrams into structured, machine-addressable semantic graphs.

2. **Exact Symbolic Grounding (``geometor.model``)**:
   Anchoring geometric constructions in 100% exact symbolic algebra (`SymPy <https://www.sympy.org/>`_) and Rational Trigonometry invariants (quadrance, spread, cross-ratio) over exact algebraic fields (:math:`\mathbb{Q}`, :math:`\mathbb{Q}(\phi)`) rather than floating-point approximations. In ``geometor.staudt``, every construction is rigorously verified straightedge-only (``len(model.circles) == 0``, Lemoine simplicity class :math:`S = R`), demonstrating that projective coordinates and harmonic conjugates emerge entirely free from metrical measurement.

3. **Repurposing Knowledge Across Mediums**:
   Re-deploying extracted semantic and algebraic structures across synchronized multi-track **Book Codices** and EPUB 3 editions (`photon-platform/publish <https://github.com/phiarchitect/publish>`_), computable deductive canons (``geometor.elements``, ``geometor.etc``, ``geometor.pappus``, ``geometor.divine``), interactive SVG laboratories, and visual broadcasts across `geometor.com <https://geometor.com>`_.

Sources, Provenance & Methodology
---------------------------------

The texts and diagrams in this edition derive directly from high-resolution scans of original nineteenth-century German editions preserved in the GEOMETOR archival repository:

* **Staudt (1847):** *Geometrie der Lage*. Nürnberg: Verlag der Friedr. Korn'schen Buchhandlung, 1847 (vi + 216 pp.). Public-domain German witness archived in ``resources/staudt/sources/staudt_1847_geometrie_der_lage_de.txt``.
* **Staudt (1857):** *Beiträge zur Geometrie der Lage, Zweites Heft* (§§ 15–29, arts. 185–408). Nürnberg: Verlag der Friedr. Korn'schen Buchhandlung, 1857. Transcribed in ``resources/staudt/sources/staudt_1857_beitraege_wuerfe_de.txt``.

Scholarly translations and commentaries follow the Digital Scriptorium methodology developed within the GEOMETOR project: strict content/code separation, verbatim transcriptions of primary German witnesses alongside modern English translations, cross-corpus concordance references, and reproducible Python test suites verifying every geometric assertion symbolically.

For further exploration of this edition's structure and verification tools:

* :ref:`Reader's Guide & Usage Instructions <usage>`
* :ref:`Cross-Corpus Concordance <concordance>`
* :ref:`Systematic Bibliography <bibliography>`
* :ref:`People & Historical Figures <persons>`
* :ref:`Bilingual Mathematical Glossary <glossary>`
* :doc:`Exact Straightedge Demonstrations <../demos/index>`
* :doc:`Python Symbolic API Reference <../modules/index>`
