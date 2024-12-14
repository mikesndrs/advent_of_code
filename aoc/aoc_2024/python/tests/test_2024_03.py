import pytest

from aoc.aoc_2024.python.ex_03 import main_func


@pytest.mark.parametrize(
    "filename, version, expected",
    [
        ("aoc/aoc_2024/inputs/03_test.txt", 1, 161),
        ("aoc/aoc_2024/inputs/03.txt", 1, 174960292),
        ("aoc/aoc_2024/inputs/03_test.txt", 2, 48),
        ("aoc/aoc_2024/inputs/03.txt", 2, 56275602),
    ],
)
def test_main_func(filename, version, expected):
    assert main_func(filename, version) == expected
