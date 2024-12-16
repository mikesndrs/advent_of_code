import pytest

from aoc.aoc_2024.python.ex_15 import main_func


@pytest.mark.parametrize(
    "filename, version, expected",
    [
        ("aoc/aoc_2024/inputs/15_test_small.txt", 1, 2028),
        ("aoc/aoc_2024/inputs/15_test.txt", 1, 10092),
        ("aoc/aoc_2024/inputs/15.txt", 1, 1486930),
        ("aoc/aoc_2024/inputs/15_test.txt", 2, 9021),
        ("aoc/aoc_2024/inputs/15.txt", 2, 1492011),
    ],
)
def test_main_func(filename, version, expected):
    assert main_func(filename, version) == expected
