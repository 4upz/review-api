from typing import TypedDict


class SearchResult(TypedDict):
    id: str
    title: str
    description: str
    image_url: str
    release_date: str
