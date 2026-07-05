from .const import TISS_BASE_URL

import httpx

client = httpx.Client(base_url=TISS_BASE_URL)


def get(url: str) -> str | None:
    res = client.get(url)
    if res.status_code != 200:
        print("oops?")
        return None
    return res.text
