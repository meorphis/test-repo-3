# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TokenizeCreateParams"]


class TokenizeCreateParams(TypedDict, total=False):
    text: Required[str]
    """
    The string to be tokenized, the minimum text length is 1 character, and the
    maximum text length is 65536 characters.
    """

    model: str
    """An optional parameter to provide the model name.

    This will ensure that the tokenization uses the tokenizer used by that model.
    """
