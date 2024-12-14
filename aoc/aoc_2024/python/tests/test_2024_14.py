import pytest

from aoc.aoc_2024.python.ex_14 import main_func


@pytest.mark.parametrize(
    "filename, version, grid_size, expected",
    [
        ("aoc/aoc_2024/inputs/14_test.txt", 1, (11, 7), 12),
        ("aoc/aoc_2024/inputs/14.txt", 1, (101, 103), 218965032),
        pytest.param(
            "aoc/aoc_2024/inputs/14.txt",
            2,
            (101, 103),
            7037,
            marks=pytest.mark.skipif(True, reason="bit slow"),
        ),
    ],
)
def test_main_func(filename, version, grid_size, expected):
    assert main_func(filename, version, grid_size) == expected
