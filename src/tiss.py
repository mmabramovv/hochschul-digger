from .const import TISS_BASE_URL

import httpx
from selectolax.parser import HTMLParser

client = httpx.Client(base_url=TISS_BASE_URL)


def get(url: str) -> str | None:
    res = client.get(url)
    if res.status_code != 200:
        print("oops?")
        return None
    return res.text


def parse_course_xml(xml: str) -> dict[str, str | float] | None:
    if not xml:
        return None

    tree = HTMLParser(xml)
    type_node = tree.css_first("courseType")
    sws_node = tree.css_first("weeklyHours")

    if not type_node or not sws_node:
        return None

    return {
        "subject_type": type_node.text(),
        "sws": float(sws_node.text()),
    }
