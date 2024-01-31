# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from meorphis_test_11 import MeorphisTest11, AsyncMeorphisTest11
from meorphis_test_11.types import ChatCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChat:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: MeorphisTest11) -> None:
        chat = client.chat.create(
            message="string",
        )
        assert_matches_type(ChatCreateResponse, chat, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: MeorphisTest11) -> None:
        chat = client.chat.create(
            message="string",
            chat_history=[
                {
                    "user_name": "Chatbot",
                    "text": "x",
                },
                {
                    "user_name": "Chatbot",
                    "text": "x",
                },
                {
                    "user_name": "Chatbot",
                    "text": "x",
                },
            ],
            citation_quality="fast",
            connectors=[{"id": "x"}, {"id": "x"}, {"id": "x"}],
            conversation_id="string",
            documents=[
                {
                    "id": "string",
                    "title": "string",
                    "snippet": "string",
                    "url": "string",
                },
                {
                    "id": "string",
                    "title": "string",
                    "snippet": "string",
                    "url": "string",
                },
                {
                    "id": "string",
                    "title": "string",
                    "snippet": "string",
                    "url": "string",
                },
            ],
            model="string",
            preamble_override="string",
            prompt_truncation="OFF",
            search_queries_only=True,
            stream=True,
            temperature=0,
        )
        assert_matches_type(ChatCreateResponse, chat, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: MeorphisTest11) -> None:
        response = client.chat.with_raw_response.create(
            message="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(ChatCreateResponse, chat, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: MeorphisTest11) -> None:
        with client.chat.with_streaming_response.create(
            message="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(ChatCreateResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncChat:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncMeorphisTest11) -> None:
        chat = await async_client.chat.create(
            message="string",
        )
        assert_matches_type(ChatCreateResponse, chat, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMeorphisTest11) -> None:
        chat = await async_client.chat.create(
            message="string",
            chat_history=[
                {
                    "user_name": "Chatbot",
                    "text": "x",
                },
                {
                    "user_name": "Chatbot",
                    "text": "x",
                },
                {
                    "user_name": "Chatbot",
                    "text": "x",
                },
            ],
            citation_quality="fast",
            connectors=[{"id": "x"}, {"id": "x"}, {"id": "x"}],
            conversation_id="string",
            documents=[
                {
                    "id": "string",
                    "title": "string",
                    "snippet": "string",
                    "url": "string",
                },
                {
                    "id": "string",
                    "title": "string",
                    "snippet": "string",
                    "url": "string",
                },
                {
                    "id": "string",
                    "title": "string",
                    "snippet": "string",
                    "url": "string",
                },
            ],
            model="string",
            preamble_override="string",
            prompt_truncation="OFF",
            search_queries_only=True,
            stream=True,
            temperature=0,
        )
        assert_matches_type(ChatCreateResponse, chat, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMeorphisTest11) -> None:
        response = await async_client.chat.with_raw_response.create(
            message="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(ChatCreateResponse, chat, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMeorphisTest11) -> None:
        async with async_client.chat.with_streaming_response.create(
            message="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(ChatCreateResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True
