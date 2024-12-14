import pytest

from aoc.aoc_2024.python.ex_07 import main_func


@pytest.mark.parametrize(
    "filename, version, expected",
    [
        ("aoc/aoc_2024/inputs/07_test.txt", 1, 3749),
        ("aoc/aoc_2024/inputs/07.txt", 1, 2437272016585),
        ("aoc/aoc_2024/inputs/07_test.txt", 2, 11387),
        pytest.param(
            "aoc/aoc_2024/inputs/07.txt",
            2,
            162987117690649,
            marks=pytest.mark.skipif(True, reason="too slow"),
        ),
    ],
)
def test_main_func(filename, version, expected):
    assert main_func(filename, version) == expected
