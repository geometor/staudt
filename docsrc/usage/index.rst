:navigation: header
:order: 20
:nav_title: Usage

.. _usage:

Using This Edition
==================

.. rubric:: Reader's Guide to the Interactive Bilingual Codices & Exact Straightedge Engine

The GEOMETOR edition of :cite:`Karl Georg Christian von Staudt (1847, 1857) <staudt:1847>` and :cite:`Moritz Pasch (1882) <pasch:1882>` integrates philological fidelity to historical German witnesses with interactive reading tracks and exact straightedge-only symbolic geometry.

Interactive Codex Features
--------------------------

1. Synchronized Reading Tracks
   Each unit across both *Geometry of Position* and *Lectures on Modern Geometry* provides four synchronized parallel tracks accessible from the book header bar:
   
   * **English Translation:** Modern mathematical translation preserving projective rigor and historical nomenclature.
   * **Original Witness:** Verbatim historical German print witnesses (1847, 1857, and 1882).
   * **Summary:** Conceptual overview, formal mathematical statements, and structural outline.
   * **Notes:** Scholarly commentary, historical analysis of the metrical-free revolution, and cross-references.

2. Primary-Source Folio Milestones
   Marginal page markers (such as ``[p. 1]``, ``[p. 43]``, or ``[p. 98]``) link directly to verified public-domain German witnesses archived in ``resources/staudt/sources/``. Header **Folio** badges open the primary witness directly in a side drawer or new tab.

3. Interactive Diagrams & Deductive Links
   Throughout the text, geometric entities, assertions, and algebraic expressions link to definitions:
   
   * Harmonic division, complete quadrangles, and order curves feature calibrated SVG figures.
   * Deductive steps cross-reference companion treatises like :cite:`Euclid's Elements <euclid:elements>` and :cite:`Pappus's Synagoge <pappus:synagoge>`.
   * Dynamic figures adapt seamlessly to light and dark reading themes.

4. Full-Text Search with In-Page Highlighting
   The sidebar search queries the complete bilingual text, commentary, and glossaries. Search query parameters automatically append ``?highlight=`` to highlight matched terms directly inside propositions and remarks.

5. Categories, Tags, Document Types & Collection Views
   Browse topics, historical figures, and projective invariants via the sidebar index. Collection pages support switching between **Cards**, **Banners**, and **List** layout modes.

6. People, Bibliography & Glossary Tooltips
   Hovering over any author or mathematician (:person:`Karl Georg Christian von Staudt <staudt>`, :person:`Moritz Pasch <pasch>`, :person:`David Hilbert <hilbert>`), citation (:cite:`staudt:1847`, :cite:`pasch:1882`), or technical term (:term:`Geometrie der Lage <geometrie-der-lage>`, :term:`Rechnung mit Würfen <rechnung-mit-wuerfen>`, :term:`Pasch's Axiom <pasch-grundsatz>`) displays an instant context card.

----

Command-Line & Python Verification API
--------------------------------------

In addition to web reading, all synthetic straightedge constructions and order verifications are executable from the command line and Python.

Command-Line Interface
~~~~~~~~~~~~~~~~~~~~~~

Inspect concordance entries and run exact symbolic straightedge verification:

.. code-block:: bash

   # Display cross-corpus concordance
   geometor-staudt --summary

   # Run exact symbolic verification of quadrangle uniqueness and throw algebra
   geometor-staudt --verify

   # Render theme-adaptive SVG figures
   geometor-staudt --render

Python API
~~~~~~~~~~

Import the exact symbolic solver directly into your Python scripts or Jupyter notebooks:

.. code-block:: python

   import sympy.geometry as spg
   from geometor.staudt.quadrangle import (
       construct_complete_quadrangle_harmonic_fourth,
       prove_symbolic_quadrangle_uniqueness,
   )
   from geometor.staudt.throws import (
       construct_von_staudt_addition,
       construct_von_staudt_multiplication,
   )

   # Construct harmonic fourth purely with straightedge lines (0 circles)
   A = spg.Point(0, 0)
   B = spg.Point(6, 0)
   C = spg.Point(2, 0)
   model, D = construct_complete_quadrangle_harmonic_fourth(A, B, C)
   assert D == spg.Point(-6, 0)

   # Prove universal independence from auxiliary quadrangle parameters
   result = prove_symbolic_quadrangle_uniqueness()
   assert result["is_harmonic_fourth"]
