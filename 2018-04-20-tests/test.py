import sys


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

def test_simple_list():
    data = [1, 2, 3, 4, 5, 2, 3, 3]
    assert mode(data) == 3


def test_something_else():
    print(f"hello from ${sys.version}")
