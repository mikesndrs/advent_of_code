import pytest

from aoc.aoc_2024.python.ex_22 import main_func


@pytest.mark.parametrize(
    "filename, version, expected",
    [
        ("aoc/aoc_2024/inputs/22_test.txt", 1, 37327623),
        ("aoc/aoc_2024/inputs/22.txt", 1, 19927218456),
        ("aoc/aoc_2024/inputs/22_test.txt", 2, 25),
        ("aoc/aoc_2024/inputs/22_test_2.txt", 2, 23),
        pytest.param(
            "aoc/aoc_2024/inputs/22.txt",
            2,
            2189,
            marks=pytest.mark.skipif(True, reason="bit slow"),
        ),
    ],
)
def test_main_func(filename, version, expected):
    assert main_func(filename, version) == expected
