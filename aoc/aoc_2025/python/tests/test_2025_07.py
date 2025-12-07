import pytest

from aoc.aoc_2025.python.ex_07 import main_func


@pytest.mark.parametrize(
    "filename, version, expected",
    [
        ("aoc/aoc_2025/inputs/07_test.txt", 1, 21),
        ("aoc/aoc_2025/inputs/07.txt", 1, 1613),
        ("aoc/aoc_2025/inputs/07_test.txt", 2, 40),
        ("aoc/aoc_2025/inputs/07.txt", 2, 48021610271997),
    ],
)
def test_main_func(filename, version, expected):
    assert main_func(filename, version) == expected
