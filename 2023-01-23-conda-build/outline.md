# conda-build

conda-build is how you build conda packages!


## Background

- what is conda?
- what is a conda package?
- how are conda-packages relocatable (rpath)?


## conda-build basics

- install: `conda install conda-build` and/or `boa`
- build with `conda build recipe_dir` where `recipe_dir` contains `met.yaml` (or `conda mambabuild` to be a bit faster if you have `boa`)

Gist:

1. setup an environment
2. fetch some files
3. run a command (usually something like `./configure --prefix=$PREFIX && make install`)
4. record changes to the environment

### Example recipes

- simplest (just make a file) (`conda build ./simplest`)
- python (pip install)
- clib (compilers, dependencies)
- python-ext (compilers + Python)
- staged-recipes recipes/dolfinx_mpc/


## conda-forge

- community-maintained infrastructure for building (thousands!) packages on CI
