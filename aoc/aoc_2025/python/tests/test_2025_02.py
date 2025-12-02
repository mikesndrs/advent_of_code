import pytest

from aoc.aoc_2025.python.ex_02 import main_func


@pytest.mark.parametrize(
    "filename, version, expected",
    [
        ("aoc/aoc_2025/inputs/02_test.txt", 1, 1227775554),
        ("aoc/aoc_2025/inputs/02.txt", 1, 23534117921),
        ("aoc/aoc_2025/inputs/02_test.txt", 2, 4174379265),
        ("aoc/aoc_2025/inputs/02.txt", 2, 31755323497),
    ],
)
def test_main_func(filename, version, expected):
    assert main_func(filename, version) == expected

    assert main_func("aoc/aoc_2025/inputs/02_test.txt", 1) == 1227775554
    assert main_func("aoc/aoc_2025/inputs/02.txt", 1) == 23534117921
    # # Part 2
    assert main_func("aoc/aoc_2025/inputs/02_test.txt", 2) == 4174379265
    assert main_func("aoc/aoc_2025/inputs/02.txt", 2) == 31755323497
