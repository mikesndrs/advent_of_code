import pytest

from aoc.aoc_2024.python.ex_09 import main_func


@pytest.mark.parametrize(
    "filename, version, expected",
    [
        ("aoc/aoc_2024/inputs/09_test.txt", 1, 1928),
        ("aoc/aoc_2024/inputs/09.txt", 1, 6382875730645),
        ("aoc/aoc_2024/inputs/09_test.txt", 2, 2858),
        pytest.param(
            "aoc/aoc_2024/inputs/09.txt",
            2,
            6420913943576,
            marks=pytest.mark.skipif(True, reason="too slow"),
        ),
    ],
)
def test_main_func(filename, version, expected):
    assert main_func(filename, version) == expected
