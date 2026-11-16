"""Sphinx & photon-platform/publish configuration for ``geometor/staudt``."""

from __future__ import annotations

import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[1]
_GEOMETOR_ROOT = _REPO_ROOT.parent
for _extra_path in (
    _REPO_ROOT / "src",
    _GEOMETOR_ROOT / "model" / "src",
    _GEOMETOR_ROOT / ".venv" / "lib" / "python3.13" / "site-packages",
):
    if _extra_path.exists() and str(_extra_path) not in sys.path:
        sys.path.insert(0, str(_extra_path))

from photon_platform.publish.global_conf import *

import geometor.staudt as module

version = module.__version__

org = "geometor"
org_name = "GEOMETOR"

repo = "staudt"
repo_name = "staudt"

setup_globals(org, org_name, repo, repo_name)

site_title = "Karl Georg Christian von Staudt"
project = site_title
html_title = f"{site_title} • {org_name}"
blog_title = site_title
author = "Karl Georg Christian von Staudt (ed. phi ARCHITECT)"
copyright = "1847–1857 Public Domain; 2026 GEOMETOR Critical Apparatus & Symbolic Library"

html_static_path = ["_static"]

# AutoAPI configuration for src/geometor/staudt
autoapi_dirs = [str(_REPO_ROOT / "src" / "geometor")]
autoapi_add_toctree_entry = False
exclude_patterns.append("modules/api/geometor/staudt/index.rst")
suppress_warnings = ["autoapi.python_import_resolution", "toc.not_included"]

# Offline-first cross-repository intersphinx mappings (replace network-only defaults)
intersphinx_mapping = {}
for _sister in (
    "pasch",
    "euclid",
    "elements",
    "pappus",
    "hilbert",
    "bertrand-russell",
    "hoenen",
    "altshiller-court",
    "lemoine",
):
    _inv = _GEOMETOR_ROOT / _sister / "docs" / "objects.inv"
    if _inv.exists():
        intersphinx_mapping[_sister.replace("-", "_")] = (
            f"https://geometor.github.io/{_sister}/",
            str(_inv),
        )
