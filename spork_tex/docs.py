"""``python3 -m spork_tex.docs``: print where the spork_tex documentation is installed.

Documents that use spork_tex shouldn't assume where the package lives (a checkout under
~/Documents, site-packages, ...); their comments point here instead.

    python3 -m spork_tex.docs           # table of documentation files (absolute paths)
    python3 -m spork_tex.docs --card    # only the reference card's path, e.g. for $(...)
"""

from __future__ import annotations

import argparse
import os
import sys

from . import REPO_URL

PACKAGE_DIR = os.path.dirname(os.path.abspath(__file__))
REFERENCE_CARD = os.path.join(PACKAGE_DIR, "REFERENCE_CARD.md")

# (description, path); the design notes exist only in a source checkout (outside the package).
DOC_FILES = [
    ("reference card (start here)", REFERENCE_CARD),
    ("primer (walkthrough)", os.path.join(PACKAGE_DIR, "PRIMER.md")),
    ("listing directives", os.path.join(PACKAGE_DIR, "README.md")),
    ("style macros, colors, TikZ keys", os.path.join(PACKAGE_DIR, "latex", "spork_style.tex")),
    ("worked example document", os.path.join(PACKAGE_DIR, "beamer_nyc25_test")),
    ("design notes (source checkout only)", os.path.join(os.path.dirname(PACKAGE_DIR), "plan_slides.md")),
]


def doc_lines() -> list[str]:
    present = [(d, p) for d, p in DOC_FILES if os.path.exists(p)]
    width = max(len(d) for d, _p in present) + 1
    lines = [f"spork_tex documentation ({REPO_URL}):"]
    lines.extend(f"  {d + ':':<{width}} {p}" for d, p in present)
    return lines


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="python3 -m spork_tex.docs",
                                description="Print where the spork_tex documentation is installed.")
    p.add_argument("--card", action="store_true", help="print only the reference card's path")
    args = p.parse_args(argv)
    print(REFERENCE_CARD if args.card else "\n".join(doc_lines()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
