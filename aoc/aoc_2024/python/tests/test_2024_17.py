import pytest

from aoc.aoc_2024.python.ex_17 import main_func


@pytest.mark.parametrize(
    "filename, version, expected",
    [
        ("aoc/aoc_2024/inputs/17_test.txt", 1, "4,6,3,5,6,3,5,2,1,0"),
        ("aoc/aoc_2024/inputs/17.txt", 1, "2,1,3,0,5,2,3,7,1"),
        ("aoc/aoc_2024/inputs/17.txt", 2, "107416732707226"),
    ],
)
def test_main_func(filename, version, expected):
    assert main_func(filename, version) == expected
