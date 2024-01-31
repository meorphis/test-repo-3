# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Required, TypedDict

__all__ = ["RerankCreateParams", "Document", "DocumentText"]


class RerankCreateParams(TypedDict, total=False):
    documents: Required[List[Document]]
    """
    A list of document objects or strings to rerank. If a document is provided the
    text fields is required and all other fields will be preserved in the response.
    The total max chunks (length of documents \\** max_chunks_per_doc) must be less
    than 10000.
    """

    query: Required[str]
    """The search query"""

    max_chunks_per_doc: int
    """The maximum number of chunks to produce internally from a document"""

    model: str
    """
    The identifier of the model to use, one of : `rerank-english-v2.0`,
    `rerank-multilingual-v2.0`
    """

    return_documents: bool
    """
    - If false, returns results without the doc text - the api will return a list of
      {index, relevance score} where index is inferred from the list passed into the
      request.
    - If true, returns results with the doc text passed in - the api will return an
      ordered list of {index, text, relevance score} where index + text refers to
      the list passed into the request.
    """

    top_n: int
    """
    The number of most relevant documents or indices to return, defaults to the
    length of the documents
    """


class DocumentText(TypedDict, total=False):
    text: Required[str]
    """The text of the document to rerank."""


Document = Union[str, DocumentText]
