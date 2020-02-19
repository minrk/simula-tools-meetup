from list_adder import list_adder_mypy as list_adder


def demo_mypy1():
    """Try to use the wrong function to add two lists
    """
    lst1 = [1, 3, 5, 2]
    lst2 = [6, 2, 7, 1]

    # Mypy will spot this error
    lst_sum = list_adder.add(lst1, lst2)
    # We should instead be doing
    # lst_sum = list_adder.add_lists(lst1, lst2)
    print(lst_sum)


def demo_mypy2():
    """Try to use the wrong type of arguments.
    Adding two strings
    """

    s1 = "Hello "
    s2 = "World!"
    # This does not work
    s = list_adder.add(s1, s2)
    print(s)


if __name__ == "__main__":
    demo_mypy1()
    demo_mypy2()
