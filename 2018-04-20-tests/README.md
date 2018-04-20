
# Testing

Writing tests for your code is useful! `py.test` is a one of several tools you can use for testingpython code, and if you call it without any options it will scan the current folder (and subfolders) for test (typically things that start with `test`).

Given a function that looks like this (not efficient code!):

```python
def mode(data):
    counts = {}
    for number in data:
        if number not in counts:
            counts[number] = 0
        counts[number] = counts[number] + 1

    max_number = None
    max_count = 0
    for number, count in counts.items():
        if count > max_count:
            max_number = number
            max_count = count
    return max_number
```

A simple test function could look like this:

```python
def test_simple_list():
    data = [1, 2, 3, 4, 5, 2, 3, 3]
    assert mode(data) == 3
```

To use pytest to run this test with pytest:
- place the test code in appropriate files in your repo (maybe in a "tests" folder, with files named `test_<what it tests>.py`)
- install pytest `pip install pytest`
- run pytest `py.test` or `python -m pytest`


## Helpful options for pytest

- `-k <expression>`: Only run tests that match the expression. Matches filenames and/or test function names. E.g. `py.test -k simple_list` would select the test above.
- `--pdb`: When a test fails, dumps you into a `pdb` debug session at the point of failure. This can allow you to inspect the variables close to the point of failure, and also inspect the callstack when the failure is due to an exception in your code.
- `--lf`: Run only the tests that failed the last time (runs all tests if no failures previously). This can allow you to focus only on checking if you have fixed the previously failing tests. PS: Always run a full test afterwards!


## Fixtures

Code to run before / after a test:

```python
import pytest

@pytest.fixture
def my_fixture():
    # This is run before the test
    my_setup()
    
    yield <value>  # the optional value will be passed to the test function
    
    # This is run after the test
    my_cleanup()


def test_my_code(my_fixture):
    value = my_function()
    assert value == my_fixture  # my_fixture will have the value yielded from the fixture
```

Fixtures can also depend on each other:

```python
import pytest

@pytest.fixture
def my_fixture1():
    my_setup()
    yield 
    my_cleanup()

@pytest.fixture
def my_fixture2(my_fixture1):
    some_other_setup()
    
def test_my_code(my_fixture2):
    # Here, my_fixture1 and my_fixture2 setup have been called
    assert 1 + 1 == 5

## Coverage

Use [pytest-cov](http://pytest-cov.readthedocs.io)! `pip install pytest-cov`. `py.test --cov=mymodule`.


## Continuous integration

Good resources:
- [Travis](http://travis-ci.org): Linux / OSX testing
- [Appveyor](http://appveyor.com): Windows testing
- [Circle CI](https://circleci.com): Linux / OSX testing
