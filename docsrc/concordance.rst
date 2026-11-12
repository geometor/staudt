.. _concordance:

Cross-Corpus Concordance
========================

.. rubric:: Mapping ``geometor/staudt`` Across the GEOMETOR Digital Scriptorium & Constructive Canon

This concordance synchronizes the 15 canonical loci of ``resources/staudt/concordance.json`` across :person:`von Staudt <staudt>`'s *Geometrie der Lage* (:cite:`1847 <staudt:1847>`), *Beiträge zur Geometrie der Lage* (:cite:`1857 <staudt:1857>`), and :person:`Pasch <pasch>`'s *Vorlesungen über neuere Geometrie* (:cite:`1882 <pasch:1882>`) with ``euclid``, ``elements``, ``pappus``, ``hilbert``, ``bertrand-russell``, ``hoenen``, ``altshiller-court``, ``lemoine``, ``divine``, and ``codes``.

.. list-table:: Master Concordance Table (15 Canonical Loci)
   :header-rows: 1
   :widths: 12 22 22 20 24

   * - ID
     - Source Locus
     - Codex Unit & API
     - Sister Repositories
     - Deductive & Algebraic Role
   * - ``staudt-01``
     - Staudt 1847 *Vorwort* & § 1 (arts. 1–15)
     - :ref:`Codex I Unit 1 <geometrie-unit-1-en>` · ``assert_straightedge_only``
     - ``euclid`` Book I Post. 1–2; ``hilbert`` § 2 Group I; ``lemoine`` ``S = R``
     - Pure incidence foundation; complete exclusion of compass circles and metric ratios.
   * - ``staudt-02``
     - Staudt 1847 §§ 2–5 (arts. 16–53)
     - :ref:`Codex I Unit 1 <geometrie-unit-1-en>` · ``construct_parallel_straightedge``
     - ``euclid`` I.27–I.31; ``pappus`` ``ideal_elements``; ``hilbert`` § 4 Group III
     - Ideal points/lines via parallel sheaves and three-dimensional :term:`reciprocity <reciprocitaet>`.
   * - ``staudt-03``
     - Staudt 1847 § 6 (arts. 66–74)
     - :ref:`Codex I Unit 2 <geometrie-unit-2-en>` · ``construct_harmonic_fourth_straightedge``
     - ``pappus`` VII.129–131; ``altshiller-court`` Ch. VI; ``bertrand-russell`` 1897 § 114
     - Pure straightedge :term:`complete quadrangle <vollstaendiges-viereck>` definition of $(A, B; C, D) = -1$ and 3D uniqueness proof.
   * - ``staudt-04``
     - Staudt 1847 §§ 7–8 (arts. 75–98)
     - :ref:`Codex I Unit 2 <geometrie-unit-2-en>` · ``verify_quadrangle_independence``
     - ``pappus`` VII.139; ``hilbert`` Kap. V (Desargues); ``bertrand-russell`` 1903 Ch. XLV
     - Harmonic preservation defines :term:`projectivity <projektivisch>`; Fundamental Theorem of Projective Geometry.
   * - ``staudt-05``
     - Staudt 1847 § 9 (arts. 103–115)
     - :ref:`Codex I Unit 3 <geometrie-unit-3-en>` · ``pair_separates``
     - ``pappus`` involution lemmas; ``altshiller-court`` Ch. IX (Involution)
     - Hyperbolic vs. elliptic involutions; double points as harmonic conjugates of every pair.
   * - ``staudt-06``
     - Staudt 1847 §§ 18–19 (arts. 235–257)
     - :ref:`Codex I Unit 3 <geometrie-unit-3-en>` · ``unit3_polar_conic_self_conjugate.svg``
     - ``pappus`` Pascal/Brianchon; ``hilbert`` Kap. VI; ``altshiller-court`` Poles & Polars
     - :term:`Order curve <ordnungscurve>` defined as self-conjugate locus $P \in \pi(P)$ of a :term:`polar system <polarsystem>`.
   * - ``staudt-07``
     - Staudt 1857 Heft 2, § 19 (arts. 256–267)
     - :ref:`Codex I Unit 4 <geometrie-unit-4-en>` · ``construct_von_staudt_addition``
     - ``hilbert`` § 15 segment addition; ``codes`` projective arithmetic
     - Straightedge addition $S = X + Y$ fixing $P_\infty$ via parabolic double perspectivity.
   * - ``staudt-08``
     - Staudt 1857 Heft 2, § 20 (arts. 268–269)
     - :ref:`Codex I Unit 4 <geometrie-unit-4-en>` · ``construct_von_staudt_multiplication``
     - ``pappus`` VII.139 (commutativity); ``hilbert`` §§ 15–16; ``euclid`` VI.12
     - Straightedge multiplication $P = X \cdot Y$ fixing $P_0, P_\infty$; commutative iff Pappus holds.
   * - ``staudt-09``
     - Staudt 1857 Heft 2, § 29 (arts. 403–404)
     - :ref:`Codex I Unit 4 <geometrie-unit-4-en>` · ``construct_harmonic_scale``, ``projective_abscissa``
     - ``bertrand-russell`` 1897 §§ 118–124; ``hilbert`` § 17 coordinates
     - :term:`Harmonic scale <harmonische-reihe>` (Möbius net) and intrinsic :term:`projective abscissae <abscisse>` without distance.
   * - ``staudt-10``
     - Staudt 1857 §§ 19–20 over $\mathbb{Q}(\phi)$
     - :ref:`Codex I Unit 4 <geometrie-unit-4-en>` · ``verify_golden_throw_identity``
     - ``divine`` golden section; ``euclid`` II.11 & VI.30; ``pappus`` $\mathbb{Q}(\phi)$ ranges
     - Exact straightedge verification that $P_\phi \cdot P_\phi = P_\phi + P_1$ on any projective carrier.
   * - ``pasch-01``
     - Pasch 1882 *Vorwort*, *Einleitung*, § 1 (pp. 1–17)
     - :ref:`Codex II Unit 1 <pasch-unit-1-en>` · ``is_between``
     - ``hilbert`` § 3 Axioms II 1–3; ``bertrand-russell`` 1903 Ch. XLVI; ``hoenen`` Cap. IV
     - Eight nuclear axioms (*Grundsätze I–VIII*) of open linear :term:`betweenness <zwischen>`.
   * - ``pasch-02``
     - Pasch 1882 § 2 *IV. Grundsatz* (p. 21) & *10. Lehrsatz* (p. 25)
     - :ref:`Codex II Unit 2 <pasch-unit-2-en>` · ``demonstrate_pasch_axiom``
     - ``hilbert`` § 3 Axiom II 4; ``hoenen`` Cap. IV; ``bertrand-russell`` 1903 § 378
     - :term:`Pasch's Planar Separation Axiom <pasch-grundsatz>`: triangle entry implies unique opposite-side exit.
   * - ``pasch-03``
     - Pasch 1882 § 2 applied to Euclid ``I.16``
     - :ref:`Codex II Unit 2 <pasch-unit-2-en>` · ``demonstrate_euclid_i16_pasch_gap``
     - ``euclid`` Book I Prop. 16; ``elements`` ``G.16``; ``hilbert`` Theorem 7
     - Closes Euclid's exterior-angle crossbar gap where spherical lines fail open betweenness.
   * - ``pasch-04``
     - Pasch 1882 § 2 applied to Euclid ``I.21``
     - :ref:`Codex II Unit 2 <pasch-unit-2-en>` · ``demonstrate_euclid_i21_pasch_gap``
     - ``euclid`` Book I Prop. 21; ``elements`` ``G.21``; ``hilbert`` § 3 Theorem 5
     - Deductive proof via $\triangle AMC$ that interior ray $BD$ must exit open side $AC$ at $E$.
   * - ``pasch-05``
     - Pasch 1882 §§ 8–11 & § 12 (pp. 58–100)
     - :ref:`Codex II Unit 2 <pasch-unit-2-en>` · ``verify_source_witnesses``
     - ``hilbert`` §§ 1, 9–12; ``hoenen`` Cap. IV–V; ``bertrand-russell`` 1903 Ch. I
     - Intrinsic sheaf construction of ideal elements and the **Hypothetico-Deductive Manifesto** (p. 98).
