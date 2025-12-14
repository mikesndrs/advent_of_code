import pytest

from aoc.aoc_2020.python.ex_01 import main_func


@pytest.mark.parametrize(
    "filename, version, expected",
    [
        ("aoc/aoc_2020/inputs/01_test.txt", 1, 514579),
        ("aoc/aoc_2020/inputs/01.txt", 1, 542619),
        ("aoc/aoc_2020/inputs/01_test.txt", 2, 241861950),
        ("aoc/aoc_2020/inputs/01.txt", 2, 32858450),
    ],
)
def test_main_func(filename, version, expected):
    assert main_func(filename, version) == expected
