# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from meorphis_test_11 import MeorphisTest11, AsyncMeorphisTest11
from meorphis_test_11.types import DetectLanguageCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDetectLanguage:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: MeorphisTest11) -> None:
        detect_language = client.detect_language.create(
            texts=["Hello world", "Здравствуй, Мир"],
        )
        assert_matches_type(DetectLanguageCreateResponse, detect_language, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: MeorphisTest11) -> None:
        response = client.detect_language.with_raw_response.create(
            texts=["Hello world", "Здравствуй, Мир"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        detect_language = response.parse()
        assert_matches_type(DetectLanguageCreateResponse, detect_language, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: MeorphisTest11) -> None:
        with client.detect_language.with_streaming_response.create(
            texts=["Hello world", "Здравствуй, Мир"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            detect_language = response.parse()
            assert_matches_type(DetectLanguageCreateResponse, detect_language, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDetectLanguage:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncMeorphisTest11) -> None:
        detect_language = await async_client.detect_language.create(
            texts=["Hello world", "Здравствуй, Мир"],
        )
        assert_matches_type(DetectLanguageCreateResponse, detect_language, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMeorphisTest11) -> None:
        response = await async_client.detect_language.with_raw_response.create(
            texts=["Hello world", "Здравствуй, Мир"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        detect_language = await response.parse()
        assert_matches_type(DetectLanguageCreateResponse, detect_language, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMeorphisTest11) -> None:
        async with async_client.detect_language.with_streaming_response.create(
            texts=["Hello world", "Здравствуй, Мир"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            detect_language = await response.parse()
            assert_matches_type(DetectLanguageCreateResponse, detect_language, path=["response"])

        assert cast(Any, response.is_closed) is True
