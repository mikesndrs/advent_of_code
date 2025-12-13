import pytest

from aoc.aoc_2025.python.ex_11 import main_func


@pytest.mark.parametrize(
    "filename, version, expected",
    [
        ("aoc/aoc_2025/inputs/11_test.txt", 1, 5),
        ("aoc/aoc_2025/inputs/11.txt", 1, 749),
        ("aoc/aoc_2025/inputs/11_test2.txt", 2, 2),
        ("aoc/aoc_2025/inputs/11.txt", 2, 420257875695750),
    ],
)
def test_main_func(filename, version, expected):
    assert main_func(filename, version) == expected
