import re

from .models import Subject

# Bsp: "+Betriebssysteme (6,0 ECTS)"
ECTS_PATTERN = re.compile(r"([+*]?)(.+?)\s*\((\d+,\d+)\s*ECTS\)")


def extract_subject(line: str, curriculum: str) -> Subject | None:
    match = ECTS_PATTERN.search(line)
    if not match:
        return None

    prefix, name, ects_str = match.groups()
    ects = float(ects_str.replace(",", "."))

    category = "Pflicht"
    if prefix == "+":
        category = "Wahl_Enge"
    if prefix == "*":
        category = "Wahl_Breite"

    return Subject(
        curriculum=curriculum, name=name.strip(), subject_category=category, ects=ects
    )
