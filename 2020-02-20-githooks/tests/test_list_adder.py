import numpy as np
import pytest

from list_adder import list_adder


@pytest.mark.parametrize("execution_number", range(3))
def test_add(execution_number):
    x = np.random.uniform(0, 100)
    y = np.random.uniform(0, 100)
    assert np.isclose(list_adder.add(x, y), x + y)


@pytest.mark.parametrize("length", range(3))
def test_add_lists(length):
    lst1 = np.random.uniform(0, 100, size=length)
    lst2 = np.random.uniform(0, 100, size=length)
    assert np.isclose(
        list_adder.add_lists(lst1.tolist(), lst2.tolist()), lst1 + lst2
    ).all()


def test_add_lists_raises_valueerror_when_unequal_length():

    with pytest.raises(ValueError):
        list_adder.add_lists(
            np.random.uniform(0, 100, size=10), np.random.uniform(0, 100, size=6)
        )


if __name__ == "__main__":
    test_add_lists(10)
