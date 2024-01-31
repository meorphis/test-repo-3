# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..types import TokenizeCreateResponse, tokenize_create_params
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

__all__ = ["Tokenize", "AsyncTokenize"]


class Tokenize(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TokenizeWithRawResponse:
        return TokenizeWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TokenizeWithStreamingResponse:
        return TokenizeWithStreamingResponse(self)

    def create(
        self,
        *,
        text: str,
        model: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TokenizeCreateResponse:
        """
        This endpoint splits input text into smaller units called tokens using byte-pair
        encoding (BPE). To learn more about tokenization and byte pair encoding, see the
        tokens page.

        Args:
          text: The string to be tokenized, the minimum text length is 1 character, and the
              maximum text length is 65536 characters.

          model: An optional parameter to provide the model name. This will ensure that the
              tokenization uses the tokenizer used by that model.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/tokenize",
            body=maybe_transform(
                {
                    "text": text,
                    "model": model,
                },
                tokenize_create_params.TokenizeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TokenizeCreateResponse,
        )


class AsyncTokenize(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTokenizeWithRawResponse:
        return AsyncTokenizeWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTokenizeWithStreamingResponse:
        return AsyncTokenizeWithStreamingResponse(self)

    async def create(
        self,
        *,
        text: str,
        model: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TokenizeCreateResponse:
        """
        This endpoint splits input text into smaller units called tokens using byte-pair
        encoding (BPE). To learn more about tokenization and byte pair encoding, see the
        tokens page.

        Args:
          text: The string to be tokenized, the minimum text length is 1 character, and the
              maximum text length is 65536 characters.

          model: An optional parameter to provide the model name. This will ensure that the
              tokenization uses the tokenizer used by that model.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/tokenize",
            body=maybe_transform(
                {
                    "text": text,
                    "model": model,
                },
                tokenize_create_params.TokenizeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TokenizeCreateResponse,
        )


class TokenizeWithRawResponse:
    def __init__(self, tokenize: Tokenize) -> None:
        self._tokenize = tokenize

        self.create = to_raw_response_wrapper(
            tokenize.create,
        )


class AsyncTokenizeWithRawResponse:
    def __init__(self, tokenize: AsyncTokenize) -> None:
        self._tokenize = tokenize

        self.create = async_to_raw_response_wrapper(
            tokenize.create,
        )


class TokenizeWithStreamingResponse:
    def __init__(self, tokenize: Tokenize) -> None:
        self._tokenize = tokenize

        self.create = to_streamed_response_wrapper(
            tokenize.create,
        )


class AsyncTokenizeWithStreamingResponse:
    def __init__(self, tokenize: AsyncTokenize) -> None:
        self._tokenize = tokenize

        self.create = async_to_streamed_response_wrapper(
            tokenize.create,
        )
