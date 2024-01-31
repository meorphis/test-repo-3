# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List

import httpx

from ..types import DetectLanguageCreateResponse, detect_language_create_params
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

__all__ = ["DetectLanguage", "AsyncDetectLanguage"]


class DetectLanguage(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DetectLanguageWithRawResponse:
        return DetectLanguageWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DetectLanguageWithStreamingResponse:
        return DetectLanguageWithStreamingResponse(self)

    def create(
        self,
        *,
        texts: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DetectLanguageCreateResponse:
        """
        This endpoint identifies which language each of the provided texts is written
        in.

        Args:
          texts: List of strings to run the detection on.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/detect-language",
            body=maybe_transform({"texts": texts}, detect_language_create_params.DetectLanguageCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DetectLanguageCreateResponse,
        )


class AsyncDetectLanguage(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDetectLanguageWithRawResponse:
        return AsyncDetectLanguageWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDetectLanguageWithStreamingResponse:
        return AsyncDetectLanguageWithStreamingResponse(self)

    async def create(
        self,
        *,
        texts: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DetectLanguageCreateResponse:
        """
        This endpoint identifies which language each of the provided texts is written
        in.

        Args:
          texts: List of strings to run the detection on.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/detect-language",
            body=maybe_transform({"texts": texts}, detect_language_create_params.DetectLanguageCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DetectLanguageCreateResponse,
        )


class DetectLanguageWithRawResponse:
    def __init__(self, detect_language: DetectLanguage) -> None:
        self._detect_language = detect_language

        self.create = to_raw_response_wrapper(
            detect_language.create,
        )


class AsyncDetectLanguageWithRawResponse:
    def __init__(self, detect_language: AsyncDetectLanguage) -> None:
        self._detect_language = detect_language

        self.create = async_to_raw_response_wrapper(
            detect_language.create,
        )


class DetectLanguageWithStreamingResponse:
    def __init__(self, detect_language: DetectLanguage) -> None:
        self._detect_language = detect_language

        self.create = to_streamed_response_wrapper(
            detect_language.create,
        )


class AsyncDetectLanguageWithStreamingResponse:
    def __init__(self, detect_language: AsyncDetectLanguage) -> None:
        self._detect_language = detect_language

        self.create = async_to_streamed_response_wrapper(
            detect_language.create,
        )
