# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from meorphis_test_11 import MeorphisTest11, AsyncMeorphisTest11
from meorphis_test_11.types import TokenizeCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTokenize:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: MeorphisTest11) -> None:
        tokenize = client.tokenize.create(
            text="tokenize me! :D",
        )
        assert_matches_type(TokenizeCreateResponse, tokenize, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: MeorphisTest11) -> None:
        tokenize = client.tokenize.create(
            text="tokenize me! :D",
            model="command",
        )
        assert_matches_type(TokenizeCreateResponse, tokenize, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: MeorphisTest11) -> None:
        response = client.tokenize.with_raw_response.create(
            text="tokenize me! :D",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tokenize = response.parse()
        assert_matches_type(TokenizeCreateResponse, tokenize, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: MeorphisTest11) -> None:
        with client.tokenize.with_streaming_response.create(
            text="tokenize me! :D",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tokenize = response.parse()
            assert_matches_type(TokenizeCreateResponse, tokenize, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTokenize:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncMeorphisTest11) -> None:
        tokenize = await async_client.tokenize.create(
            text="tokenize me! :D",
        )
        assert_matches_type(TokenizeCreateResponse, tokenize, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMeorphisTest11) -> None:
        tokenize = await async_client.tokenize.create(
            text="tokenize me! :D",
            model="command",
        )
        assert_matches_type(TokenizeCreateResponse, tokenize, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMeorphisTest11) -> None:
        response = await async_client.tokenize.with_raw_response.create(
            text="tokenize me! :D",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tokenize = await response.parse()
        assert_matches_type(TokenizeCreateResponse, tokenize, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMeorphisTest11) -> None:
        async with async_client.tokenize.with_streaming_response.create(
            text="tokenize me! :D",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tokenize = await response.parse()
            assert_matches_type(TokenizeCreateResponse, tokenize, path=["response"])

        assert cast(Any, response.is_closed) is True
