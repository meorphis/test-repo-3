# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["DetokenizeCreateParams"]


class DetokenizeCreateParams(TypedDict, total=False):
    tokens: Required[List[int]]
    """The list of tokens to be detokenized."""

    model: str
    """An optional parameter to provide the model name.

    This will ensure that the detokenization is done by the tokenizer used by that
    model.
    """
