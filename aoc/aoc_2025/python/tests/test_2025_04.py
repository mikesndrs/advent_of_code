import pytest

from aoc.aoc_2025.python.ex_04 import main_func


@pytest.mark.parametrize(
    "filename, version, expected",
    [
        ("aoc/aoc_2025/inputs/04_test.txt", 1, 13),
        ("aoc/aoc_2025/inputs/04.txt", 1, 1409),
        ("aoc/aoc_2025/inputs/04_test.txt", 2, 43),
        ("aoc/aoc_2025/inputs/04.txt", 2, 8366),
    ],
)
def test_main_func(filename, version, expected):
    assert main_func(filename, version) == expected
