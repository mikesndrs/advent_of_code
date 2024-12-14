import pytest

from aoc.aoc_2024.python.ex_12 import main_func


@pytest.mark.parametrize(
    "filename, version, expected",
    [
        ("aoc/aoc_2024/inputs/12_test.txt", 1, 1930),
        ("aoc/aoc_2024/inputs/12.txt", 1, 1387004),
        ("aoc/aoc_2024/inputs/12_test.txt", 2, 1206),
        ("aoc/aoc_2024/inputs/12.txt", 2, 844198),
    ],
)
def test_main_func(filename, version, expected):
    assert main_func(filename, version) == expected
