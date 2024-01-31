# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ..types import ClassifyCreateResponse, classify_create_params
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

__all__ = ["Classify", "AsyncClassify"]


class Classify(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ClassifyWithRawResponse:
        return ClassifyWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ClassifyWithStreamingResponse:
        return ClassifyWithStreamingResponse(self)

    def create(
        self,
        *,
        examples: List[classify_create_params.Example],
        inputs: List[str],
        model: str | NotGiven = NOT_GIVEN,
        preset: str | NotGiven = NOT_GIVEN,
        truncate: Literal["NONE", "START", "END"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ClassifyCreateResponse:
        """
        This endpoint makes a prediction about which label fits the specified text
        inputs best. To make a prediction, Classify uses the provided `examples` of
        text + label pairs as a reference.

        Note: [Custom Models](/training-representation-models) trained on classification
        examples don't require the `examples` parameter to be passed in explicitly.

        Args:
          examples: An array of examples to provide context to the model. Each example is a text
              string and its associated label/class. Each unique label requires at least 2
              examples associated with it; the maximum number of examples is 2500, and each
              example has a maximum length of 512 tokens. The values should be structured as
              `{text: "...",label: "..."}`.

              Note: [Custom Models](/training-representation-models) trained on classification
              examples don't require the `examples` parameter to be passed in explicitly.

          inputs: Represents a list of queries to be classified, each entry must not be empty. The
              maximum is 96 inputs.

          model: The identifier of the model. Currently available models are
              `embed-multilingual-v2.0`, `embed-english-light-v2.0`, and `embed-english-v2.0`
              (default). Smaller "light" models are faster, while larger models will perform
              better. [Custom models](/docs/training-custom-models) can also be supplied with
              their full ID.

          preset: The ID of a custom playground preset. You can create presets in the
              [playground](https://dashboard.cohere.ai/playground/classify?model=large). If
              you use a preset, all other parameters become optional, and any included
              parameters will override the preset's parameters.

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
            "/classify",
            body=maybe_transform(
                {
                    "examples": examples,
                    "inputs": inputs,
                    "model": model,
                    "preset": preset,
                    "truncate": truncate,
                },
                classify_create_params.ClassifyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClassifyCreateResponse,
        )


class AsyncClassify(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncClassifyWithRawResponse:
        return AsyncClassifyWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncClassifyWithStreamingResponse:
        return AsyncClassifyWithStreamingResponse(self)

    async def create(
        self,
        *,
        examples: List[classify_create_params.Example],
        inputs: List[str],
        model: str | NotGiven = NOT_GIVEN,
        preset: str | NotGiven = NOT_GIVEN,
        truncate: Literal["NONE", "START", "END"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ClassifyCreateResponse:
        """
        This endpoint makes a prediction about which label fits the specified text
        inputs best. To make a prediction, Classify uses the provided `examples` of
        text + label pairs as a reference.

        Note: [Custom Models](/training-representation-models) trained on classification
        examples don't require the `examples` parameter to be passed in explicitly.

        Args:
          examples: An array of examples to provide context to the model. Each example is a text
              string and its associated label/class. Each unique label requires at least 2
              examples associated with it; the maximum number of examples is 2500, and each
              example has a maximum length of 512 tokens. The values should be structured as
              `{text: "...",label: "..."}`.

              Note: [Custom Models](/training-representation-models) trained on classification
              examples don't require the `examples` parameter to be passed in explicitly.

          inputs: Represents a list of queries to be classified, each entry must not be empty. The
              maximum is 96 inputs.

          model: The identifier of the model. Currently available models are
              `embed-multilingual-v2.0`, `embed-english-light-v2.0`, and `embed-english-v2.0`
              (default). Smaller "light" models are faster, while larger models will perform
              better. [Custom models](/docs/training-custom-models) can also be supplied with
              their full ID.

          preset: The ID of a custom playground preset. You can create presets in the
              [playground](https://dashboard.cohere.ai/playground/classify?model=large). If
              you use a preset, all other parameters become optional, and any included
              parameters will override the preset's parameters.

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
            "/classify",
            body=maybe_transform(
                {
                    "examples": examples,
                    "inputs": inputs,
                    "model": model,
                    "preset": preset,
                    "truncate": truncate,
                },
                classify_create_params.ClassifyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClassifyCreateResponse,
        )


class ClassifyWithRawResponse:
    def __init__(self, classify: Classify) -> None:
        self._classify = classify

        self.create = to_raw_response_wrapper(
            classify.create,
        )


class AsyncClassifyWithRawResponse:
    def __init__(self, classify: AsyncClassify) -> None:
        self._classify = classify

        self.create = async_to_raw_response_wrapper(
            classify.create,
        )


class ClassifyWithStreamingResponse:
    def __init__(self, classify: Classify) -> None:
        self._classify = classify

        self.create = to_streamed_response_wrapper(
            classify.create,
        )


class AsyncClassifyWithStreamingResponse:
    def __init__(self, classify: AsyncClassify) -> None:
        self._classify = classify

        self.create = async_to_streamed_response_wrapper(
            classify.create,
        )
