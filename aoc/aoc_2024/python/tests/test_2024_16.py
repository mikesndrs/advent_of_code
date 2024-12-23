import pytest

from aoc.aoc_2024.python.ex_16 import main_func


@pytest.mark.parametrize(
    "filename, version, expected",
    [
        ("aoc/aoc_2024/inputs/16_test_small.txt", 1, 7036),
        ("aoc/aoc_2024/inputs/16_test.txt", 1, 11048),
        pytest.param(
            "aoc/aoc_2024/inputs/16.txt",
            1,
            79404,
            marks=pytest.mark.skipif(True, reason="bit slow"),
        ),
        ("aoc/aoc_2024/inputs/16_test_small.txt", 2, 45),
        ("aoc/aoc_2024/inputs/16_test.txt", 2, 64),
        pytest.param(
            "aoc/aoc_2024/inputs/16.txt",
            2,
            451,
            marks=pytest.mark.skipif(True, reason="bit slow"),
        ),
    ],
)
def test_main_func(filename, version, expected):
    assert main_func(filename, version) == expected
