import pytest

from aoc.aoc_2024.python.ex_13 import main_func


@pytest.mark.parametrize(
    "filename, version, expected",
    [
        ("aoc/aoc_2024/inputs/13_test.txt", 1, 480),
        ("aoc/aoc_2024/inputs/13.txt", 1, 29388),
        ("aoc/aoc_2024/inputs/13_test.txt", 2, 875318608908),
        ("aoc/aoc_2024/inputs/13.txt", 2, 99548032866004),
    ],
)
def test_main_func(filename, version, expected):
    assert main_func(filename, version) == expected
