#!/usr/bin/env python3

from pathlib import Path

from sqlmodel import SQLModel
import typer

from .config import engine
from .models import *  # noqa: F403

app = typer.Typer(help="Hochschul-Digger")


@app.command()
def init_db():
    SQLModel.metadata.create_all(engine)
    typer.echo("DB initialized")


@app.command()
def main(
    filename: Path = typer.Argument(
        help="File taken as input",
        exists=True,
        file_okay=True,
        dir_okay=False,
        readable=True,
    ),
    foo: str = typer.Option(
        ...,
        "--foo",
        "-f",
        help="Mandatory option (bar)",
    ),
):
    typer.echo(typer.style("Done!", fg=typer.colors.GREEN, bold=True))


if __name__ == "__main__":
    app()
