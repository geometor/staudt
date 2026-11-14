:navigation: header
:order: 10
:nav_title: Mission

Mission & Axiomatic Synthesis
=============================

.. rubric:: Why von Staudt (1847, 1857) and Pasch (1882) Stand Together in GEOMETOR

Across the nineteenth century, synthetic geometry confronted two foundational crises:

1. **The Circularity of Metrical Projective Geometry**: :person:`Jean-Victor Poncelet <poncelet>`, :person:`Jakob Steiner <steiner>`, and :person:`Michel Chasles <chasles>` discovered that incidence, harmonic division, and conic polarity remain invariant under central projection—the *most general* spatial transformations—yet defined those invariants using Euclidean segment lengths and signed arithmetic cross-ratios $\frac{AC}{BC} : \frac{AD}{BD}$. How could the science of pure position depend upon compass-based congruence?
2. **The Unstated Order Assumptions of Classical & Projective Deduction**: Both :person:`Euclid <euclid>` (in :cite:`*Elements* <euclid:elements>` ``I.16`` and ``I.21``) and :person:`von Staudt <staudt>` himself (in assuming that the rational :term:`harmonic scale <harmonische-reihe>` exhausts continuous projective order) relied silently on visual inspection of betweenness and planar separation.

``geometor/staudt`` unites the two treatises that resolved these twin crises and forged modern axiomatic geometry:

* **Karl Georg Christian von Staudt** (*Geometrie der Lage*, :cite:`1847 <staudt:1847>`; *Beiträge*, :cite:`Heft 2, 1857 <staudt:1857>`):
  Constructs the :term:`harmonic fourth <harmonisches-gebilde>` $D$ of three collinear points $(A, B, C)$ purely by unmarked straightedge via the :term:`complete plane quadrangle <vollstaendiges-viereck>`, defines :term:`conics <ordnungscurve>` as self-conjugate loci of :term:`planar polarities <polarsystem>`, and erects the :term:`Algebra of Throws <rechnung-mit-wuerfen>` ($X + Y$, $X \cdot Y$), generating intrinsic coordinates over any commutative field **before** a single distance is measured.
* **Moritz Pasch** (*Vorlesungen über neuere Geometrie*, :cite:`1882 <pasch:1882>`):
  Isolates the eight nuclear axioms of open linear :term:`betweenness <zwischen>` (§ 1) and **Pasch's Planar Separation Axiom** (:term:`IV. Grundsatz <pasch-grundsatz>`, § 2, p. 21), grounds projective ideal elements strictly on finite sheaves (*Bündel*, §§ 8–11), and states the modern hypothetico-deductive criterion (§ 12, p. 98) directly inherited by :person:`David Hilbert <hilbert>`, :person:`Bertrand Russell <russell>`, :person:`Oswald Veblen <veblen>`, :person:`Fr. Petrus Hoenen <hoenen>`, and :person:`Alfred Tarski <tarski>`.

Exact Symbolic Realization in ``geometor.staudt``
-------------------------------------------------

In keeping with GEOMETOR's mandate of **100% exact symbolic algebra** and **strict content/code separation**:

* Every straightedge construction in ``geometor.staudt`` executes on ``Model(..., auto_intersect=False)`` over $\mathbb{Q}$ and $\mathbb{Q}(\phi)$ and enforces ``assert_straightedge_only(model)`` (**zero circles**, ``len(model.circles) == 0``, Lemoine class ``S = R``).
* All historical and translated codex tracks in :doc:`Codex I <../geometrie_der_lage/index>` and :doc:`Codex II <../pasch_1882/index>` remain pure scholarly text accompanied by standalone ``.euclid-graphic`` SVG figures, while executable Python constructions reside cleanly in ``src/geometor/staudt/`` and ``demos/``.
