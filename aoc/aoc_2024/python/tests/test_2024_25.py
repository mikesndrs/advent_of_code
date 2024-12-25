import pytest

from aoc.aoc_2024.python.ex_25 import main_func


@pytest.mark.parametrize(
    "filename, version, expected",
    [
        ("aoc/aoc_2024/inputs/25_test.txt", 1, 3),
        ("aoc/aoc_2024/inputs/25.txt", 1, 3116),
    ],
)
def test_main_func(filename, version, expected):
    assert main_func(filename, version) == expected
