"""CLI commands"""

import runpy

import click

from aoc import get_project_root


@click.command()
@click.argument("year", type=int)
@click.argument("number", type=int)
def run(year: int, number: int) -> None:
    """Run exercise for a given year and number"""
    module_str = f"aoc.aoc_{year}.python.ex_{number:02}"
    runpy.run_module(module_str, run_name="__main__")


@click.command()
@click.argument("year", type=int)
@click.argument("number", type=int)
def profile(year: int, number: int) -> None:
    """Profile exercise for a given year and number"""
    print(f"profile {year} {number}")


@click.command()
@click.argument("year", type=int)
@click.argument("number", type=int)
@click.option("--language", default="python", help="Programming language", type=str)
def init(year: int, number: int, language: str) -> None:
    """Initialize all the necessary files for a given year and number"""
    print(f"init {year} {number}")
    root = get_project_root()
    base = root / "aoc" / f"aoc_{year}"
    template_base = root / "aoc" / "templates"
    for filename, template_name in [
        (base / "python" / f"ex_{number:02}.py", "code.py"),
        (base / "inputs" / f"{number:02}.txt", None),
        (base / "inputs" / f"{number:02}_test.txt", None),
        (base / "python" / "tests" / f"test_{year}_{number:02}.py", "test.py"),
    ]:
        if not filename.exists():
            if template_name is not None:
                with open(template_base / template_name, mode="r") as f:
                    content = f.read()
                content = content.replace("<year>", str(year))
                content = content.replace("<number>", str(number).zfill(2))
                with open(filename, mode="w") as f:
                    f.write(content)
            else:
                filename.touch()
        print(filename)


@click.group()
def cli() -> None:
    pass


cli.add_command(run)
cli.add_command(profile)
cli.add_command(init)

if __name__ == "__main__":
    cli()
