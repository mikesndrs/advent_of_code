import pytest
from aoc_<year>.python.ex_<number> import main_func


@pytest.mark.parametrize("filename, version, expected", [
    ("<year>/inputs/<number>_test.txt", 1, 0),
    # ("<year>/inputs/<number>.txt", 1, 0),
    # ("<year>/inputs/<number>_test.txt", 2, 0),
    # ("<year>/inputs/<number>.txt", 2, 0),
])
def test_main_func(filename, version, expected):
    assert main_func(filename, version) == expected
