import pytest

from aoc.aoc_2025.python.ex_10 import main_func


@pytest.mark.parametrize(
    "filename, version, expected",
    [
        ("aoc/aoc_2025/inputs/10_test.txt", 1, 7),
        ("aoc/aoc_2025/inputs/10.txt", 1, 502),
        ("aoc/aoc_2025/inputs/10_test.txt", 2, 33),
        pytest.param(
            "aoc/aoc_2025/inputs/10.txt",
            2,
            21467,
            marks=pytest.mark.skipif(True, reason="slow"),
        ),
    ],
)
def test_main_func(filename, version, expected):
    assert main_func(filename, version) == expected
