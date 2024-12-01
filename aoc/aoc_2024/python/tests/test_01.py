import pytest

from aoc.aoc_2024.python.ex_01 import main_func


@pytest.mark.parametrize(
    "filename, version, expected",
    [
        ("aoc/aoc_2024/inputs/01_test.txt", 1, 11),
        ("aoc/aoc_2024/inputs/01.txt", 1, 1830467),
        ("aoc/aoc_2024/inputs/01_test.txt", 2, 31),
        ("aoc/aoc_2024/inputs/01.txt", 2, 26674158),
    ],
)
def test_main_func(filename, version, expected):
    assert main_func(filename, version) == expected
