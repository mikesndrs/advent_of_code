import pytest

from aoc.aoc_2025.python.ex_05 import main_func


@pytest.mark.parametrize(
    "filename, version, expected",
    [
        ("aoc/aoc_2025/inputs/05_test.txt", 1, 3),
        ("aoc/aoc_2025/inputs/05.txt", 1, 770),
        ("aoc/aoc_2025/inputs/05_test.txt", 2, 14),
        ("aoc/aoc_2025/inputs/05.txt", 2, 357674099117260),
    ],
)
def test_main_func(filename, version, expected):
    assert main_func(filename, version) == expected
