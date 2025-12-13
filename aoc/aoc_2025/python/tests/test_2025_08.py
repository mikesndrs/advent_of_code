import pytest

from aoc.aoc_2025.python.ex_08 import main_func


@pytest.mark.parametrize(
    "filename, version, n_connections, expected",
    [
        ("aoc/aoc_2025/inputs/08_test.txt", 1, 10, 40),
        ("aoc/aoc_2025/inputs/08.txt", 1, 1000, 131580),
        ("aoc/aoc_2025/inputs/08_test.txt", 2, 10, 25272),
        ("aoc/aoc_2025/inputs/08.txt", 2, 1000, 6844224),
    ],
)
def test_main_func(filename, version, n_connections, expected):
    assert main_func(filename, version, n_connections) == expected
