# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Any, List, cast
from typing_extensions import Literal

import httpx

from ..types import ChatCreateResponse, chat_create_params
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

__all__ = ["Chat", "AsyncChat"]


class Chat(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ChatWithRawResponse:
        return ChatWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChatWithStreamingResponse:
        return ChatWithStreamingResponse(self)

    def create(
        self,
        *,
        message: str,
        chat_history: List[chat_create_params.ChatHistory] | NotGiven = NOT_GIVEN,
        citation_quality: Literal["fast", "accurate"] | NotGiven = NOT_GIVEN,
        connectors: List[chat_create_params.Connector] | NotGiven = NOT_GIVEN,
        conversation_id: str | NotGiven = NOT_GIVEN,
        documents: List[chat_create_params.Document] | NotGiven = NOT_GIVEN,
        model: str | NotGiven = NOT_GIVEN,
        preamble_override: str | NotGiven = NOT_GIVEN,
        prompt_truncation: Literal["OFF", "AUTO"] | NotGiven = NOT_GIVEN,
        search_queries_only: bool | NotGiven = NOT_GIVEN,
        stream: bool | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCreateResponse:
        """
        _Note: this functionality is currently experimental and in alpha development.
        Please reach out to Cohere if you would like to learn more._

        The `chat` endpoint allows users to have conversations with a Large Language
        Model (LLM) from Cohere. Users can send messages as part of a persisted
        conversation using the `conversation_id` parameter, or they can pass in their
        own conversation history using the `chat_history` parameter.

        The endpoint features additional parameters such as `connectors` and `documents`
        that enable conversations enriched by external knowledge. We call this
        "Retrieval Augmented Generation", or "RAG".

        If you have questions or require support, we're here to help! Reach out to your
        Cohere partner to enable access to this API.

        Args:
          message: Accepts a string.

              The chat message from the user to the model.

          chat_history: A list of previous messages between the user and the model, meant to give the
              model conversational context for responding to the user's `message`.

          citation_quality: Defaults to `"accurate"`.

              Dictates the approach taken to generating citations as part of the RAG flow by
              allowing the user to specify whether they want `"accurate"` results or `"fast"`
              results.

          connectors: Currently only accepts `"web-search"`.

              When specified, the model's reply will be enriched with information found by
              quering each of the connectors (RAG).

          conversation_id: An alternative to `chat_history`. Previous conversations can be resumed by
              providing the conversation's identifier. The contents of `message` and the
              model's response will be stored as part of this conversation.

              If a conversation with this id does not already exist, a new conversation will
              be created.

          documents: A list of relevant documents that the model can use to enrich its reply (RAG).

              The recommended length for the snippet of each document is relatively short,
              under 300 words. Documents with long snippets should be split up into several
              smaller documents.

          model: Defaults to `command`.

              The identifier of the model, which can be one of the existing Cohere models or
              the full ID for a [finetuned custom model](/docs/training-custom-models).
              Compatible Cohere models are `command` and `command-light` as well as the
              experimental `command-nightly` and `command-light-nightly` variants. Read more
              about [Cohere models](https://docs.cohere.com/docs/models).

          preamble_override: When specified, the default Cohere preamble will be replaced with the provided
              one.

          prompt_truncation: Defaults to `OFF`.

              Dictates how the prompt will be constructed.

              With `prompt_truncation` set to "AUTO", some elements from `chat_history` and
              `documents` will be dropped in attempt to construct a prompt that fits within
              the model's context length limit.

              With `prompt_truncation` set to "OFF", no elements will be dropped. If the sum
              of the inputs exceeds the model's context length limit, a `TooManyTokens` error
              will be returned.

          search_queries_only: Defaults to `false`.

              When `true`, the response will only contain a list of generated search queries,
              but no search will take place, and no reply from the model to the user's
              `message` will be generated.

          stream: Defaults to `false`.

              When `true`, the response will be a JSON stream of events. The final event will
              contain the complete response, and will have an `event_type` of `"stream-end"`.

              Streaming is beneficial for user interfaces that render the contents of the
              response piece by piece, as it gets generated.

          temperature: Defaults to `0.5` when neither `documents` nor `connectors` are specified.
              Defaults to `0.1` when one of `documents` or `connectors` is specified

              A non-negative float that tunes the degree of randomness in generation. Lower
              temperatures mean less random generations, and higher temperatures mean more
              random generations.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            ChatCreateResponse,
            self._post(
                "/chat",
                body=maybe_transform(
                    {
                        "message": message,
                        "chat_history": chat_history,
                        "citation_quality": citation_quality,
                        "connectors": connectors,
                        "conversation_id": conversation_id,
                        "documents": documents,
                        "model": model,
                        "preamble_override": preamble_override,
                        "prompt_truncation": prompt_truncation,
                        "search_queries_only": search_queries_only,
                        "stream": stream,
                        "temperature": temperature,
                    },
                    chat_create_params.ChatCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, ChatCreateResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncChat(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncChatWithRawResponse:
        return AsyncChatWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChatWithStreamingResponse:
        return AsyncChatWithStreamingResponse(self)

    async def create(
        self,
        *,
        message: str,
        chat_history: List[chat_create_params.ChatHistory] | NotGiven = NOT_GIVEN,
        citation_quality: Literal["fast", "accurate"] | NotGiven = NOT_GIVEN,
        connectors: List[chat_create_params.Connector] | NotGiven = NOT_GIVEN,
        conversation_id: str | NotGiven = NOT_GIVEN,
        documents: List[chat_create_params.Document] | NotGiven = NOT_GIVEN,
        model: str | NotGiven = NOT_GIVEN,
        preamble_override: str | NotGiven = NOT_GIVEN,
        prompt_truncation: Literal["OFF", "AUTO"] | NotGiven = NOT_GIVEN,
        search_queries_only: bool | NotGiven = NOT_GIVEN,
        stream: bool | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCreateResponse:
        """
        _Note: this functionality is currently experimental and in alpha development.
        Please reach out to Cohere if you would like to learn more._

        The `chat` endpoint allows users to have conversations with a Large Language
        Model (LLM) from Cohere. Users can send messages as part of a persisted
        conversation using the `conversation_id` parameter, or they can pass in their
        own conversation history using the `chat_history` parameter.

        The endpoint features additional parameters such as `connectors` and `documents`
        that enable conversations enriched by external knowledge. We call this
        "Retrieval Augmented Generation", or "RAG".

        If you have questions or require support, we're here to help! Reach out to your
        Cohere partner to enable access to this API.

        Args:
          message: Accepts a string.

              The chat message from the user to the model.

          chat_history: A list of previous messages between the user and the model, meant to give the
              model conversational context for responding to the user's `message`.

          citation_quality: Defaults to `"accurate"`.

              Dictates the approach taken to generating citations as part of the RAG flow by
              allowing the user to specify whether they want `"accurate"` results or `"fast"`
              results.

          connectors: Currently only accepts `"web-search"`.

              When specified, the model's reply will be enriched with information found by
              quering each of the connectors (RAG).

          conversation_id: An alternative to `chat_history`. Previous conversations can be resumed by
              providing the conversation's identifier. The contents of `message` and the
              model's response will be stored as part of this conversation.

              If a conversation with this id does not already exist, a new conversation will
              be created.

          documents: A list of relevant documents that the model can use to enrich its reply (RAG).

              The recommended length for the snippet of each document is relatively short,
              under 300 words. Documents with long snippets should be split up into several
              smaller documents.

          model: Defaults to `command`.

              The identifier of the model, which can be one of the existing Cohere models or
              the full ID for a [finetuned custom model](/docs/training-custom-models).
              Compatible Cohere models are `command` and `command-light` as well as the
              experimental `command-nightly` and `command-light-nightly` variants. Read more
              about [Cohere models](https://docs.cohere.com/docs/models).

          preamble_override: When specified, the default Cohere preamble will be replaced with the provided
              one.

          prompt_truncation: Defaults to `OFF`.

              Dictates how the prompt will be constructed.

              With `prompt_truncation` set to "AUTO", some elements from `chat_history` and
              `documents` will be dropped in attempt to construct a prompt that fits within
              the model's context length limit.

              With `prompt_truncation` set to "OFF", no elements will be dropped. If the sum
              of the inputs exceeds the model's context length limit, a `TooManyTokens` error
              will be returned.

          search_queries_only: Defaults to `false`.

              When `true`, the response will only contain a list of generated search queries,
              but no search will take place, and no reply from the model to the user's
              `message` will be generated.

          stream: Defaults to `false`.

              When `true`, the response will be a JSON stream of events. The final event will
              contain the complete response, and will have an `event_type` of `"stream-end"`.

              Streaming is beneficial for user interfaces that render the contents of the
              response piece by piece, as it gets generated.

          temperature: Defaults to `0.5` when neither `documents` nor `connectors` are specified.
              Defaults to `0.1` when one of `documents` or `connectors` is specified

              A non-negative float that tunes the degree of randomness in generation. Lower
              temperatures mean less random generations, and higher temperatures mean more
              random generations.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            ChatCreateResponse,
            await self._post(
                "/chat",
                body=maybe_transform(
                    {
                        "message": message,
                        "chat_history": chat_history,
                        "citation_quality": citation_quality,
                        "connectors": connectors,
                        "conversation_id": conversation_id,
                        "documents": documents,
                        "model": model,
                        "preamble_override": preamble_override,
                        "prompt_truncation": prompt_truncation,
                        "search_queries_only": search_queries_only,
                        "stream": stream,
                        "temperature": temperature,
                    },
                    chat_create_params.ChatCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, ChatCreateResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class ChatWithRawResponse:
    def __init__(self, chat: Chat) -> None:
        self._chat = chat

        self.create = to_raw_response_wrapper(
            chat.create,
        )


class AsyncChatWithRawResponse:
    def __init__(self, chat: AsyncChat) -> None:
        self._chat = chat

        self.create = async_to_raw_response_wrapper(
            chat.create,
        )


class ChatWithStreamingResponse:
    def __init__(self, chat: Chat) -> None:
        self._chat = chat

        self.create = to_streamed_response_wrapper(
            chat.create,
        )


class AsyncChatWithStreamingResponse:
    def __init__(self, chat: AsyncChat) -> None:
        self._chat = chat

        self.create = async_to_streamed_response_wrapper(
            chat.create,
        )
