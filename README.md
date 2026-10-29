# spork_tex

`spork_tex`: one directory per document holds a paper (`main.tex`) and any number of Beamer decks that share
figures, style, and code listings cut out of real source files (checked by a command of your choice, e.g. a compiler).

The name is a legacy of its origin in the Exo-GPU ("spork") project; the package itself does not depend on Exo.

## Install (dev mode)

```bash
cd ~/Documents/spork_tex
python3 -m pip install --user -e '.[test]'
```

Then, from any directory:

```bash
python3 -m spork_tex.build <doc dir> [--slides DECK] ...   # build driver (--help)
python3 -m spork_tex SRC OUTDIR                             # listing generator alone
```

Needs `xelatex` on PATH (and `pdftoppm` for `--png`).
`python3 -m spork_tex.docs` prints where the documentation is installed (`--card`: just the reference card),
so documents using spork_tex can point there instead of assuming a checkout location.

Repository: https://github.com/akeley98/spork_tex.git

## Layout

* [spork_tex/](spork_tex/): the package. Start at [spork_tex/REFERENCE_CARD.md](spork_tex/REFERENCE_CARD.md),
  then [PRIMER.md](spork_tex/PRIMER.md) (walkthrough) and [README.md](spork_tex/README.md) (listing directives in depth).
* [spork_tex/beamer_nyc25_test/](spork_tex/beamer_nyc25_test/): worked example document. Its `tex_build.json` checks
  `samples.py` with `exocc`, so building it needs Exo installed.
* [plan_slides.md](plan_slides.md): design doc and implementation notes (history: dated entries);
  [plan_slides_human_wishlist.md](plan_slides_human_wishlist.md): the original requirements.

## Tests

```bash
cd ~/Documents/spork_tex && python3 -m pytest
```

LaTeX-level tests are skipped when `xelatex` is missing.
