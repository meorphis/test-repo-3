# File generated from our OpenAPI spec by Stainless.

from typing import Union

from .streamed_chat_response import StreamedChatResponse
from .non_streamed_chat_response import NonStreamedChatResponse
from .search_queries_only_response import SearchQueriesOnlyResponse

__all__ = ["ChatCreateResponse"]

ChatCreateResponse = Union[NonStreamedChatResponse, StreamedChatResponse, SearchQueriesOnlyResponse]
