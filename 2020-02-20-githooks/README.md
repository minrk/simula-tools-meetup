# Git pre-commit hooks

Sometimes it is a good idea to test your code whenever you perform a commit

Things you might want to test whenever you commit

- You are following the correct coding style

  - If you are working with other people then it is good practice to agree on the coding style
  - python: PEP8

- New changes does not break any core functionality

  - Run a minimal number tests

- Type checking
  - python: `mypy`

## Example code to illustrate pre-commit hooks

A sample of code is found in the folder [`list_adder`](list_adder). This is really a dummy example just to be used for illustrating pre-commit hooks (do not use this code for anything else :))

### Install

Make sure you what `virtualenv` installed

```
[sudo] python -m pip install virtualenv
```

Create a virtual environent

```
python -m virtualenv venv
```

Activate the virtual environment

```
source venv/bin/activate
```

Install the code in your newly created virtual environment

```
python -m pip install .
```

Note that if you plan to change the code that you install, then you should install the code in editable mode

```
python -m pip install -e .
```

This allows you to edit the code without having to install it again every time you want to try out your new changes.

## Checking for correct code style using `flake8`

```python
def add(x,y):
    return x+y
```

you should (according to PEP8), do

```python
def add(x, y):
    return x + y
```

Having the same coding style makes your code more readable and it prevents you for having unwanted

```
python3 -m pip install flake8
```

### Add flake8 as a pre-commit hook

Will run `flake8` every time you commit

1. Install `pre-commit` package

```
python -m pip install pre-commit
```

2. Create a file called `.pre-commit-config.yaml` and add the following content to it

```
repos:
  - repo: local
    hooks:
      - id: flake8
        name: flake8
        stages: [commit]
        language: system
        entry: python -m flake8
        types: [python]
        exclude: setup.py
```

3. Install the pre-commit hook

```
pre-commit install
```

4. Try to do some changes that violates PEP8, and commit them

Note: you can remove the pre-commit hook by executing

```
pre-commit uninstall
```

## Do not run pre-commit hook

You can choose not to run the pre-commit hook when comitting by passing the flag `--no-verify` to the `git commit` command, i.e

```
git commit -m "Do not use pre-commit hooks` --no-verify
```

## More info about githooks

https://pre-commit.com

```
man githooks
```

## Coding style using `black` formatter

```
python3 -m pip install black
```

Autoformat code

```
python -m black script.py
```

or just check consistent coding style

```
python -m black --check script.py
```

## Checking for consistent import order using `isort`

```
python3 -m pip install isort
```

Autoformat code

```
python -m black script.py
```

or just check consistent import order

```
python -m black --check script.py
```

## Static type checker using `mypy`

You can add types to variables and run `mypy` to verify that you are always passing correct arguments to functions

```python
from typing import Optional

def add(x: float, y: Optional[float] = None) -> float:
    """Add two numbers

    Arguments
    ---------
    x : float
        First number
    y : float
        Second number. If not provided it will default to 1

    Returns
    -------
    float
        The sum of x and y
    """
    if y is None:
        y = 1
    return float(x + y)
```

```
python3 -m pip install mypy
```

Check types by running

```
python3 -m mypy list_adder demo
```

## Full pre-commit config

.pre-commit-config

```
repos:
  - repo: local
    hooks:
      - id: flake8
        name: flake8
        stages: [commit]
        language: system
        entry: python -m flake8
        types: [python]

      - id: isort
        name: isort
        stages: [commit]
        language: system
        entry: python -m isort -y
        types: [python]

      - id: black
        name: black
        stages: [commit]
        language: system
        entry: python -m black
        types: [python]

      - id: mypy
        name: mypy
        stages: [commit]
        language: system
        entry: python -m mypy
        types: [python]

```

## Customize pre-commit hooks using `setup.cfg`

```
[isort]
multi_line_output=3
include_trailing_comma=True
force_grid_wrap=0
use_parentheses=True
line_length=88
skip=venv

[flake8]
exclude = docs
ignore = E203, E266, E501, W503, E731
max-line-length = 88
max-complexity = 18
select = B,C,E,F,W,T4

[mypy]
files=list_adder, demo,tests
ignore_missing_imports=true
```
