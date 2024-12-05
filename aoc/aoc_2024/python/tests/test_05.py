import pytest

from aoc.aoc_2024.python.ex_05 import main_func


@pytest.mark.parametrize(
    "filename, version, expected",
    [
        ("aoc/aoc_2024/inputs/05_test.txt", 1, 143),
        ("aoc/aoc_2024/inputs/05.txt", 1, 5588),
        ("aoc/aoc_2024/inputs/05_test.txt", 2, 123),
        ("aoc/aoc_2024/inputs/05.txt", 2, 5331),
    ],
)
def test_main_func(filename, version, expected):
    assert main_func(filename, version) == expected
