# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["DetectLanguageCreateResponse", "Meta", "MetaAPIVersion", "Result"]


class MetaAPIVersion(BaseModel):
    version: str

    is_deprecated: Optional[bool] = None

    is_experimental: Optional[bool] = None


class Meta(BaseModel):
    api_version: Optional[List[MetaAPIVersion]] = None

    warnings: Optional[List[str]] = None


class Result(BaseModel):
    language_code: Optional[str] = None

    language_name: Optional[str] = None


class DetectLanguageCreateResponse(BaseModel):
    meta: Optional[List[Meta]] = None

    results: Optional[List[Result]] = None
    """List of languages, one per input text"""
