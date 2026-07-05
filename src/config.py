from typing import Final

from sqlmodel import create_engine

DB_FILE: Final[str] = "digger.db"
engine = create_engine(f"sqlite:///{DB_FILE}")
