"""spork_tex: shared paper/slides LaTeX toolchain (listing generator, styles, build driver).

Self-contained (stdlib only, Python 3.10); see README.md.

* ``python3 -m spork_tex SRC OUTDIR`` -- listing generator (`spork_tex.listing`)
* ``python3 -m spork_tex.build DIR ...`` -- build driver (`spork_tex.build`)
* ``python3 -m spork_tex.docs`` -- where the documentation is (start: REFERENCE_CARD.md)
* ``latex/*.tex`` -- styles copied into each document's ``copied_styles/``
"""

REPO_URL = "https://github.com/akeley98/spork_tex.git"
