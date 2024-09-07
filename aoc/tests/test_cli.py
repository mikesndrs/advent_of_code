from distutils.dir_util import copy_tree
from pathlib import Path
from unittest.mock import patch

import click.testing
import pytest

from aoc import get_project_root
from aoc.aoc_cli import cli


@pytest.fixture
def runner():
    return click.testing.CliRunner()


def test_run_no_args(runner, tmpdir):
    """Test whether no arguments fails"""
    result = runner.invoke(cli, ["run"])

    assert result.exit_code > 0


def test_run_args(runner, tmpdir):
    """Test whether no arguments fails"""
    result = runner.invoke(cli, ["run", "2023", "8"])

    assert result.exit_code == 0


def test_profile_no_args(runner, tmpdir):
    """Test whether no arguments fails"""
    result = runner.invoke(cli, ["profile"])

    assert result.exit_code > 0


def test_profile_args(runner, tmpdir):
    """Test whether no arguments fails"""
    result = runner.invoke(cli, ["profile", "2023", "8"])

    assert result.exit_code == 0


def test_init_no_args(runner, tmpdir):
    """Test whether no arguments fails"""
    result = runner.invoke(cli, ["init"])

    assert result.exit_code > 0


def test_init_args(runner, tmpdir):
    """Test whether with arguments works"""
    root = get_project_root()
    copy_tree(str(root / "aoc" / "templates"), str(Path(tmpdir) / "aoc" / "templates"))
    target_dir = Path(tmpdir) / "aoc" / "aoc_2023"
    source_dir = root / "aoc" / "aoc_2023"
    (target_dir / "python" / "tests").mkdir(parents=True)
    (target_dir / "inputs").mkdir(parents=True)
    with patch(
        "aoc.aoc_cli.get_project_root",
        return_value=Path(tmpdir),
    ):
        result = runner.invoke(cli, ["init", "2023", "30"])

    assert result.exit_code == 0
    assert Path.exists(target_dir / "python" / "ex_30.py")
    assert not Path.exists(source_dir / "python" / "ex_30.py")
