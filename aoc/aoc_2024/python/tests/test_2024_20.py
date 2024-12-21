import pytest

from aoc.aoc_2024.python.ex_20 import main_func


@pytest.mark.parametrize(
    "filename, version, cutoff, expected",
    [
        ("aoc/aoc_2024/inputs/20_test.txt", 1, 5, 16),
        ("aoc/aoc_2024/inputs/20_test.txt", 1, 20, 5),
        ("aoc/aoc_2024/inputs/20.txt", 1, 100, 1307),
        ("aoc/aoc_2024/inputs/20_test.txt", 2, 60, 129),
        ("aoc/aoc_2024/inputs/20_test.txt", 2, 70, 41),
        pytest.param(
            "aoc/aoc_2024/inputs/20.txt",
            2,
            100,
            986545,
            marks=pytest.mark.skipif(True, reason="bit slow"),
        ),
    ],
)
def test_main_func(filename, version, cutoff, expected):
    assert main_func(filename, version, cutoff) == expected
