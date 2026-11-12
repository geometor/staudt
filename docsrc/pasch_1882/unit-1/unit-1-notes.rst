:layout: book

.. _pasch-unit-1-notes:

Unit 1 Critical Notes: From Pasch's Eight Grundsätze to Hilbert Group II
========================================================================

.. rubric:: Scholarly & Constructive Commentary on *Vorlesungen* (1882), § 1

* **Direct Lineage to Hilbert's Axioms II 1–3 (1899)**: Seventeen years after :person:`Pasch <pasch>`'s *Vorlesungen*, :person:`David Hilbert <hilbert>` (:cite:`Grundlagen § 3 <hilbert:1899>`, ``geometor/hilbert``) compressed Pasch's *Grundsätze* I–VIII into his Group II linear order axioms (II 1: symmetry $A\text{--}B\text{--}C \implies C\text{--}B\text{--}A$ and collinearity; II 2: density + prolongation $A\text{--}C\text{--}B$ and $A\text{--}B\text{--}D$; II 3: at most one of three collinear points lies between the other two), noting in 1902 that E. H. Moore proved Hilbert's original four-point Theorem 4 redundant once Pasch's planar Axiom II 4 is assumed!
* **Why Spherical Geometry Fails Grundsatz III & VI**: On a sphere (Riemannian elliptic geometry), great-circle segments prolonged sufficiently far return to their starting point, so $C$ can lie between $A$ and $B$ along one arc while $A$ lies between $B$ and $C$ along the complementary arc—violating **Grundsatz III** and breaking :person:`Euclid <euclid>`'s proof of the Exterior Angle Theorem (``Elements I.16``)!
* **Exact Symbolic Implementation**: In ``geometor.staudt.projective``, ``is_between(A, B, C)`` verifies exact collinearity via `zero_test` of the $2 \times 2$ cross product and tests strict open positivity $0 < t < 1$ in $(C - A) = t (B - A)$ over exact SymPy rationals and quadratic radicals.
