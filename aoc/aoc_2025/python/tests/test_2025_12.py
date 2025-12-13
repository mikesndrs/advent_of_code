import pytest

from aoc.aoc_2025.python.ex_12 import main_func


@pytest.mark.parametrize(
    "filename, version, expected",
    [
        pytest.param(
            "aoc/aoc_2025/inputs/12_test.txt",
            1,
            2,
            marks=pytest.mark.skipif(True, reason="Not solved"),
        ),
        ("aoc/aoc_2025/inputs/12.txt", 1, 485),
    ],
)
def test_main_func(filename, version, expected):
    assert main_func(filename, version) == expected
