#!/usr/bin/env python3
"""Regenerate all 8 standalone ``.euclid-graphic`` SVG figures for ``geometor/staudt``."""

from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
MODEL_SRC = REPO_ROOT.parent / "model" / "src"
for candidate in (REPO_ROOT / "src", MODEL_SRC):
    if str(candidate) not in sys.path:
        sys.path.insert(0, str(candidate))

from geometor.staudt.render import build_all_figures


def main() -> None:
    paths = build_all_figures()
    for p in paths:
        print(f"Wrote {p.relative_to(REPO_ROOT)} ({p.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
