import pytest

from aoc.aoc_2020.python.ex_03 import main_func


@pytest.mark.parametrize(
    "filename, version, expected",
    [
        ("aoc/aoc_2020/inputs/03_test.txt", 1, 0),
        ("aoc/aoc_2020/inputs/03.txt", 1, 200),
        ("aoc/aoc_2020/inputs/03_test.txt", 2, 3),
        ("aoc/aoc_2020/inputs/03.txt", 2, 3737923200),
    ],
)
def test_main_func(filename, version, expected):
    assert main_func(filename, version) == expected
