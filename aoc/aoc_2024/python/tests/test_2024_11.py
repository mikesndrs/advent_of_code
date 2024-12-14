import pytest

from aoc.aoc_2024.python.ex_11 import main_func


@pytest.mark.parametrize(
    "filename, version, expected",
    [
        ("aoc/aoc_2024/inputs/11_test.txt", 1, 55312),
        ("aoc/aoc_2024/inputs/11.txt", 1, 198089),
        ("aoc/aoc_2024/inputs/11_test.txt", 2, 65601038650482),
        ("aoc/aoc_2024/inputs/11.txt", 2, 236302670835517),
    ],
)
def test_main_func(filename, version, expected):
    assert main_func(filename, version) == expected
