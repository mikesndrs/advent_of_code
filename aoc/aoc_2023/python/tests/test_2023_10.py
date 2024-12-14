import pytest

from aoc.aoc_2023.python.ex_10 import main_func


@pytest.mark.parametrize(
    "filename, version, expected",
    [
        ("aoc/aoc_2023/inputs/10_test.txt", 1, 4),
        ("aoc/aoc_2023/inputs/10_test_2.txt", 1, 8),
        ("aoc/aoc_2023/inputs/10.txt", 1, 7086),
        ("aoc/aoc_2023/inputs/10_test.txt", 2, 1),
        ("aoc/aoc_2023/inputs/10_test_2.txt", 2, 1),
        ("aoc/aoc_2023/inputs/10_test_3.txt", 2, 4),
        ("aoc/aoc_2023/inputs/10.txt", 2, 317),
    ],
)
def test_main_func(filename, version, expected):
    assert main_func(filename, version) == expected
