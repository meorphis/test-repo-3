# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List

import httpx

from ..types import DetokenizeCreateResponse, detokenize_create_params
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

__all__ = ["Detokenize", "AsyncDetokenize"]


class Detokenize(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DetokenizeWithRawResponse:
        return DetokenizeWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DetokenizeWithStreamingResponse:
        return DetokenizeWithStreamingResponse(self)

    def create(
        self,
        *,
        tokens: List[int],
        model: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DetokenizeCreateResponse:
        """
        This endpoint takes tokens using byte-pair encoding and returns their text
        representation. To learn more about tokenization and byte pair encoding, see the
        tokens page.

        Args:
          tokens: The list of tokens to be detokenized.

          model: An optional parameter to provide the model name. This will ensure that the
              detokenization is done by the tokenizer used by that model.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/detokenize",
            body=maybe_transform(
                {
                    "tokens": tokens,
                    "model": model,
                },
                detokenize_create_params.DetokenizeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DetokenizeCreateResponse,
        )


class AsyncDetokenize(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDetokenizeWithRawResponse:
        return AsyncDetokenizeWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDetokenizeWithStreamingResponse:
        return AsyncDetokenizeWithStreamingResponse(self)

    async def create(
        self,
        *,
        tokens: List[int],
        model: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DetokenizeCreateResponse:
        """
        This endpoint takes tokens using byte-pair encoding and returns their text
        representation. To learn more about tokenization and byte pair encoding, see the
        tokens page.

        Args:
          tokens: The list of tokens to be detokenized.

          model: An optional parameter to provide the model name. This will ensure that the
              detokenization is done by the tokenizer used by that model.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/detokenize",
            body=maybe_transform(
                {
                    "tokens": tokens,
                    "model": model,
                },
                detokenize_create_params.DetokenizeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DetokenizeCreateResponse,
        )


class DetokenizeWithRawResponse:
    def __init__(self, detokenize: Detokenize) -> None:
        self._detokenize = detokenize

        self.create = to_raw_response_wrapper(
            detokenize.create,
        )


class AsyncDetokenizeWithRawResponse:
    def __init__(self, detokenize: AsyncDetokenize) -> None:
        self._detokenize = detokenize

        self.create = async_to_raw_response_wrapper(
            detokenize.create,
        )


class DetokenizeWithStreamingResponse:
    def __init__(self, detokenize: Detokenize) -> None:
        self._detokenize = detokenize

        self.create = to_streamed_response_wrapper(
            detokenize.create,
        )


class AsyncDetokenizeWithStreamingResponse:
    def __init__(self, detokenize: AsyncDetokenize) -> None:
        self._detokenize = detokenize

        self.create = async_to_streamed_response_wrapper(
            detokenize.create,
        )
