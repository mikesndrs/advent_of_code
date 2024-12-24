import pytest

from aoc.aoc_2024.python.ex_24 import main_func


@pytest.mark.parametrize(
    "filename, version, expected",
    [
        ("aoc/aoc_2024/inputs/24_test_small.txt", 1, 4),
        ("aoc/aoc_2024/inputs/24_test.txt", 1, 2024),
        ("aoc/aoc_2024/inputs/24.txt", 1, 60614602965288),
        ("aoc/aoc_2024/inputs/24.txt", 2, 'cgr,hpc,hwk,qmd,tnt,z06,z31,z37'),
    ],
)
def test_main_func(filename, version, expected):
    assert main_func(filename, version) == expected
