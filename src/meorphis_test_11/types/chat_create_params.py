# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ChatCreateParams", "ChatHistory", "Connector", "Document"]


class ChatCreateParams(TypedDict, total=False):
    message: Required[str]
    """Accepts a string.

    The chat message from the user to the model.
    """

    chat_history: List[ChatHistory]
    """
    A list of previous messages between the user and the model, meant to give the
    model conversational context for responding to the user's `message`.
    """

    citation_quality: Literal["fast", "accurate"]
    """Defaults to `"accurate"`.

    Dictates the approach taken to generating citations as part of the RAG flow by
    allowing the user to specify whether they want `"accurate"` results or `"fast"`
    results.
    """

    connectors: List[Connector]
    """Currently only accepts `"web-search"`.

    When specified, the model's reply will be enriched with information found by
    quering each of the connectors (RAG).
    """

    conversation_id: str
    """An alternative to `chat_history`.

    Previous conversations can be resumed by providing the conversation's
    identifier. The contents of `message` and the model's response will be stored as
    part of this conversation.

    If a conversation with this id does not already exist, a new conversation will
    be created.
    """

    documents: List[Document]
    """A list of relevant documents that the model can use to enrich its reply (RAG).

    The recommended length for the snippet of each document is relatively short,
    under 300 words. Documents with long snippets should be split up into several
    smaller documents.
    """

    model: str
    """Defaults to `command`.

    The identifier of the model, which can be one of the existing Cohere models or
    the full ID for a [finetuned custom model](/docs/training-custom-models).
    Compatible Cohere models are `command` and `command-light` as well as the
    experimental `command-nightly` and `command-light-nightly` variants. Read more
    about [Cohere models](https://docs.cohere.com/docs/models).
    """

    preamble_override: str
    """
    When specified, the default Cohere preamble will be replaced with the provided
    one.
    """

    prompt_truncation: Literal["OFF", "AUTO"]
    """Defaults to `OFF`.

    Dictates how the prompt will be constructed.

    With `prompt_truncation` set to "AUTO", some elements from `chat_history` and
    `documents` will be dropped in attempt to construct a prompt that fits within
    the model's context length limit.

    With `prompt_truncation` set to "OFF", no elements will be dropped. If the sum
    of the inputs exceeds the model's context length limit, a `TooManyTokens` error
    will be returned.
    """

    search_queries_only: bool
    """Defaults to `false`.

    When `true`, the response will only contain a list of generated search queries,
    but no search will take place, and no reply from the model to the user's
    `message` will be generated.
    """

    stream: bool
    """Defaults to `false`.

    When `true`, the response will be a JSON stream of events. The final event will
    contain the complete response, and will have an `event_type` of `"stream-end"`.

    Streaming is beneficial for user interfaces that render the contents of the
    response piece by piece, as it gets generated.
    """

    temperature: float
    """
    Defaults to `0.5` when neither `documents` nor `connectors` are specified.
    Defaults to `0.1` when one of `documents` or `connectors` is specified

    A non-negative float that tunes the degree of randomness in generation. Lower
    temperatures mean less random generations, and higher temperatures mean more
    random generations.
    """


class ChatHistory(TypedDict, total=False):
    text: Required[str]

    user_name: Required[Literal["Chatbot", "User"]]


class Connector(TypedDict, total=False):
    id: Required[str]
    """The identifier of the connector. Currently only 'web-search' is supported."""


class Document(TypedDict, total=False):
    snippet: Required[str]
    """The contents of the document."""

    title: Required[str]
    """Title describing the contents of the document."""

    id: str
    """Unique identifier for this document."""

    url: str
    """The URL from which this document originates."""
