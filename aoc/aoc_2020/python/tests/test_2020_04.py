import pytest

from aoc.aoc_2020.python.ex_04 import main_func


@pytest.mark.parametrize(
    "filename, version, expected",
    [
        ("aoc/aoc_2020/inputs/04_test.txt", 1, 2),
        ("aoc/aoc_2020/inputs/04.txt", 1, 245),
        ("aoc/aoc_2020/inputs/04_test.txt", 2, 2),
        ("aoc/aoc_2020/inputs/04.txt", 2, 133),
    ],
)
def test_main_func(filename, version, expected):
    assert main_func(filename, version) == expected
