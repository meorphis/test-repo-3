# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["TokenizeCreateResponse", "Meta", "MetaAPIVersion"]


class MetaAPIVersion(BaseModel):
    version: str

    is_deprecated: Optional[bool] = None

    is_experimental: Optional[bool] = None


class Meta(BaseModel):
    api_version: Optional[List[MetaAPIVersion]] = None

    warnings: Optional[List[str]] = None


class TokenizeCreateResponse(BaseModel):
    token_strings: List[str]

    tokens: List[int]
    """An array of tokens, where each token is an integer."""

    meta: Optional[List[Meta]] = None
