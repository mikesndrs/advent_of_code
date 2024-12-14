import pytest

from aoc.aoc_2024.python.ex_10 import main_func


@pytest.mark.parametrize(
    "filename, version, expected",
    [
        ("aoc/aoc_2024/inputs/10_test.txt", 1, 36),
        ("aoc/aoc_2024/inputs/10.txt", 1, 501),
        ("aoc/aoc_2024/inputs/10_test.txt", 2, 81),
        ("aoc/aoc_2024/inputs/10.txt", 2, 1017),
    ],
)
def test_main_func(filename, version, expected):
    assert main_func(filename, version) == expected
