# File generated from our OpenAPI spec by Stainless.

from typing import List

from .._models import BaseModel

__all__ = ["SearchQueriesOnlyResponse", "SearchQuery"]


class SearchQuery(BaseModel):
    generation_id: str
    """Unique identifier for the generated search query.

    Useful for submitting feedback.
    """

    text: str
    """The text of the search query."""


class SearchQueriesOnlyResponse(BaseModel):
    search_queries: List[SearchQuery]
    """Generated search queries, meant to be used as part of the RAG flow."""
