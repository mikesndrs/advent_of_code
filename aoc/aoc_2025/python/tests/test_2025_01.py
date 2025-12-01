import pytest

from aoc.aoc_2025.python.ex_01 import main_func


@pytest.mark.parametrize(
    "filename, version, expected",
    [
        ("aoc/aoc_2025/inputs/01_test.txt", 1, 3),
        ("aoc/aoc_2025/inputs/01.txt", 1, 1135),
        ("aoc/aoc_2025/inputs/01_test.txt", 2, 6),
        ("aoc/aoc_2025/inputs/01.txt", 2, 6558),
    ],
)
def test_main_func(filename, version, expected):
    assert main_func(filename, version) == expected
