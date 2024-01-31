# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List

import httpx

from ..types import RerankCreateResponse, rerank_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import (
    make_request_options,
)

__all__ = ["Rerank", "AsyncRerank"]


class Rerank(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RerankWithRawResponse:
        return RerankWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RerankWithStreamingResponse:
        return RerankWithStreamingResponse(self)

    def create(
        self,
        *,
        documents: List[rerank_create_params.Document],
        query: str,
        max_chunks_per_doc: int | NotGiven = NOT_GIVEN,
        model: str | NotGiven = NOT_GIVEN,
        return_documents: bool | NotGiven = NOT_GIVEN,
        top_n: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RerankCreateResponse:
        """
        This endpoint takes in a query and a list of texts and produces an ordered array
        with each text assigned a relevance score.

        Args:
          documents: A list of document objects or strings to rerank. If a document is provided the
              text fields is required and all other fields will be preserved in the response.
              The total max chunks (length of documents \\** max_chunks_per_doc) must be less
              than 10000.

          query: The search query

          max_chunks_per_doc: The maximum number of chunks to produce internally from a document

          model: The identifier of the model to use, one of : `rerank-english-v2.0`,
              `rerank-multilingual-v2.0`

          return_documents: - If false, returns results without the doc text - the api will return a list of
                {index, relevance score} where index is inferred from the list passed into the
                request.
              - If true, returns results with the doc text passed in - the api will return an
                ordered list of {index, text, relevance score} where index + text refers to
                the list passed into the request.

          top_n: The number of most relevant documents or indices to return, defaults to the
              length of the documents

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/rerank",
            body=maybe_transform(
                {
                    "documents": documents,
                    "query": query,
                    "max_chunks_per_doc": max_chunks_per_doc,
                    "model": model,
                    "return_documents": return_documents,
                    "top_n": top_n,
                },
                rerank_create_params.RerankCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RerankCreateResponse,
        )


class AsyncRerank(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRerankWithRawResponse:
        return AsyncRerankWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRerankWithStreamingResponse:
        return AsyncRerankWithStreamingResponse(self)

    async def create(
        self,
        *,
        documents: List[rerank_create_params.Document],
        query: str,
        max_chunks_per_doc: int | NotGiven = NOT_GIVEN,
        model: str | NotGiven = NOT_GIVEN,
        return_documents: bool | NotGiven = NOT_GIVEN,
        top_n: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RerankCreateResponse:
        """
        This endpoint takes in a query and a list of texts and produces an ordered array
        with each text assigned a relevance score.

        Args:
          documents: A list of document objects or strings to rerank. If a document is provided the
              text fields is required and all other fields will be preserved in the response.
              The total max chunks (length of documents \\** max_chunks_per_doc) must be less
              than 10000.

          query: The search query

          max_chunks_per_doc: The maximum number of chunks to produce internally from a document

          model: The identifier of the model to use, one of : `rerank-english-v2.0`,
              `rerank-multilingual-v2.0`

          return_documents: - If false, returns results without the doc text - the api will return a list of
                {index, relevance score} where index is inferred from the list passed into the
                request.
              - If true, returns results with the doc text passed in - the api will return an
                ordered list of {index, text, relevance score} where index + text refers to
                the list passed into the request.

          top_n: The number of most relevant documents or indices to return, defaults to the
              length of the documents

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/rerank",
            body=maybe_transform(
                {
                    "documents": documents,
                    "query": query,
                    "max_chunks_per_doc": max_chunks_per_doc,
                    "model": model,
                    "return_documents": return_documents,
                    "top_n": top_n,
                },
                rerank_create_params.RerankCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RerankCreateResponse,
        )


class RerankWithRawResponse:
    def __init__(self, rerank: Rerank) -> None:
        self._rerank = rerank

        self.create = to_raw_response_wrapper(
            rerank.create,
        )


class AsyncRerankWithRawResponse:
    def __init__(self, rerank: AsyncRerank) -> None:
        self._rerank = rerank

        self.create = async_to_raw_response_wrapper(
            rerank.create,
        )


class RerankWithStreamingResponse:
    def __init__(self, rerank: Rerank) -> None:
        self._rerank = rerank

        self.create = to_streamed_response_wrapper(
            rerank.create,
        )


class AsyncRerankWithStreamingResponse:
    def __init__(self, rerank: AsyncRerank) -> None:
        self._rerank = rerank

        self.create = async_to_streamed_response_wrapper(
            rerank.create,
        )
