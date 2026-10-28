"""spork_tex: shared paper/slides LaTeX toolchain (listing generator, styles, build driver).

Self-contained (stdlib only, Python 3.10); see README.md.

* ``python3 -m spork_tex SRC OUTDIR`` -- listing generator (`spork_tex.listing`)
* ``python3 -m spork_tex.build DIR ...`` -- build driver (`spork_tex.build`)
* ``latex/*.tex`` -- styles copied into each document's ``copied_styles/``
"""
