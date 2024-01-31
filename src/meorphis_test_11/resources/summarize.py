# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import SummarizeCreateResponse, summarize_create_params
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

__all__ = ["Summarize", "AsyncSummarize"]


class Summarize(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SummarizeWithRawResponse:
        return SummarizeWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SummarizeWithStreamingResponse:
        return SummarizeWithStreamingResponse(self)

    def create(
        self,
        *,
        text: str,
        additional_command: str | NotGiven = NOT_GIVEN,
        extractiveness: Literal["low", "medium", "high"] | NotGiven = NOT_GIVEN,
        format: Literal["paragraph", "bullets"] | NotGiven = NOT_GIVEN,
        length: Literal["short", "medium", "long"] | NotGiven = NOT_GIVEN,
        model: Literal["command", "command-light"] | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SummarizeCreateResponse:
        """
        This endpoint generates a summary in English for a given text.

        Args:
          text: The text to generate a summary for. Can be up to 100,000 characters long.
              Currently the only supported language is English.

          additional_command: A free-form instruction for modifying how the summaries get generated. Should
              complete the sentence "Generate a summary \\__". Eg. "focusing on the next steps"
              or "written by Yoda"

          extractiveness: One of `low`, `medium`, `high`, or `auto`, defaults to `auto`. Controls how
              close to the original text the summary is. `high` extractiveness summaries will
              lean towards reusing sentences verbatim, while `low` extractiveness summaries
              will tend to paraphrase more. If `auto` is selected, the best option will be
              picked based on the input text.

          format: One of `paragraph`, `bullets`, or `auto`, defaults to `auto`. Indicates the
              style in which the summary will be delivered - in a free form paragraph or in
              bullet points. If `auto` is selected, the best option will be picked based on
              the input text.

          length: One of `short`, `medium`, `long`, or `auto` defaults to `auto`. Indicates the
              approximate length of the summary. If `auto` is selected, the best option will
              be picked based on the input text.

          model: The identifier of the model to generate the summary with. Currently available
              models are `command` (default), `command-nightly` (experimental),
              `command-light`, and `command-light-nightly` (experimental). Smaller, "light"
              models are faster, while larger models will perform better.

          temperature: Ranges from 0 to 5. Controls the randomness of the output. Lower values tend to
              generate more “predictable” output, while higher values tend to generate more
              “creative” output. The sweet spot is typically between 0 and 1.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/summarize",
            body=maybe_transform(
                {
                    "text": text,
                    "additional_command": additional_command,
                    "extractiveness": extractiveness,
                    "format": format,
                    "length": length,
                    "model": model,
                    "temperature": temperature,
                },
                summarize_create_params.SummarizeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SummarizeCreateResponse,
        )


class AsyncSummarize(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSummarizeWithRawResponse:
        return AsyncSummarizeWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSummarizeWithStreamingResponse:
        return AsyncSummarizeWithStreamingResponse(self)

    async def create(
        self,
        *,
        text: str,
        additional_command: str | NotGiven = NOT_GIVEN,
        extractiveness: Literal["low", "medium", "high"] | NotGiven = NOT_GIVEN,
        format: Literal["paragraph", "bullets"] | NotGiven = NOT_GIVEN,
        length: Literal["short", "medium", "long"] | NotGiven = NOT_GIVEN,
        model: Literal["command", "command-light"] | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SummarizeCreateResponse:
        """
        This endpoint generates a summary in English for a given text.

        Args:
          text: The text to generate a summary for. Can be up to 100,000 characters long.
              Currently the only supported language is English.

          additional_command: A free-form instruction for modifying how the summaries get generated. Should
              complete the sentence "Generate a summary \\__". Eg. "focusing on the next steps"
              or "written by Yoda"

          extractiveness: One of `low`, `medium`, `high`, or `auto`, defaults to `auto`. Controls how
              close to the original text the summary is. `high` extractiveness summaries will
              lean towards reusing sentences verbatim, while `low` extractiveness summaries
              will tend to paraphrase more. If `auto` is selected, the best option will be
              picked based on the input text.

          format: One of `paragraph`, `bullets`, or `auto`, defaults to `auto`. Indicates the
              style in which the summary will be delivered - in a free form paragraph or in
              bullet points. If `auto` is selected, the best option will be picked based on
              the input text.

          length: One of `short`, `medium`, `long`, or `auto` defaults to `auto`. Indicates the
              approximate length of the summary. If `auto` is selected, the best option will
              be picked based on the input text.

          model: The identifier of the model to generate the summary with. Currently available
              models are `command` (default), `command-nightly` (experimental),
              `command-light`, and `command-light-nightly` (experimental). Smaller, "light"
              models are faster, while larger models will perform better.

          temperature: Ranges from 0 to 5. Controls the randomness of the output. Lower values tend to
              generate more “predictable” output, while higher values tend to generate more
              “creative” output. The sweet spot is typically between 0 and 1.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/summarize",
            body=maybe_transform(
                {
                    "text": text,
                    "additional_command": additional_command,
                    "extractiveness": extractiveness,
                    "format": format,
                    "length": length,
                    "model": model,
                    "temperature": temperature,
                },
                summarize_create_params.SummarizeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SummarizeCreateResponse,
        )


class SummarizeWithRawResponse:
    def __init__(self, summarize: Summarize) -> None:
        self._summarize = summarize

        self.create = to_raw_response_wrapper(
            summarize.create,
        )


class AsyncSummarizeWithRawResponse:
    def __init__(self, summarize: AsyncSummarize) -> None:
        self._summarize = summarize

        self.create = async_to_raw_response_wrapper(
            summarize.create,
        )


class SummarizeWithStreamingResponse:
    def __init__(self, summarize: Summarize) -> None:
        self._summarize = summarize

        self.create = to_streamed_response_wrapper(
            summarize.create,
        )


class AsyncSummarizeWithStreamingResponse:
    def __init__(self, summarize: AsyncSummarize) -> None:
        self._summarize = summarize

        self.create = async_to_streamed_response_wrapper(
            summarize.create,
        )
