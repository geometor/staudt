:date: 2026-04-16
:type: log
:summary: Initial release of geometor/staudt (v0.1.0) — uniting von Staudt's Geometrie der Lage (1847) & Algebra of Throws (1857) with Pasch's Vorlesungen über neuere Geometrie (1882) in two 4-track Book Codices and an exact straightedge-only SymPy library.

Initial Bilingual Book Codices & Straightedge-Only Symbolic Engine (``v0.1.0``)
===============================================================================

Established ``geometor/staudt`` (``v0.1.0``) to close the canonical reference and constructive loop across ``hilbert``, ``bertrand-russell``, ``pappus``, ``altshiller-court``, ``hoenen``, ``lemoine``, ``divine``, and ``codes``:

- **Archival Public-Domain Witnesses & SHA-256 Verification**:
  Curated clean German source witnesses in ``resources/staudt/sources/`` for :person:`Karl Georg Christian von Staudt <staudt>`'s *Geometrie der Lage* (:cite:`1847 <staudt:1847>`), *Beiträge zur Geometrie der Lage, Heft 2* (:cite:`1857 <staudt:1857>`), and :person:`Moritz Pasch <pasch>`'s *Vorlesungen über neuere Geometrie* (:cite:`1882 <pasch:1882>`), verified via ``resources/staudt/sources_manifest.json`` and mapped across 15 cross-repository loci in ``resources/staudt/concordance.json``.
- **Synchronized 4-Track Book Codex (``:layout: book``)**:
  Compiled :doc:`Geometrie der Lage & Beiträge (1847 & 1857) <../../geometrie_der_lage/index>` (with Moritz Pasch unbundled into standalone sister repository :doc:`geometor/pasch <pasch:index>`) across *English · Deutsch · Summary · Notes*, accompanied by standalone ``.euclid-graphic`` vector figures and full ``:person:``, ``:cite:``, and ``:term:`` apparatus.
- **100% Exact Straightedge-Only Symbolic Package (``geometor.staudt``)**:
  Implemented ``projective``, ``quadrangle``, ``throws``, ``pasch``, ``concordance``, ``render``, and ``cli`` on Python 3.13 with ``assert_straightedge_only(model)`` (**zero compass circles**), verifying complete-quadrangle harmonic fourths, projective field laws (:math:`X + Y`, :math:`X \cdot Y`), the :math:`\mathbb{Q}(\phi)` golden throw identity :math:`P_\phi \cdot P_\phi = P_\phi + P_1`, and deductive Pasch audits of Euclid ``I.16`` and ``I.21``.
