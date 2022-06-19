# Publish you package to PyPi

In other to make it easier for others to install your software you can upload you package to [pypi](https://pypi.org). That want you can `pip` install your package.

We will try to add a new package to pypi, namely [`pyscholar`](https://github.com/finsberg/pyscholar) which is a side-project I have for extracting statistics from google scholar.

All the information you need can be found in the [python documentation](https://packaging.python.org/en/latest/tutorials/packaging-projects/)

---
Demo of `pyscholar`

We would like to do
```
python -m pip install pyscholar
```

---
## Step 1: Make your package installable

You need structure your code in a certain way in order to make it possible to install. For example you might have a `setup.py` and then you can run
```
python -m pip install .
```
inside the root directory in order to install it.
In order to do this you can
- read the [python documentation](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
- use an existing project that you know work and modify that to you use-case
- use a [cookiecutter template](https://cookiecutter.readthedocs.io/en/stable/README.html). See [this blog](https://pycon.switowski.com/03-project-structure-2-parts/cookiecutter/) for an example.

---

## Step 2: Create an account on pypi
In order to upload your package to pypi you need to create an account there first. 

---

## Step 3: Build source distribution and wheels

Now we need to create the files that should be uploaded to pypi. These are typically a wheel and a source distributions.

First install `build`
```
python -m pip install build
```

Next run
```
python -m build
```
This will create a new folder called `dist` containing the wheel and the source distribution.


## Step 4: Upload wheels to pypi
The next thing you need to do is to upload the wheel and the source distribution to pypi. To do this you need to first install `twine`
```
python -m twine
```
and then run the following command
```
twine upload dist/*
```

---

## Extra

### Tag and update version automatically using `bump2version`
In stead of manually updating the version in the `setup.cfg` and creating the `tag` you can use a tool like [`bump2version`](https://pypi.org/project/bump2version/) to do this.

### Set up github actions to publish your wheels when there is a new release / tag

There is a whole sections about this at the [python docs](https://packaging.python.org/en/latest/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/)

You can also see a working example [here](https://github.com/ComputationalPhysiology/simcardems/blob/master/.github/workflows/main.yml)


### If your package compiles code

If your package compiles code as a part of the build/installation process (e.g you have a C-extension) then you need to make a separate wheel for each platform and architecture (e.g linux, mac, mac ARM etc). To ease this process you can use [cibuildwheel](https://cibuildwheel.readthedocs.io/en/stable/). See [ap_feautres](https://github.com/ComputationalPhysiology/ap_features/blob/master/.github/workflows/deploy.yml) for an example.



