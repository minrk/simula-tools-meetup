from pathlib import Path

here = Path(__file__).absolute().parent


def compute_priority(item: str) -> int:
    if item.isupper():
        return ord(item) - ord("A") + 27
    else:
        return ord(item) - ord("a") + 1


def compute_total(rucksack: str) -> int:
    fst = set(rucksack[: len(rucksack) // 2])
    snd = set(rucksack[len(rucksack) // 2 :])
    intersection = fst & snd
    if intersection:
        unique_item = (intersection).pop()
        return compute_priority(unique_item)
    else:
        return 0


def compute_total_part1(text: str) -> int:
    return sum(map(compute_total, map(str.strip, text.strip().split("\n"))))


def main() -> int:

    with open(here / "input.txt") as f:
        text = f.read()

    print(f"Part 1:\n{compute_total_part1(text)}")
    # print(f"Part 2:\n{compute_total_part2(text)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
else:
    import pytest

    EXAMPLE_INPUT = """
    vJrwpWtwJgWrhcsFMMfFFhFp
    jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
    PmmdzqPrVvPwwTWBwg
    wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
    ttgJtRGJQctTZtZT
    CrZsJsPPZsGzwwsLwLmpwMDw
    """

    def test_compute_total_part1():
        assert compute_total_part1(EXAMPLE_INPUT) == 157

    @pytest.mark.parametrize(
        ("rucksack", "expected_priority"),
        (
            ("vJrwpWtwJgWrhcsFMMfFFhFp", 16),
            ("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", 38),
            ("PmmdzqPrVvPwwTWBwg", 42),
            ("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", 22),
            ("ttgJtRGJQctTZtZT", 20),
            ("CrZsJsPPZsGzwwsLwLmpwMDw", 19),
        ),
    )
    def test_compute_total(rucksack, expected_priority):
        assert compute_total(rucksack) == expected_priority

    @pytest.mark.parametrize(
        ("letter", "expected_priority"), (("a", 1), ("z", 26), ("A", 27), ("Z", 52))
    )
    def test_compute_priority(letter, expected_priority):
        assert compute_priority(letter) == expected_priority
