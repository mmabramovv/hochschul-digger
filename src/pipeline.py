from pathlib import Path
from typing import Final

from sqlmodel import Session

from .config import engine
from .parser import extract_subject
from .models import Subject

CURRICULUM: Final[str] = "INF"  # TODO?


def process_line(line: str, curriculum: str, session: Session) -> Subject:
    subject = extract_subject(line, curriculum)
    if not subject:
        return
    session.add(subject)
    return subject


def run_pipeline(file: Path):
    curriculum = CURRICULUM
    with open(file) as f:
        lines = f.readlines()

    with Session(engine) as session:
        for line in lines:
            process_line(line, curriculum, session)
        session.commit()
