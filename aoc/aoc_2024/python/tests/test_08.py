import pytest

from aoc.aoc_2024.python.ex_08 import main_func


@pytest.mark.parametrize(
    "filename, version, expected",
    [
        ("aoc/aoc_2024/inputs/08_test.txt", 1, 14),
        ("aoc/aoc_2024/inputs/08.txt", 1, 336),
        ("aoc/aoc_2024/inputs/08_test.txt", 2, 34),
        ("aoc/aoc_2024/inputs/08.txt", 2, 1131),
    ],
)
def test_main_func(filename, version, expected):
    assert main_func(filename, version) == expected
