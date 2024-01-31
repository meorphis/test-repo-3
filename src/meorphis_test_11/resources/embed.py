# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ..types import EmbedCreateResponse, embed_create_params
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

__all__ = ["Embed", "AsyncEmbed"]


class Embed(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EmbedWithRawResponse:
        return EmbedWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmbedWithStreamingResponse:
        return EmbedWithStreamingResponse(self)

    def create(
        self,
        *,
        texts: List[str],
        model: str | NotGiven = NOT_GIVEN,
        truncate: Literal["NONE", "START", "END"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmbedCreateResponse:
        """This endpoint returns text embeddings.

        An embedding is a list of floating point
        numbers that captures semantic information about the text that it represents.

        Embeddings can be used to create text classifiers as well as empower semantic
        search. To learn more about embeddings, see the embedding page.

        If you want to learn more how to use the embedding model, have a look at the
        [Semantic Search Guide](/docs/semantic-search).

        Args:
          texts: An array of strings for the model to embed. Maximum number of texts per call is
              `96`. We recommend reducing the length of each text to be under `512` tokens for
              optimal quality.

          model: The identifier of the model. Smaller "light" models are faster, while larger
              models will perform better. [Custom models](/docs/training-custom-models) can
              also be supplied with their full ID.

              Available models and corresponding embedding dimensions:

              - `embed-english-v2.0` (default) 4096
              - `embed-english-light-v2.0` 1024
              - `embed-multilingual-v2.0` 768

          truncate: One of `NONE|START|END` to specify how the API will handle inputs longer than
              the maximum token length.

              Passing `START` will discard the start of the input. `END` will discard the end
              of the input. In both cases, input is discarded until the remaining input is
              exactly the maximum input token length for the model.

              If `NONE` is selected, when the input exceeds the maximum input token length an
              error will be returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/embed",
            body=maybe_transform(
                {
                    "texts": texts,
                    "model": model,
                    "truncate": truncate,
                },
                embed_create_params.EmbedCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmbedCreateResponse,
        )


class AsyncEmbed(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEmbedWithRawResponse:
        return AsyncEmbedWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmbedWithStreamingResponse:
        return AsyncEmbedWithStreamingResponse(self)

    async def create(
        self,
        *,
        texts: List[str],
        model: str | NotGiven = NOT_GIVEN,
        truncate: Literal["NONE", "START", "END"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmbedCreateResponse:
        """This endpoint returns text embeddings.

        An embedding is a list of floating point
        numbers that captures semantic information about the text that it represents.

        Embeddings can be used to create text classifiers as well as empower semantic
        search. To learn more about embeddings, see the embedding page.

        If you want to learn more how to use the embedding model, have a look at the
        [Semantic Search Guide](/docs/semantic-search).

        Args:
          texts: An array of strings for the model to embed. Maximum number of texts per call is
              `96`. We recommend reducing the length of each text to be under `512` tokens for
              optimal quality.

          model: The identifier of the model. Smaller "light" models are faster, while larger
              models will perform better. [Custom models](/docs/training-custom-models) can
              also be supplied with their full ID.

              Available models and corresponding embedding dimensions:

              - `embed-english-v2.0` (default) 4096
              - `embed-english-light-v2.0` 1024
              - `embed-multilingual-v2.0` 768

          truncate: One of `NONE|START|END` to specify how the API will handle inputs longer than
              the maximum token length.

              Passing `START` will discard the start of the input. `END` will discard the end
              of the input. In both cases, input is discarded until the remaining input is
              exactly the maximum input token length for the model.

              If `NONE` is selected, when the input exceeds the maximum input token length an
              error will be returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/embed",
            body=maybe_transform(
                {
                    "texts": texts,
                    "model": model,
                    "truncate": truncate,
                },
                embed_create_params.EmbedCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmbedCreateResponse,
        )


class EmbedWithRawResponse:
    def __init__(self, embed: Embed) -> None:
        self._embed = embed

        self.create = to_raw_response_wrapper(
            embed.create,
        )


class AsyncEmbedWithRawResponse:
    def __init__(self, embed: AsyncEmbed) -> None:
        self._embed = embed

        self.create = async_to_raw_response_wrapper(
            embed.create,
        )


class EmbedWithStreamingResponse:
    def __init__(self, embed: Embed) -> None:
        self._embed = embed

        self.create = to_streamed_response_wrapper(
            embed.create,
        )


class AsyncEmbedWithStreamingResponse:
    def __init__(self, embed: AsyncEmbed) -> None:
        self._embed = embed

        self.create = async_to_streamed_response_wrapper(
            embed.create,
        )
