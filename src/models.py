from sqlmodel import Field, SQLModel
from sqlmodel.main import Undefined


class Subject(SQLModel, table=True):
    id: int = Field(default=Undefined, primary_key=True)
    curriculum: str
    name: str
    subject_type: str | None = None
    subject_category: str
    semester_recommended: int | None = None
    sws: float | None = None
    ects: float
    requirements: str | None = None
    notes: str | None = None
