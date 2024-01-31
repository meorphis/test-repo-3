# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["RerankCreateResponse", "Result", "ResultDocument", "Meta", "MetaAPIVersion"]


class ResultDocument(BaseModel):
    text: str
    """The text of the document to rerank"""


class Result(BaseModel):
    index: int
    """The index of the input document"""

    relevance_score: float
    """A relevance score assigned to the ranking"""

    document: Optional[ResultDocument] = None
    """The doc object which was ranked"""


class MetaAPIVersion(BaseModel):
    version: Optional[str] = None


class Meta(BaseModel):
    api_version: Optional[MetaAPIVersion] = None


class RerankCreateResponse(BaseModel):
    results: List[Result]
    """An ordered list of ranked documents"""

    id: Optional[str] = None

    meta: Optional[Meta] = None
