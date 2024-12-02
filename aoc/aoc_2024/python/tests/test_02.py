import pytest

from aoc.aoc_2024.python.ex_02 import main_func


@pytest.mark.parametrize(
    "filename, version, expected",
    [
        ("aoc/aoc_2024/inputs/02_test.txt", 1, 2),
        ("aoc/aoc_2024/inputs/02.txt", 1, 526),
        ("aoc/aoc_2024/inputs/02_test.txt", 2, 4),
        ("aoc/aoc_2024/inputs/02.txt", 2, 566),
    ],
)
def test_main_func(filename, version, expected):
    assert main_func(filename, version) == expected
