import pytest

from aoc.aoc_2024.python.ex_06 import main_func


@pytest.mark.parametrize(
    "filename, version, expected",
    [
        ("aoc/aoc_2024/inputs/06_test.txt", 1, 41),
        ("aoc/aoc_2024/inputs/06.txt", 1, 4982),
        ("aoc/aoc_2024/inputs/06_test.txt", 2, 6),
        pytest.param(
            "aoc/aoc_2024/inputs/06.txt",
            2,
            1663,
            marks=pytest.mark.skipif(True, reason="too slow"),
        ),
    ],
)
def test_main_func(filename, version, expected):
    assert main_func(filename, version) == expected
