# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, List
from typing_extensions import Literal

import httpx

from ..types import Generation, generate_create_params
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

__all__ = ["Generate", "AsyncGenerate"]


class Generate(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GenerateWithRawResponse:
        return GenerateWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GenerateWithStreamingResponse:
        return GenerateWithStreamingResponse(self)

    def create(
        self,
        *,
        prompt: str,
        end_sequences: List[str] | NotGiven = NOT_GIVEN,
        frequency_penalty: float | NotGiven = NOT_GIVEN,
        k: int | NotGiven = NOT_GIVEN,
        logit_bias: Dict[str, float] | NotGiven = NOT_GIVEN,
        max_tokens: int | NotGiven = NOT_GIVEN,
        model: str | NotGiven = NOT_GIVEN,
        num_generations: int | NotGiven = NOT_GIVEN,
        p: float | NotGiven = NOT_GIVEN,
        presence_penalty: float | NotGiven = NOT_GIVEN,
        preset: str | NotGiven = NOT_GIVEN,
        return_likelihoods: Literal["GENERATION", "ALL", "NONE"] | NotGiven = NOT_GIVEN,
        stop_sequences: List[str] | NotGiven = NOT_GIVEN,
        stream: bool | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        truncate: Literal["NONE", "START", "END"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Generation:
        """
        This endpoint generates realistic text conditioned on a given input.

        Args:
          prompt: The input text that serves as the starting point for generating the response.
              Note: The prompt will be pre-processed and modified before reaching the model.

          end_sequences: The generated text will be cut at the beginning of the earliest occurence of an
              end sequence. The sequence will be excluded from the text.

          frequency_penalty: Used to reduce repetitiveness of generated tokens. The higher the value, the
              stronger a penalty is applied to previously present tokens, proportional to how
              many times they have already appeared in the prompt or prior generation.'

          k: Ensures only the top `k` most likely tokens are considered for generation at
              each step. Defaults to `0`, min value of `0`, max value of `500`.

          logit_bias: Used to prevent the model from generating unwanted tokens or to incentivize it
              to include desired tokens. The format is `{token_id: bias}` where bias is a
              float between -10 and 10. Tokens can be obtained from text using
              [Tokenize](/reference/tokenize).

              For example, if the value `{'11': -10}` is provided, the model will be very
              unlikely to include the token 11 (`"\n"`, the newline character) anywhere in the
              generated text. In contrast `{'11': 10}` will result in generations that nearly
              only contain that token. Values between -10 and 10 will proportionally affect
              the likelihood of the token appearing in the generated text.

              Note: logit bias may not be supported for all custom models.

          max_tokens: The maximum number of tokens the model will generate as part of the response.
              Note: Setting a low value may result in incomplete generations. Defaults to
              `20`. See [BPE Tokens](/bpe-tokens-wiki) for more details.

              Can only be set to `0` if `return_likelihoods` is set to `ALL` to get the
              likelihood of the prompt.

          model: The identifier of the model to generate with. Currently available models are
              `command` (default), `command-nightly` (experimental), `command-light`, and
              `command-light-nightly` (experimental). Smaller, "light" models are faster,
              while larger models will perform better.
              [Custom models](/docs/training-custom-models) can also be supplied with their
              full ID.

          num_generations: The maximum number of generations that will be returned. Defaults to `1`, min
              value of `1`, max value of `5`.

          p: Ensures that only the most likely tokens, with total probability mass of `p`,
              are considered for generation at each step. If both `k` and `p` are enabled, `p`
              acts after `k`. Defaults to `0`. min value of `0.01`, max value of `0.99`.

          presence_penalty: Defaults to `0.0`, min value of `0.0`, max value of `1.0`. Can be used to reduce
              repetitiveness of generated tokens. Similar to `frequency_penalty`, except that
              this penalty is applied equally to all tokens that have already appeared,
              regardless of their exact frequencies.

          preset: Identifier of a custom preset. A preset is a combination of parameters, such as
              prompt, temperature etc. You can create presets in the
              [playground](https://dashboard.cohere.ai/playground/generate). When a preset is
              specified, the `prompt` parameter becomes optional, and any included parameters
              will override the preset's parameters.

          return_likelihoods: One of `GENERATION|ALL|NONE` to specify how and if the token likelihoods are
              returned with the response. Defaults to `NONE`.

              If `GENERATION` is selected, the token likelihoods will only be provided for
              generated text.

              If `ALL` is selected, the token likelihoods will be provided both for the prompt
              and the generated text.

          stop_sequences: The generated text will be cut at the end of the earliest occurence of a stop
              sequence. The sequence will be included the text.

          stream: When `true`, the response will be a JSON stream of events. Streaming is
              beneficial for user interfaces that render the contents of the response piece by
              piece, as it gets generated.

              The final event will contain the complete response, and will contain an
              `is_finished` field set to `true`. The event will also contain a
              `finish_reason`, which can be one of the following:

              - `COMPLETE` - the model sent back a finished reply
              - `MAX_TOKENS` - the reply was cut off because the model reached the maximum
                number of tokens for its context length
              - `ERROR` - something went wrong when generating the reply
              - `ERROR_TOXIC` - the model generated a reply that was deemed toxic

          temperature: A non-negative float that tunes the degree of randomness in generation. Lower
              temperatures mean less random generations. See [Temperature](/temperature-wiki)
              for more details. Defaults to `0.75`, min value of `0.0`, max value of `5.0`.

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
            "/generate",
            body=maybe_transform(
                {
                    "prompt": prompt,
                    "end_sequences": end_sequences,
                    "frequency_penalty": frequency_penalty,
                    "k": k,
                    "logit_bias": logit_bias,
                    "max_tokens": max_tokens,
                    "model": model,
                    "num_generations": num_generations,
                    "p": p,
                    "presence_penalty": presence_penalty,
                    "preset": preset,
                    "return_likelihoods": return_likelihoods,
                    "stop_sequences": stop_sequences,
                    "stream": stream,
                    "temperature": temperature,
                    "truncate": truncate,
                },
                generate_create_params.GenerateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Generation,
        )


class AsyncGenerate(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGenerateWithRawResponse:
        return AsyncGenerateWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGenerateWithStreamingResponse:
        return AsyncGenerateWithStreamingResponse(self)

    async def create(
        self,
        *,
        prompt: str,
        end_sequences: List[str] | NotGiven = NOT_GIVEN,
        frequency_penalty: float | NotGiven = NOT_GIVEN,
        k: int | NotGiven = NOT_GIVEN,
        logit_bias: Dict[str, float] | NotGiven = NOT_GIVEN,
        max_tokens: int | NotGiven = NOT_GIVEN,
        model: str | NotGiven = NOT_GIVEN,
        num_generations: int | NotGiven = NOT_GIVEN,
        p: float | NotGiven = NOT_GIVEN,
        presence_penalty: float | NotGiven = NOT_GIVEN,
        preset: str | NotGiven = NOT_GIVEN,
        return_likelihoods: Literal["GENERATION", "ALL", "NONE"] | NotGiven = NOT_GIVEN,
        stop_sequences: List[str] | NotGiven = NOT_GIVEN,
        stream: bool | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        truncate: Literal["NONE", "START", "END"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Generation:
        """
        This endpoint generates realistic text conditioned on a given input.

        Args:
          prompt: The input text that serves as the starting point for generating the response.
              Note: The prompt will be pre-processed and modified before reaching the model.

          end_sequences: The generated text will be cut at the beginning of the earliest occurence of an
              end sequence. The sequence will be excluded from the text.

          frequency_penalty: Used to reduce repetitiveness of generated tokens. The higher the value, the
              stronger a penalty is applied to previously present tokens, proportional to how
              many times they have already appeared in the prompt or prior generation.'

          k: Ensures only the top `k` most likely tokens are considered for generation at
              each step. Defaults to `0`, min value of `0`, max value of `500`.

          logit_bias: Used to prevent the model from generating unwanted tokens or to incentivize it
              to include desired tokens. The format is `{token_id: bias}` where bias is a
              float between -10 and 10. Tokens can be obtained from text using
              [Tokenize](/reference/tokenize).

              For example, if the value `{'11': -10}` is provided, the model will be very
              unlikely to include the token 11 (`"\n"`, the newline character) anywhere in the
              generated text. In contrast `{'11': 10}` will result in generations that nearly
              only contain that token. Values between -10 and 10 will proportionally affect
              the likelihood of the token appearing in the generated text.

              Note: logit bias may not be supported for all custom models.

          max_tokens: The maximum number of tokens the model will generate as part of the response.
              Note: Setting a low value may result in incomplete generations. Defaults to
              `20`. See [BPE Tokens](/bpe-tokens-wiki) for more details.

              Can only be set to `0` if `return_likelihoods` is set to `ALL` to get the
              likelihood of the prompt.

          model: The identifier of the model to generate with. Currently available models are
              `command` (default), `command-nightly` (experimental), `command-light`, and
              `command-light-nightly` (experimental). Smaller, "light" models are faster,
              while larger models will perform better.
              [Custom models](/docs/training-custom-models) can also be supplied with their
              full ID.

          num_generations: The maximum number of generations that will be returned. Defaults to `1`, min
              value of `1`, max value of `5`.

          p: Ensures that only the most likely tokens, with total probability mass of `p`,
              are considered for generation at each step. If both `k` and `p` are enabled, `p`
              acts after `k`. Defaults to `0`. min value of `0.01`, max value of `0.99`.

          presence_penalty: Defaults to `0.0`, min value of `0.0`, max value of `1.0`. Can be used to reduce
              repetitiveness of generated tokens. Similar to `frequency_penalty`, except that
              this penalty is applied equally to all tokens that have already appeared,
              regardless of their exact frequencies.

          preset: Identifier of a custom preset. A preset is a combination of parameters, such as
              prompt, temperature etc. You can create presets in the
              [playground](https://dashboard.cohere.ai/playground/generate). When a preset is
              specified, the `prompt` parameter becomes optional, and any included parameters
              will override the preset's parameters.

          return_likelihoods: One of `GENERATION|ALL|NONE` to specify how and if the token likelihoods are
              returned with the response. Defaults to `NONE`.

              If `GENERATION` is selected, the token likelihoods will only be provided for
              generated text.

              If `ALL` is selected, the token likelihoods will be provided both for the prompt
              and the generated text.

          stop_sequences: The generated text will be cut at the end of the earliest occurence of a stop
              sequence. The sequence will be included the text.

          stream: When `true`, the response will be a JSON stream of events. Streaming is
              beneficial for user interfaces that render the contents of the response piece by
              piece, as it gets generated.

              The final event will contain the complete response, and will contain an
              `is_finished` field set to `true`. The event will also contain a
              `finish_reason`, which can be one of the following:

              - `COMPLETE` - the model sent back a finished reply
              - `MAX_TOKENS` - the reply was cut off because the model reached the maximum
                number of tokens for its context length
              - `ERROR` - something went wrong when generating the reply
              - `ERROR_TOXIC` - the model generated a reply that was deemed toxic

          temperature: A non-negative float that tunes the degree of randomness in generation. Lower
              temperatures mean less random generations. See [Temperature](/temperature-wiki)
              for more details. Defaults to `0.75`, min value of `0.0`, max value of `5.0`.

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
            "/generate",
            body=maybe_transform(
                {
                    "prompt": prompt,
                    "end_sequences": end_sequences,
                    "frequency_penalty": frequency_penalty,
                    "k": k,
                    "logit_bias": logit_bias,
                    "max_tokens": max_tokens,
                    "model": model,
                    "num_generations": num_generations,
                    "p": p,
                    "presence_penalty": presence_penalty,
                    "preset": preset,
                    "return_likelihoods": return_likelihoods,
                    "stop_sequences": stop_sequences,
                    "stream": stream,
                    "temperature": temperature,
                    "truncate": truncate,
                },
                generate_create_params.GenerateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Generation,
        )


class GenerateWithRawResponse:
    def __init__(self, generate: Generate) -> None:
        self._generate = generate

        self.create = to_raw_response_wrapper(
            generate.create,
        )


class AsyncGenerateWithRawResponse:
    def __init__(self, generate: AsyncGenerate) -> None:
        self._generate = generate

        self.create = async_to_raw_response_wrapper(
            generate.create,
        )


class GenerateWithStreamingResponse:
    def __init__(self, generate: Generate) -> None:
        self._generate = generate

        self.create = to_streamed_response_wrapper(
            generate.create,
        )


class AsyncGenerateWithStreamingResponse:
    def __init__(self, generate: AsyncGenerate) -> None:
        self._generate = generate

        self.create = async_to_streamed_response_wrapper(
            generate.create,
        )
