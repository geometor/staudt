"""Cross-corpus concordance loader and SHA-256 archival source witness verifier for
``geometor.staudt``.
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

__all__ = [
    "ConcordanceEntry",
    "SourceWitness",
    "get_repo_root",
    "load_concordance",
    "load_sources_manifest",
    "verify_source_witnesses",
]


def get_repo_root() -> Path:
    """Return the root directory of the ``geometor/staudt`` repository."""
    return Path(__file__).resolve().parents[3]


@dataclass(frozen=True)
class ConcordanceEntry:
    """Single locus cross-reference across the GEOMETOR historical and formal canon."""

    id: str
    treatise: str
    locus_de: str
    title: str
    codex_ref: str
    cross_refs: dict[str, str]
    summary: str


@dataclass(frozen=True)
class SourceWitness:
    """Archival public-domain primary German text witness tracked by SHA-256."""

    id: str
    author: str
    work: str
    edition: str
    year: int
    language: str
    license: str
    relative_path: str
    sha256: str
    bytes: int


def load_concordance(repo_root: Path | None = None) -> list[ConcordanceEntry]:
    """Load structured cross-repository concordance entries from ``resources/staudt/concordance.json``."""
    root = repo_root or get_repo_root()
    path = root / "resources" / "staudt" / "concordance.json"
    raw = json.loads(path.read_text(encoding="utf-8"))
    return [
        ConcordanceEntry(
            id=item["id"],
            treatise=item["treatise"],
            locus_de=item["locus_de"],
            title=item["title"],
            codex_ref=item["codex_ref"],
            cross_refs=dict(item["cross_refs"]),
            summary=item["summary"],
        )
        for item in raw["entries"]
    ]


def load_sources_manifest(repo_root: Path | None = None) -> list[SourceWitness]:
    """Load archival primary source metadata from ``resources/staudt/sources_manifest.json``."""
    root = repo_root or get_repo_root()
    path = root / "resources" / "staudt" / "sources_manifest.json"
    raw = json.loads(path.read_text(encoding="utf-8"))
    return [
        SourceWitness(
            id=w["id"],
            author=w["author"],
            work=w["work"],
            edition=w["edition"],
            year=int(w["year"]),
            language=w["language"],
            license=w["license"],
            relative_path=w["relative_path"],
            sha256=w["sha256"],
            bytes=int(w["bytes"]),
        )
        for w in raw["witnesses"]
    ]


def verify_source_witnesses(repo_root: Path | None = None) -> dict[str, Any]:
    """Verify existence, byte size, and SHA-256 digest of every primary source witness."""
    root = repo_root or get_repo_root()
    witnesses = load_sources_manifest(root)
    results: list[dict[str, Any]] = []
    all_ok = True
    for w in witnesses:
        fpath = root / w.relative_path
        if not fpath.is_file():
            all_ok = False
            results.append({"id": w.id, "ok": False, "error": f"Missing file: {w.relative_path}"})
            continue
        data = fpath.read_bytes()
        digest = hashlib.sha256(data).hexdigest()
        size_ok = len(data) == w.bytes and len(data) > 0
        hash_ok = digest == w.sha256
        ok = size_ok and hash_ok
        if not ok:
            all_ok = False
        results.append(
            {
                "id": w.id,
                "ok": ok,
                "bytes": len(data),
                "expected_bytes": w.bytes,
                "sha256": digest,
                "expected_sha256": w.sha256,
            }
        )
    return {"all_ok": all_ok, "count": len(witnesses), "witnesses": results}
