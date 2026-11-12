:layout: book

.. _pasch-unit-2-notes:

Unit 2 Critical Notes: Closing Euclid's Gaps & the Birth of Modern Axiomatics
=============================================================================

.. rubric:: Scholarly & Constructive Commentary on *Vorlesungen* (1882), §§ 2, 8–12

* **Closing Euclid's ``I.16`` and ``I.21`` Order Gaps (`geometor.staudt.pasch`)**:

  * In ``Elements I.16`` (*Exterior Angle Theorem*, ``geometor/euclid`` & ``geometor/elements`` ``G.16``), :person:`Euclid <euclid>` bisects $AC$ at $E$, doubles $BE$ to $F$, and assumes from the diagram that $F$ lies inside exterior angle $\angle ACD$. ``demonstrate_euclid_i16_pasch_gap()`` applies :person:`Pasch <pasch>`'s *IV. Grundsatz* to $\triangle ABD$ and transversal $[CF]$: since $B\text{--}C\text{--}D$ on side $BD$ while $[CF]$ meets $[BF]$ at $F$ beyond $E$, ray $CF$ is forced to pierce crossbar $AD$ internally at $K$ ($A\text{--}K\text{--}D$).
  * In ``Elements I.21``, given interior point $D$ of $\triangle ABC$, Euclid writes *"let $BD$ be drawn through to $E$ [on $AC$]"* without proof. ``demonstrate_euclid_i21_pasch_gap()`` draws $[CD]$ meeting $AB$ at $M$ ($A\text{--}M\text{--}B$, $C\text{--}D\text{--}M$) and applies *Grundsatz IV* to sub-triangle $\triangle AMC$: since $[BD]$ enters open side $CM$ at $D$ and meets $[AM]$ externally at $B$, it **must** exit open side $AC$ at $E$ ($A\text{--}E\text{--}C$).

* **From Pasch § 12 (1882) to Hilbert's Tables, Chairs, and Beer Mugs (1899) & Hoenen's Critique (1954)**:

  * :person:`Pasch <pasch>`'s famous paragraph on p. 98 of § 12 is the verbatim philosophical fountainhead of :person:`David Hilbert <hilbert>`'s :cite:`*Grundlagen der Geometrie* (1899) <hilbert:1899>` (*"One must be able to say at all times—instead of points, straight lines, and planes—tables, chairs, and beer mugs"*), :person:`Bertrand Russell <russell>`'s relational logicism (:cite:`1903 Ch. I & XLVI <russell:1903>`), and :person:`Alfred Tarski <tarski>`'s first-order inner/outer Pasch axiom (:cite:`1959 <tarski:1959>`).
  * Conversely, in ``geometor/hoenen`` (:cite:`*De Noetica Geometriae*, 1954, Cap. IV–V <hoenen:1954>`), :person:`Fr. Petrus Hoenen, S.J. <hoenen>` engages Pasch directly: praising Pasch for uncovering the true relational content of ``I.16`` and planar separation, while arguing that our initial grasp of :term:`Stammsätze <stammsaetze>` arises not from brute Humean induction over physical bodies, but from intellectual abstraction (*judicium per phantasma*) in intelligible extension.
