from typing import Optional, List


def add(x: float, y: Optional[float] = 1) -> float:
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
    return float(x + y)


def add_lists(lst1: List[float], lst2: List[float]) -> List[float]:
    """Elementwise addition of lists

    Arguments
    ---------
    list1: list
        The first list
    list2 : list
        The seond list

    Returns
    -------
    list
        Elementwise sum of the two lists
    """
    if len(lst1) != len(lst2):
        msg = (
            "Elementwise additions of two lists of different sizes not "
            f"allowed. len(list1) = {len(lst1)}, len(list2) == {len(lst2)}"
        )
        raise ValueError(msg)
    return [add(x, y) for x, y in zip(lst1, lst2)]

