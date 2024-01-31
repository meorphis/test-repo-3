# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["EmbedCreateResponse", "Meta", "MetaAPIVersion"]


class MetaAPIVersion(BaseModel):
    version: str

    is_deprecated: Optional[bool] = None

    is_experimental: Optional[bool] = None


class Meta(BaseModel):
    api_version: Optional[List[MetaAPIVersion]] = None

    warnings: Optional[List[str]] = None


class EmbedCreateResponse(BaseModel):
    id: str

    embeddings: List[List[float]]
    """An array of embeddings, where each embedding is an array of floats.

    The length of the `embeddings` array will be the same as the length of the
    original `texts` array.
    """

    texts: List[str]
    """The text entries for which embeddings were returned."""

    meta: Optional[List[Meta]] = None
