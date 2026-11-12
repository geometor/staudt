# GEOMETOR • staudt

**Synthetic Projective Foundations & Order Axiomatics**: Synchronized 4-Track Bilingual Digital Scriptorium Book Codices and exact symbolic straightedge-only constructive library uniting:

1. **Karl Georg Christian von Staudt (1798–1867)**:
   - *Geometrie der Lage* (Nuremberg: Fr. Korn / Bauer und Raspe, 1847) — Emancipation of projective geometry from metric cross-ratios, complete quadrangles (*Vollständiges Viereck*), Desarguesian uniqueness of the fourth harmonic point, the Fundamental Theorem of Projective Geometry, involutions, and the polar definition of conics as self-conjugate loci ($P \in \pi(P)$).
   - *Beiträge zur Geometrie der Lage* (Nuremberg: Fr. Korn / Bauer und Raspe, 1856–1860, Heft 1–3) — *Rechnung mit Würfen* (*Algebra of Throws*, §§ 19, 20, 29): constructing projective addition ($X + Y$), projective multiplication ($X \cdot Y$), harmonic scales, and abscissa coordinates purely from complete quadrangles and an unmarked straightedge—without a ruler scale or compass distance.
2. **Moritz Pasch (1843–1930)**:
   - *Vorlesungen über neuere Geometrie* (Leipzig: B. G. Teubner, 1882) — Primitive concepts (*Grundbegriffe* / *Kernbegriffe*) and primitive propositions (*Grundsätze* / *Kernsätze*), linear betweenness (§ 1), **Pasch's Planar Separation Axiom** (*IV. Grundsatz* in § 2, p. 21 & *10. Lehrsatz* in § 2, p. 25), ideal bundles completing descriptive into projective space, and the hypothetico-deductive manifesto (§ 12, pp. 98–100) closing Euclid's diagrammatic order gaps (`I.1`, `I.16`, `I.21`).

---

## Architectural Invariants

1. **100% Exact Symbolic Algebra & Pure Straightedge Incidence**:
   - Every construction in `src/geometor/staudt/` operates on `Model(..., auto_intersect=False)` over exact SymPy `Integer`, `Rational`, or quadratic/radical number fields ($\mathbb{Q}$, $\mathbb{Q}(\phi)$)—**zero `float` or `sp.Float` approximations**.
   - **Strict Straightedge Purity**: Projective constructions (`quadrangle.py`, `throws.py`) call **zero `model.construct_circle` operations** (`assert_straightedge_only(model)`), working seamlessly both when the horizon point $P_\infty$ is a **finite projective point** on the carrier line and when $P_\infty$ is an **ideal point at infinity**.
2. **Strict Historical Text / Executable Code Separation**:
   - Both 4-track Book Codices (`docsrc/geometrie_der_lage/` and `docsrc/pasch_1882/`) use `:layout: book` across `-en.rst`, `-de.rst`, `-summary.rst`, and `-notes.rst` with standalone `.euclid-graphic` SVGs in `docsrc/_static/figures/` and **zero embedded `py_file` directives**.
   - All executable SymPy constructions and verification scripts live in `src/geometor/staudt/`, `demos/`, `scripts/`, and `tests/`.
3. **100% Public-Domain Provenance**:
   - Primary German witnesses derive strictly from the public-domain Nuremberg (1847, 1856–1860) and Leipzig Teubner (1882) editions archived in `resources/staudt/sources/` with SHA-256 verification. All English translations in `-en.rst` are original scholarly GEOMETOR translations from the 1847, 1857, and 1882 German originals.

---

## Key Modules (`src/geometor/staudt/`)

- `projective.py`: Projective cross-ratio abscissae `(Pinf, P0; P1, X)` (both finite horizon and ideal parallel), linear betweenness `is_between`, 4-point cyclic separation `pair_separates`, and `assert_straightedge_only`.
- `quadrangle.py`: `construct_harmonic_fourth_straightedge` (von Staudt 1847 § 8 art. 93) and `verify_quadrangle_independence` proving Desarguesian invariance across distinct auxiliary quadrangles.
- `throws.py`: `construct_von_staudt_addition` (*Beiträge* § 19 arts. 256–267), `construct_von_staudt_multiplication` (§ 20 arts. 268–275), `construct_parallel_straightedge` (Steiner–trapezoid pure straightedge parallel), `construct_harmonic_scale`, and `verify_golden_throw_identity` ($\phi^2 = \phi + 1$ over $\mathbb{Q}(\phi)$).
- `pasch.py`: `demonstrate_pasch_axiom` (Pasch 1882 § 2 *IV. Grundsatz* & *10. Lehrsatz*) and symbolic audits of Euclid `I.16` and `I.21` (`demonstrate_euclid_i16_pasch_gap`, `demonstrate_euclid_i21_pasch_gap`).
- `concordance.py`: Cross-corpus concordance (`euclid`, `elements`, `pappus`, `hilbert`, `bertrand-russell`, `hoenen`, `altshiller-court`, `lemoine`, `codes` `GeoCoq`/`LeanEuclid`) and SHA-256 source witness auditor.
- `render.py` & `cli.py`: Theme-adaptive `.euclid-graphic` SVG generator and `geometor-staudt` CLI (`summary`, `verify`, `build-figures`).

---

## Verification Commands

```bash
/home/phi/.local/bin/pytest
/home/phi/.local/bin/ruff check src demos scripts tests
/home/phi/.local/bin/publish build
```
