import pytest

from aoc.aoc_2025.python.ex_09 import main_func


@pytest.mark.parametrize(
    "filename, version, expected",
    [
        ("aoc/aoc_2025/inputs/09_test.txt", 1, 50),
        ("aoc/aoc_2025/inputs/09.txt", 1, 4763509452),
        ("aoc/aoc_2025/inputs/09_test.txt", 2, 24),
        pytest.params(
            "aoc/aoc_2025/inputs/09.txt",
            2,
            1516897893,
            marks=pytest.mark.skipif(True, reason="slow"),
        ),
    ],
)
def test_main_func(filename, version, expected):
    assert main_func(filename, version) == expected
