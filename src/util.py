from typing import NoReturn
import sys

import typer


def _e(e: Exception) -> str:
    return f"\n\t{e.__class__.__name__}: {str(e)}"


def err(msg: str, e: Exception | None = None):
    if e is not None:
        msg += _e(e)
    typer.secho(msg, err=True, fg=typer.colors.RED)


def log(msg: str):
    typer.secho(msg, err=True, fg=typer.colors.GREEN)


def die(msg: str, e: Exception | None = None) -> NoReturn:
    err(msg, e)
    sys.exit(1)
