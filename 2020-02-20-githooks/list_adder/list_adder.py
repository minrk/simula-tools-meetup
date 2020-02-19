def add(x, y):
    """Add two numbers

    Arguments
    ---------
    x : float
        First number
    y : float
        Second number

    Returns
    -------
    float
        The sum of x and y
    """
    for arg in [x, y]:
        assert isinstance(arg, float)
    return float(x + y)


def add_lists(list1, list2):
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
    if len(list1) != len(list2):
        msg = (
            "Elementwise additions of two lists of different sizes not "
            f"allowed. len(list1) = {len(list1)}, len(list2) == {len(list2)}"
        )
        raise ValueError(msg)
    return [add(x, y) for x, y in zip(list1, list2)]

