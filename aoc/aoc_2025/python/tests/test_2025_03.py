import pytest

from aoc.aoc_2025.python.ex_03 import main_func


@pytest.mark.parametrize(
    "filename, version, expected",
    [
        ("aoc/aoc_2025/inputs/03_test.txt", 1, 357),
        ("aoc/aoc_2025/inputs/03.txt", 1, 17432),
        ("aoc/aoc_2025/inputs/03_test.txt", 2, 3121910778619),
        ("aoc/aoc_2025/inputs/03.txt", 2, 173065202451341),
    ],
)
def test_main_func(filename, version, expected):
    assert main_func(filename, version) == expected
