import pytest

from aoc.aoc_2024.python.ex_04 import main_func


@pytest.mark.parametrize(
    "filename, version, expected",
    [
        ("aoc/aoc_2024/inputs/04_test.txt", 1, 18),
        ("aoc/aoc_2024/inputs/04.txt", 1, 2500),
        ("aoc/aoc_2024/inputs/04_test.txt", 2, 9),
        ("aoc/aoc_2024/inputs/04.txt", 2, 1933),
    ],
)
def test_main_func(filename, version, expected):
    assert main_func(filename, version) == expected
