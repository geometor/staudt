=========
Changelog
=========

0.1.2 (2026-11-14)
==================

* Standardized Book Title Page with publication metadata, reading instructions, and structured navigation.
* Added top-level Header Navigation (``Book``, ``People``, ``Bibliography``, ``Usage``) and dedicated Reader's Guide (``docsrc/usage/``).
* Enhanced ``People`` directory with featured Author and Translator biographical profiles.
* Standardized structural section headings and terminology in English across codex indices.

0.1.1 (2026-11-13)
==================

* **added**: Added track-aware primary-source folio map (``resources/staudt/folio_map.json``) resolving 32/32 folio directives to verified German text loci and source files across *Geometrie der Lage* and *Vorlesungen über neuere Geometrie*.

0.1.0 (2026-11-12)
==================

* **Codex I (*Geometrie der Lage* 1847 & *Beiträge* 1856–1860)**: Synchronized 4-track Bilingual Book Codex (``English · Deutsch · Summary · Notes``) across 4 curated units covering pure projective incidence, complete quadrangles and harmonic conjugates, the Fundamental Theorem and polar conics, and von Staudt's *Rechnung mit Würfen* (*Algebra of Throws*, §§ 19, 20, 29).
* **Codex II (*Vorlesungen über neuere Geometrie* 1882)**: Synchronized 4-track Bilingual Book Codex across 2 curated units covering Pasch's *Grundbegriffe* / *Grundsätze*, linear betweenness (§ 1), Pasch's Line–Triangle Separation Axiom (*IV. Grundsatz* in § 2, p. 21 & *10. Lehrsatz*, p. 25), ideal elements, and the § 12 hypothetico-deductive criterion (pp. 98–100).
* **Exact Symbolic Straightedge-Only Library (``geometor.staudt``)**: Implemented ``construct_harmonic_fourth_straightedge``, ``verify_quadrangle_independence``, ``construct_von_staudt_addition``, ``construct_von_staudt_multiplication``, ``verify_golden_throw_identity``, ``demonstrate_pasch_axiom``, and symbolic Euclid ``I.16`` / ``I.21`` order-gap analyses with zero ``Float`` values and zero compass circles.
* **Visual & Cross-Corpus Apparatus**: Generated 8 theme-adaptive ``.euclid-graphic`` SVGs, 4 runnable ``demos/`` scripts, SHA-256 verified German archival source witnesses, and cross-corpus concordance linking ``euclid``, ``elements``, ``pappus``, ``hilbert``, ``bertrand-russell``, ``hoenen``, ``altshiller-court``, ``lemoine``, and ``codes`` (``GeoCoq`` / ``LeanEuclid``).
