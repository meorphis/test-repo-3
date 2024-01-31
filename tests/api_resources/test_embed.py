# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from meorphis_test_11 import MeorphisTest11, AsyncMeorphisTest11
from meorphis_test_11.types import EmbedCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEmbed:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: MeorphisTest11) -> None:
        embed = client.embed.create(
            texts=["hello", "goodbye"],
        )
        assert_matches_type(EmbedCreateResponse, embed, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: MeorphisTest11) -> None:
        embed = client.embed.create(
            texts=["hello", "goodbye"],
            model="string",
            truncate="NONE",
        )
        assert_matches_type(EmbedCreateResponse, embed, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: MeorphisTest11) -> None:
        response = client.embed.with_raw_response.create(
            texts=["hello", "goodbye"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        embed = response.parse()
        assert_matches_type(EmbedCreateResponse, embed, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: MeorphisTest11) -> None:
        with client.embed.with_streaming_response.create(
            texts=["hello", "goodbye"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            embed = response.parse()
            assert_matches_type(EmbedCreateResponse, embed, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEmbed:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncMeorphisTest11) -> None:
        embed = await async_client.embed.create(
            texts=["hello", "goodbye"],
        )
        assert_matches_type(EmbedCreateResponse, embed, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMeorphisTest11) -> None:
        embed = await async_client.embed.create(
            texts=["hello", "goodbye"],
            model="string",
            truncate="NONE",
        )
        assert_matches_type(EmbedCreateResponse, embed, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMeorphisTest11) -> None:
        response = await async_client.embed.with_raw_response.create(
            texts=["hello", "goodbye"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        embed = await response.parse()
        assert_matches_type(EmbedCreateResponse, embed, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMeorphisTest11) -> None:
        async with async_client.embed.with_streaming_response.create(
            texts=["hello", "goodbye"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            embed = await response.parse()
            assert_matches_type(EmbedCreateResponse, embed, path=["response"])

        assert cast(Any, response.is_closed) is True
