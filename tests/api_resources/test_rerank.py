# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from meorphis_test_11 import MeorphisTest11, AsyncMeorphisTest11
from meorphis_test_11.types import RerankCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRerank:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: MeorphisTest11) -> None:
        rerank = client.rerank.create(
            documents=[
                "Carson City is the capital city of the American state of Nevada.",
                "The Commonwealth of the Northern Mariana Islands is a group of islands in the Pacific Ocean. Its capital is Saipan.",
                "Washington, D.C. (also known as simply Washington or D.C., and officially as the District of Columbia) is the capital of the United States. It is a federal district.",
                "Capital punishment (the death penalty) has existed in the United States since beforethe United States was a country. As of 2017, capital punishment is legal in 30 of the 50 states.",
            ],
            query="What is the capital of the United States?",
        )
        assert_matches_type(RerankCreateResponse, rerank, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: MeorphisTest11) -> None:
        rerank = client.rerank.create(
            documents=[
                "Carson City is the capital city of the American state of Nevada.",
                "The Commonwealth of the Northern Mariana Islands is a group of islands in the Pacific Ocean. Its capital is Saipan.",
                "Washington, D.C. (also known as simply Washington or D.C., and officially as the District of Columbia) is the capital of the United States. It is a federal district.",
                "Capital punishment (the death penalty) has existed in the United States since beforethe United States was a country. As of 2017, capital punishment is legal in 30 of the 50 states.",
            ],
            query="What is the capital of the United States?",
            max_chunks_per_doc=0,
            model="rerank-english-v2.0",
            return_documents=True,
            top_n=1,
        )
        assert_matches_type(RerankCreateResponse, rerank, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: MeorphisTest11) -> None:
        response = client.rerank.with_raw_response.create(
            documents=[
                "Carson City is the capital city of the American state of Nevada.",
                "The Commonwealth of the Northern Mariana Islands is a group of islands in the Pacific Ocean. Its capital is Saipan.",
                "Washington, D.C. (also known as simply Washington or D.C., and officially as the District of Columbia) is the capital of the United States. It is a federal district.",
                "Capital punishment (the death penalty) has existed in the United States since beforethe United States was a country. As of 2017, capital punishment is legal in 30 of the 50 states.",
            ],
            query="What is the capital of the United States?",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rerank = response.parse()
        assert_matches_type(RerankCreateResponse, rerank, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: MeorphisTest11) -> None:
        with client.rerank.with_streaming_response.create(
            documents=[
                "Carson City is the capital city of the American state of Nevada.",
                "The Commonwealth of the Northern Mariana Islands is a group of islands in the Pacific Ocean. Its capital is Saipan.",
                "Washington, D.C. (also known as simply Washington or D.C., and officially as the District of Columbia) is the capital of the United States. It is a federal district.",
                "Capital punishment (the death penalty) has existed in the United States since beforethe United States was a country. As of 2017, capital punishment is legal in 30 of the 50 states.",
            ],
            query="What is the capital of the United States?",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rerank = response.parse()
            assert_matches_type(RerankCreateResponse, rerank, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRerank:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncMeorphisTest11) -> None:
        rerank = await async_client.rerank.create(
            documents=[
                "Carson City is the capital city of the American state of Nevada.",
                "The Commonwealth of the Northern Mariana Islands is a group of islands in the Pacific Ocean. Its capital is Saipan.",
                "Washington, D.C. (also known as simply Washington or D.C., and officially as the District of Columbia) is the capital of the United States. It is a federal district.",
                "Capital punishment (the death penalty) has existed in the United States since beforethe United States was a country. As of 2017, capital punishment is legal in 30 of the 50 states.",
            ],
            query="What is the capital of the United States?",
        )
        assert_matches_type(RerankCreateResponse, rerank, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMeorphisTest11) -> None:
        rerank = await async_client.rerank.create(
            documents=[
                "Carson City is the capital city of the American state of Nevada.",
                "The Commonwealth of the Northern Mariana Islands is a group of islands in the Pacific Ocean. Its capital is Saipan.",
                "Washington, D.C. (also known as simply Washington or D.C., and officially as the District of Columbia) is the capital of the United States. It is a federal district.",
                "Capital punishment (the death penalty) has existed in the United States since beforethe United States was a country. As of 2017, capital punishment is legal in 30 of the 50 states.",
            ],
            query="What is the capital of the United States?",
            max_chunks_per_doc=0,
            model="rerank-english-v2.0",
            return_documents=True,
            top_n=1,
        )
        assert_matches_type(RerankCreateResponse, rerank, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMeorphisTest11) -> None:
        response = await async_client.rerank.with_raw_response.create(
            documents=[
                "Carson City is the capital city of the American state of Nevada.",
                "The Commonwealth of the Northern Mariana Islands is a group of islands in the Pacific Ocean. Its capital is Saipan.",
                "Washington, D.C. (also known as simply Washington or D.C., and officially as the District of Columbia) is the capital of the United States. It is a federal district.",
                "Capital punishment (the death penalty) has existed in the United States since beforethe United States was a country. As of 2017, capital punishment is legal in 30 of the 50 states.",
            ],
            query="What is the capital of the United States?",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rerank = await response.parse()
        assert_matches_type(RerankCreateResponse, rerank, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMeorphisTest11) -> None:
        async with async_client.rerank.with_streaming_response.create(
            documents=[
                "Carson City is the capital city of the American state of Nevada.",
                "The Commonwealth of the Northern Mariana Islands is a group of islands in the Pacific Ocean. Its capital is Saipan.",
                "Washington, D.C. (also known as simply Washington or D.C., and officially as the District of Columbia) is the capital of the United States. It is a federal district.",
                "Capital punishment (the death penalty) has existed in the United States since beforethe United States was a country. As of 2017, capital punishment is legal in 30 of the 50 states.",
            ],
            query="What is the capital of the United States?",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rerank = await response.parse()
            assert_matches_type(RerankCreateResponse, rerank, path=["response"])

        assert cast(Any, response.is_closed) is True
