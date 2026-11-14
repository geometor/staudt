:navigation: header
:order: 25
:nav_title: Demos

Exact Straightedge Demonstrations
=================================

.. rubric:: Executable ``geometor.model`` Propositions for ``geometor/staudt``

The four standalone scripts in ``demos/`` verify every constructive theorem of :person:`von Staudt <staudt>` and :person:`Pasch <pasch>` in exact SymPy rational and quadratic-radical arithmetic, enforcing ``assert_straightedge_only(model)`` (**zero compass circles**).

----

01 · Complete-Quadrangle Harmonic Fourth & Desarguesian Uniqueness
------------------------------------------------------------------

* **Script**: ``demos/01_harmonic_fourth_straightedge.py``
* **Locus**: :cite:`Staudt 1847 §§ 6–8, arts. 66–98 <staudt:1847>` (:ref:`Codex I, Unit 2 <geometrie-unit-2-en>`)
* **Verification**: Constructs the harmonic fourth $D = (-6, 0)$ of $A=(0,0), B=(6,0), C=(2,0)$ using 7 straightedge lines and 0 circles, proves $(A, B; C, D) = -1$ and mutual pair separation $AB \parallel CD$, confirms numerical invariance across distinct auxiliary quadrangles, and proves universally over $\mathbb{Q}(c, u, v, t)$ via ``prove_symbolic_quadrangle_uniqueness()`` that $x_D = \frac{c}{2c - 1}$ is completely independent of the off-line quadrangle parameters $(u, v, t)$.

.. picture:: /_static/figures/unit2_complete_quadrangle_harmonic.svg
   :alt: Complete plane quadrangle EFGH cutting carrier line l in harmonic tetrad (A, B; C, D) = -1.
   :caption: **Complete Plane Quadrangle EFGH (1847 § 6, art. 67):** Opposite sides pass through $A$ and $B$, while diagonals $[EG]$ and $[FH]$ cut the carrier in $C$ and $D$ with $(A, B; C, D) = -1$.

----

02 · Pure Straightedge Addition of Throws & the Harmonic Scale
--------------------------------------------------------------

* **Script**: ``demos/02_von_staudt_addition.py``
* **Locus**: :cite:`Staudt 1857 Heft 2, §§ 19 & 29, arts. 256–267, 403–404 <staudt:1857>` (:ref:`Codex I, Unit 4 <geometrie-unit-4-en>`)
* **Verification**: Executes parabolic double-perspectivity addition $S = X + Y$ both for a finite horizon point $P_\infty = (8, 0)$ and for the ideal horizon $P_\infty = \infty$ (via ``construct_parallel_straightedge``), verifying $P_1 + P_1 = P_2$ and $P_2 + P_3 = P_5$, and builds the integer harmonic ladder $P_{-1}, P_0, P_1, \dots, P_5$.

.. picture:: /_static/figures/unit4_addition_of_throws.svg
   :alt: Von Staudt's pure straightedge addition of throws S = X + Y via centers U, V collinear with P_inf.
   :caption: **Summen von Würfen (1857 § 19, art. 256):** Horizon ray $[P_\infty U V]$ and perspective axis $a = [P_\infty R]$ construct $S = X + Y$ using 6 straightedge incidences and 0 circles.

----

03 · Straightedge Multiplication of Throws & Golden Identity over $\mathbb{Q}(\phi)$
------------------------------------------------------------------------------------

* **Script**: ``demos/03_von_staudt_multiplication_golden.py``
* **Locus**: :cite:`Staudt 1857 Heft 2, § 20, arts. 268–269 <staudt:1857>` (:ref:`Codex I, Unit 4 <geometrie-unit-4-en>`)
* **Verification**: Executes hyperbolic double-perspectivity multiplication $P = X \cdot Y$ fixing $P_0$ and $P_\infty$, verifies $P_2 \cdot P_3 = P_6$ and distributivity $(P_2 + P_3) \cdot P_2 = P_2 \cdot P_2 + P_3 \cdot P_2$, and proves over $\mathbb{Q}(\phi)$ ($\phi = \frac{1 + \sqrt{5}}{2}$) that the straightedge product $P_\phi \cdot P_\phi$ and the straightedge sum $P_\phi + P_1$ land on the **exact same symbolic point** $P_{\phi^2} = \left(\frac{92 + 28\sqrt{5}}{71}, 0\right)$ on the projective carrier!

.. picture:: /_static/figures/unit4_multiplication_of_throws.svg
   :alt: Von Staudt's pure straightedge multiplication of throws P = X * Y via centers U, V collinear with P_0.
   :caption: **Produkte aus Würfen (1857 § 20, art. 268):** Center line $[P_0 U V]$ and horizon axis $a = [P_\infty W]$ construct $P = X \cdot Y$ purely by straightedge.

----

04 · Pasch's Planar Separation Axiom & Euclid's ``I.16`` / ``I.21`` Order Audits
--------------------------------------------------------------------------------

* **Script**: ``demos/04_pasch_axiom_and_euclid_i16.py``
* **Locus**: :cite:`Pasch 1882 § 2, IV. Grundsatz (p. 21) & 10. Lehrsatz (p. 25) <pasch:1882>` (:ref:`Codex II, Unit 2 <pasch-unit-2-en>`)
* **Verification**: Audits signed half-plane orientations and strict interior side exits on $\triangle ABC$, verifies the interior crossbar intersection $K \in AD$ needed for ``Elements I.16``, and deductively proves ``Elements I.21``'s interior ray exit $E \in AC$ by applying Pasch's *IV. Grundsatz* to sub-triangle $\triangle AMC$.

.. picture:: /_static/figures/pasch_unit2_planar_axiom_euclid_gaps.svg
   :alt: Pasch's planar separation axiom on triangle ABC and deductive proof of Euclid I.21 ray exit E on AC.
   :caption: **Pasch's IV. Grundsatz (1882 § 2, p. 21) & Euclid I.21:** Transversal $[BD]$ enters $\triangle AMC$ on open segment $CM$ and misses segment $AM$, forcing an interior exit $E$ strictly between $A$ and $C$.
