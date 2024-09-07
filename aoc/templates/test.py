import pytest

from aoc.aoc_<year>.python.ex_<number> import main_func


@pytest.mark.parametrize("filename, version, expected", [
    ("aoc/aoc_<year>/inputs/<number>_test.txt", 1, 0),
    # (aoc/aoc_"<year>/inputs/<number>.txt", 1, 0),
    # ("aoc/aoc_<year>/inputs/<number>_test.txt", 2, 0),
    # ("aoc/aoc_<year>/inputs/<number>.txt", 2, 0),
])
def test_main_func(filename, version, expected):
    assert main_func(filename, version) == expected
