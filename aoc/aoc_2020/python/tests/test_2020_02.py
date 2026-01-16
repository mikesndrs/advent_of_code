import pytest

from aoc.aoc_2020.python.ex_02 import main_func


@pytest.mark.parametrize(
    "filename, version, expected",
    [
        ("aoc/aoc_2020/inputs/02_test.txt", 1, 2),
        ("aoc/aoc_2020/inputs/02.txt", 1, 467),
        ("aoc/aoc_2020/inputs/02_test.txt", 2, 1),
        ("aoc/aoc_2020/inputs/02.txt", 2, 441),
    ],
)
def test_main_func(filename, version, expected):
    assert main_func(filename, version) == expected
