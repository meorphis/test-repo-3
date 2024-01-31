# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["DetectLanguageCreateParams"]


class DetectLanguageCreateParams(TypedDict, total=False):
    texts: Required[List[str]]
    """List of strings to run the detection on."""
