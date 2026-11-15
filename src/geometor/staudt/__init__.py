"""Exact symbolic straightedge-only projective geometry, von Staudt's Algebra of Throws,
and Moritz Pasch's planar order axiomatics for GEOMETOR.
"""

from __future__ import annotations

__version__ = "0.1.4"

from geometor.staudt.concordance import (
    ConcordanceEntry,
    SourceWitness,
    get_repo_root,
    load_concordance,
    load_sources_manifest,
    verify_source_witnesses,
)
from geometor.staudt.pasch import (
    PaschAuditResult,
    demonstrate_euclid_i16_pasch_gap,
    demonstrate_euclid_i21_pasch_gap,
    demonstrate_pasch_axiom,
)
from geometor.staudt.projective import (
    assert_straightedge_only,
    is_between,
    is_collinear,
    pair_separates,
    point_from_abscissa,
    projective_abscissa,
)
from geometor.staudt.quadrangle import (
    construct_harmonic_fourth_straightedge,
    prove_symbolic_quadrangle_uniqueness,
    verify_quadrangle_independence,
)
from geometor.staudt.throws import (
    construct_harmonic_scale,
    construct_parallel_straightedge,
    construct_von_staudt_addition,
    construct_von_staudt_multiplication,
    verify_golden_throw_identity,
)

__all__ = [
    "ConcordanceEntry",
    "PaschAuditResult",
    "SourceWitness",
    "__version__",
    "assert_straightedge_only",
    "construct_harmonic_fourth_straightedge",
    "construct_harmonic_scale",
    "construct_parallel_straightedge",
    "construct_von_staudt_addition",
    "construct_von_staudt_multiplication",
    "demonstrate_euclid_i16_pasch_gap",
    "demonstrate_euclid_i21_pasch_gap",
    "demonstrate_pasch_axiom",
    "get_repo_root",
    "is_between",
    "is_collinear",
    "load_concordance",
    "load_sources_manifest",
    "pair_separates",
    "point_from_abscissa",
    "projective_abscissa",
    "prove_symbolic_quadrangle_uniqueness",
    "verify_golden_throw_identity",
    "verify_quadrangle_independence",
    "verify_source_witnesses",
]
