# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from meorphis_test_11 import MeorphisTest11, AsyncMeorphisTest11
from meorphis_test_11.types import ClassifyCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestClassify:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: MeorphisTest11) -> None:
        classify = client.classify.create(
            examples=[{}, {}, {}, {}, {}, {}, {}, {}, {}, {}],
            inputs=["Confirm your email address", "hey i need u to send some $"],
        )
        assert_matches_type(ClassifyCreateResponse, classify, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: MeorphisTest11) -> None:
        classify = client.classify.create(
            examples=[
                {
                    "text": "Dermatologists don't like her!",
                    "label": "Spam",
                },
                {
                    "text": "Hello, open to this?",
                    "label": "Spam",
                },
                {
                    "text": "I need help please wire me $1000 right now",
                    "label": "Spam",
                },
                {
                    "text": "Nice to know you ;)",
                    "label": "Spam",
                },
                {
                    "text": "Please help me?",
                    "label": "Spam",
                },
                {
                    "text": "Your parcel will be delivered today",
                    "label": "Not spam",
                },
                {
                    "text": "Review changes to our Terms and Conditions",
                    "label": "Not spam",
                },
                {
                    "text": "Weekly sync notes",
                    "label": "Not spam",
                },
                {
                    "text": "Re: Follow up from today’s meeting",
                    "label": "Not spam",
                },
                {
                    "text": "Pre-read for tomorrow",
                    "label": "Not spam",
                },
            ],
            inputs=["Confirm your email address", "hey i need u to send some $"],
            model="string",
            preset="my-preset-a58sbd",
            truncate="NONE",
        )
        assert_matches_type(ClassifyCreateResponse, classify, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: MeorphisTest11) -> None:
        response = client.classify.with_raw_response.create(
            examples=[{}, {}, {}, {}, {}, {}, {}, {}, {}, {}],
            inputs=["Confirm your email address", "hey i need u to send some $"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        classify = response.parse()
        assert_matches_type(ClassifyCreateResponse, classify, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: MeorphisTest11) -> None:
        with client.classify.with_streaming_response.create(
            examples=[{}, {}, {}, {}, {}, {}, {}, {}, {}, {}],
            inputs=["Confirm your email address", "hey i need u to send some $"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            classify = response.parse()
            assert_matches_type(ClassifyCreateResponse, classify, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncClassify:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncMeorphisTest11) -> None:
        classify = await async_client.classify.create(
            examples=[{}, {}, {}, {}, {}, {}, {}, {}, {}, {}],
            inputs=["Confirm your email address", "hey i need u to send some $"],
        )
        assert_matches_type(ClassifyCreateResponse, classify, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMeorphisTest11) -> None:
        classify = await async_client.classify.create(
            examples=[
                {
                    "text": "Dermatologists don't like her!",
                    "label": "Spam",
                },
                {
                    "text": "Hello, open to this?",
                    "label": "Spam",
                },
                {
                    "text": "I need help please wire me $1000 right now",
                    "label": "Spam",
                },
                {
                    "text": "Nice to know you ;)",
                    "label": "Spam",
                },
                {
                    "text": "Please help me?",
                    "label": "Spam",
                },
                {
                    "text": "Your parcel will be delivered today",
                    "label": "Not spam",
                },
                {
                    "text": "Review changes to our Terms and Conditions",
                    "label": "Not spam",
                },
                {
                    "text": "Weekly sync notes",
                    "label": "Not spam",
                },
                {
                    "text": "Re: Follow up from today’s meeting",
                    "label": "Not spam",
                },
                {
                    "text": "Pre-read for tomorrow",
                    "label": "Not spam",
                },
            ],
            inputs=["Confirm your email address", "hey i need u to send some $"],
            model="string",
            preset="my-preset-a58sbd",
            truncate="NONE",
        )
        assert_matches_type(ClassifyCreateResponse, classify, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMeorphisTest11) -> None:
        response = await async_client.classify.with_raw_response.create(
            examples=[{}, {}, {}, {}, {}, {}, {}, {}, {}, {}],
            inputs=["Confirm your email address", "hey i need u to send some $"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        classify = await response.parse()
        assert_matches_type(ClassifyCreateResponse, classify, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMeorphisTest11) -> None:
        async with async_client.classify.with_streaming_response.create(
            examples=[{}, {}, {}, {}, {}, {}, {}, {}, {}, {}],
            inputs=["Confirm your email address", "hey i need u to send some $"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            classify = await response.parse()
            assert_matches_type(ClassifyCreateResponse, classify, path=["response"])

        assert cast(Any, response.is_closed) is True
