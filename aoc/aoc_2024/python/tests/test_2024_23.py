import pytest

from aoc.aoc_2024.python.ex_23 import main_func


@pytest.mark.parametrize(
    "filename, version, expected",
    [
        ("aoc/aoc_2024/inputs/23_test.txt", 1, 7),
        ("aoc/aoc_2024/inputs/23.txt", 1, 1314),
        ("aoc/aoc_2024/inputs/23_test.txt", 2, 'co,de,ka,ta'),
        ("aoc/aoc_2024/inputs/23.txt", 2, 'bg,bu,ce,ga,hw,jw,nf,nt,ox,tj,uu,vk,wp'),
    ],
)
def test_main_func(filename, version, expected):
    assert main_func(filename, version) == expected
