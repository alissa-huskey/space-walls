"""Command Line Interface."""

from sys import stderr

from rich import print
from rich.console import Console
from rich.table import Table
from rich.traceback import install as rich_tracebacks
from typer import Typer

from space_walls import SpaceWallsProgramError, SpaceWallsUserError
from space_walls.config import Config


cli = Typer()
console = Console(stderr=True)
rich_tracebacks(show_locals=True)


def abort(e, status=1):
    """Print an error message and exit the program."""
    if hasattr(e, "status"):
        status = int(e.status)

    print(
        "\n[red]Woops![/red] This is embarssing. It looks like something unexpectedly failed.\n",
        file=stderr
    )
    console.print_exception(show_locals=True)

    exit(status)


@cli.command(name="list")
def ls():
    """List the current wallpapers."""
    cfg = Config()
    table = Table("Space", "Image")

    for img in cfg.images.values():
        table.add_row(str(img.space_number), img.image_path)

    print(table)


def run():
    try:
        cli()
    except SpaceWallsProgramError as e:
        abort(e)
    except SpaceWallsUserError as e:
        print("[red]Error[/red]", e)
        exit(int(e.status))
    except SystemExit:
        ...
    #  except BaseException as e:
    #      breakpoint()
    #      ...


if __name__ == "__main__":
    run()
