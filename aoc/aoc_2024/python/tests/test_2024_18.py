import pytest

from aoc.aoc_2024.python.ex_18 import main_func


@pytest.mark.parametrize(
    "filename, version, size, n_bytes, expected",
    [
        ("aoc/aoc_2024/inputs/18_test.txt", 1, 6, 12, 22),
        ("aoc/aoc_2024/inputs/18.txt", 1, 70, 1024, 306),
        ("aoc/aoc_2024/inputs/18_test.txt", 2, 6, 12, (6, 1)),
        pytest.param(
            "aoc/aoc_2024/inputs/18.txt",
            2,
            70,
            1024,
            (38, 63),
            marks=pytest.mark.skipif(True, reason="bit slow"),
        ),
    ],
)
def test_main_func(filename, version, size, n_bytes, expected):
    assert main_func(filename, version, size, n_bytes) == expected
