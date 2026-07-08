#!/usr/bin/env python3

from pathlib import Path

from sqlmodel import SQLModel
import typer


from .config import engine
from .models import *  # noqa: F403
from .pipeline import run_pipeline
from .util import log

app = typer.Typer(help="Hochschul-Digger")


@app.command()
def init_db():
    SQLModel.metadata.create_all(engine)
    typer.echo("DB initialized")


@app.command()
def main(
    filename: Path = typer.Argument(
        help="Verordnungstext",
        exists=True,
        file_okay=True,
        dir_okay=False,
        readable=True,
    ),
):
    run_pipeline(filename)
    log("Imported fine")


if __name__ == "__main__":
    app()
