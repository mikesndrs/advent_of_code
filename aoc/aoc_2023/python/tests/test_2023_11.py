import pytest

from aoc.aoc_2023.python.ex_11 import main_func


@pytest.mark.parametrize(
    "filename, version, expected",
    [
        ("aoc/aoc_2023/inputs/11_test.txt", 2, 374),
        ("aoc/aoc_2023/inputs/11.txt", 2, 9918828),
        ("aoc/aoc_2023/inputs/11_test.txt", 10, 1030),
        ("aoc/aoc_2023/inputs/11_test.txt", 100, 8410),
        ("aoc/aoc_2023/inputs/11.txt", 1000000, 692506533832),
    ],
)
def test_main_func(filename, version, expected):
    assert main_func(filename, version) == expected
