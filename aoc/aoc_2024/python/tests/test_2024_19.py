import pytest

from aoc.aoc_2024.python.ex_19 import main_func


@pytest.mark.parametrize(
    "filename, version, expected",
    [
        ("aoc/aoc_2024/inputs/19_test.txt", 1, 6),
        ("aoc/aoc_2024/inputs/19.txt", 1, 311),
        ("aoc/aoc_2024/inputs/19_test.txt", 2, 16),
        ("aoc/aoc_2024/inputs/19.txt", 2, 616234236468263),
    ],
)
def test_main_func(filename, version, expected):
    assert main_func(filename, version) == expected
