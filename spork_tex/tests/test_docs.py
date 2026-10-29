"""Tests for spork_tex.docs (where the documentation is installed) and its pointers elsewhere."""

from __future__ import annotations

import os
import subprocess
import sys

from spork_tex import REPO_URL, build, docs


def test_doc_files_exist_in_checkout():
    # In a source checkout every listed file is present (the design notes only exist there).
    for _desc, path in docs.DOC_FILES:
        assert os.path.exists(path), path
    assert os.path.basename(docs.REFERENCE_CARD) == "REFERENCE_CARD.md"


def test_docs_cli(tmp_path):
    # Run from an unrelated directory: paths are absolute, not relative to the cwd.
    run = lambda *a: subprocess.run([sys.executable, "-m", "spork_tex.docs", *a], cwd=tmp_path,
                                    capture_output=True, text=True, check=True).stdout
    assert run("--card") == docs.REFERENCE_CARD + "\n"
    out = run().splitlines()
    assert out[0] == f"spork_tex documentation ({REPO_URL}):"
    assert out[1].startswith("  reference card (start here):") and out[1].endswith(docs.REFERENCE_CARD)


def test_docs_skip_missing(monkeypatch, tmp_path):
    # An installed wheel has no plan_slides.md or worked example: those lines are left out.
    monkeypatch.setattr(docs, "DOC_FILES", [("card", docs.REFERENCE_CARD), ("gone", str(tmp_path / "nope.md"))])
    assert docs.doc_lines()[1:] == [f"  card: {docs.REFERENCE_CARD}"]


def test_build_help_points_at_reference_card():
    text = build.make_parser().format_help()
    assert "".join(text.split()).count("".join(docs.REFERENCE_CARD.split())) == 1  # argparse may wrap it
    assert "python3 -m spork_tex.docs" in " ".join(text.split())
