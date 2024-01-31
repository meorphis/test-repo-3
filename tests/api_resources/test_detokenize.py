# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from meorphis_test_11 import MeorphisTest11, AsyncMeorphisTest11
from meorphis_test_11.types import DetokenizeCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDetokenize:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: MeorphisTest11) -> None:
        detokenize = client.detokenize.create(
            tokens=[10104, 12221, 1315, 34, 1420, 69],
        )
        assert_matches_type(DetokenizeCreateResponse, detokenize, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: MeorphisTest11) -> None:
        detokenize = client.detokenize.create(
            tokens=[10104, 12221, 1315, 34, 1420, 69],
            model="string",
        )
        assert_matches_type(DetokenizeCreateResponse, detokenize, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: MeorphisTest11) -> None:
        response = client.detokenize.with_raw_response.create(
            tokens=[10104, 12221, 1315, 34, 1420, 69],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        detokenize = response.parse()
        assert_matches_type(DetokenizeCreateResponse, detokenize, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: MeorphisTest11) -> None:
        with client.detokenize.with_streaming_response.create(
            tokens=[10104, 12221, 1315, 34, 1420, 69],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            detokenize = response.parse()
            assert_matches_type(DetokenizeCreateResponse, detokenize, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDetokenize:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncMeorphisTest11) -> None:
        detokenize = await async_client.detokenize.create(
            tokens=[10104, 12221, 1315, 34, 1420, 69],
        )
        assert_matches_type(DetokenizeCreateResponse, detokenize, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMeorphisTest11) -> None:
        detokenize = await async_client.detokenize.create(
            tokens=[10104, 12221, 1315, 34, 1420, 69],
            model="string",
        )
        assert_matches_type(DetokenizeCreateResponse, detokenize, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMeorphisTest11) -> None:
        response = await async_client.detokenize.with_raw_response.create(
            tokens=[10104, 12221, 1315, 34, 1420, 69],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        detokenize = await response.parse()
        assert_matches_type(DetokenizeCreateResponse, detokenize, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMeorphisTest11) -> None:
        async with async_client.detokenize.with_streaming_response.create(
            tokens=[10104, 12221, 1315, 34, 1420, 69],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            detokenize = await response.parse()
            assert_matches_type(DetokenizeCreateResponse, detokenize, path=["response"])

        assert cast(Any, response.is_closed) is True
