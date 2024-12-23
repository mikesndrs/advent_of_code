import pytest

from aoc.aoc_2024.python.ex_21 import main_func


@pytest.mark.parametrize(
    "filename, version, expected",
    [
        ("aoc/aoc_2024/inputs/21_test.txt", 1, 126384),
        ("aoc/aoc_2024/inputs/21.txt", 1, 219366),
        ("aoc/aoc_2024/inputs/21_test.txt", 2, 154115708116294),
        ("aoc/aoc_2024/inputs/21.txt", 2, 271631192020464),
    ],
)
def test_main_func(filename, version, expected):
    assert main_func(filename, version) == expected
