import pytest

from aoc.aoc_2025.python.ex_06 import main_func


@pytest.mark.parametrize(
    "filename, version, expected",
    [
        ("aoc/aoc_2025/inputs/06_test.txt", 1, 0),
        # ("aoc/aoc_2025/inputs/06.txt", 1, 0),
        # ("aoc/aoc_2025/inputs/06_test.txt", 2, 0),
        # ("aoc/aoc_2025/inputs/06.txt", 2, 0),
    ],
)
def test_main_func(filename, version, expected):
    assert main_func(filename, version) == expected
