# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import resources, _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    get_async_library,
)
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, MeorphisTest11Error
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "resources",
    "MeorphisTest11",
    "AsyncMeorphisTest11",
    "Client",
    "AsyncClient",
]


class MeorphisTest11(SyncAPIClient):
    generate: resources.Generate
    embed: resources.Embed
    chat: resources.Chat
    classify: resources.Classify
    tokenize: resources.Tokenize
    detokenize: resources.Detokenize
    detect_language: resources.DetectLanguage
    summarize: resources.Summarize
    rerank: resources.Rerank
    with_raw_response: MeorphisTest11WithRawResponse
    with_streaming_response: MeorphisTest11WithStreamedResponse

    # client options
    bearer_token: str

    def __init__(
        self,
        *,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client. See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous meorphis-test-11 client instance.

        This automatically infers the `bearer_token` argument from the `MEORPHIS_TEST_11_BEARER_TOKEN` environment variable if it is not provided.
        """
        if bearer_token is None:
            bearer_token = os.environ.get("MEORPHIS_TEST_11_BEARER_TOKEN")
        if bearer_token is None:
            raise MeorphisTest11Error(
                "The bearer_token client option must be set either by passing bearer_token to the client or by setting the MEORPHIS_TEST_11_BEARER_TOKEN environment variable"
            )
        self.bearer_token = bearer_token

        if base_url is None:
            base_url = os.environ.get("MEORPHIS_TEST_11_BASE_URL")
        if base_url is None:
            base_url = f"https://api.cohere.ai/v1"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.generate = resources.Generate(self)
        self.embed = resources.Embed(self)
        self.chat = resources.Chat(self)
        self.classify = resources.Classify(self)
        self.tokenize = resources.Tokenize(self)
        self.detokenize = resources.Detokenize(self)
        self.detect_language = resources.DetectLanguage(self)
        self.summarize = resources.Summarize(self)
        self.rerank = resources.Rerank(self)
        self.with_raw_response = MeorphisTest11WithRawResponse(self)
        self.with_streaming_response = MeorphisTest11WithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        bearer_token = self.bearer_token
        return {"Authorization": f"Bearer {bearer_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            bearer_token=bearer_token or self.bearer_token,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncMeorphisTest11(AsyncAPIClient):
    generate: resources.AsyncGenerate
    embed: resources.AsyncEmbed
    chat: resources.AsyncChat
    classify: resources.AsyncClassify
    tokenize: resources.AsyncTokenize
    detokenize: resources.AsyncDetokenize
    detect_language: resources.AsyncDetectLanguage
    summarize: resources.AsyncSummarize
    rerank: resources.AsyncRerank
    with_raw_response: AsyncMeorphisTest11WithRawResponse
    with_streaming_response: AsyncMeorphisTest11WithStreamedResponse

    # client options
    bearer_token: str

    def __init__(
        self,
        *,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client. See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async meorphis-test-11 client instance.

        This automatically infers the `bearer_token` argument from the `MEORPHIS_TEST_11_BEARER_TOKEN` environment variable if it is not provided.
        """
        if bearer_token is None:
            bearer_token = os.environ.get("MEORPHIS_TEST_11_BEARER_TOKEN")
        if bearer_token is None:
            raise MeorphisTest11Error(
                "The bearer_token client option must be set either by passing bearer_token to the client or by setting the MEORPHIS_TEST_11_BEARER_TOKEN environment variable"
            )
        self.bearer_token = bearer_token

        if base_url is None:
            base_url = os.environ.get("MEORPHIS_TEST_11_BASE_URL")
        if base_url is None:
            base_url = f"https://api.cohere.ai/v1"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.generate = resources.AsyncGenerate(self)
        self.embed = resources.AsyncEmbed(self)
        self.chat = resources.AsyncChat(self)
        self.classify = resources.AsyncClassify(self)
        self.tokenize = resources.AsyncTokenize(self)
        self.detokenize = resources.AsyncDetokenize(self)
        self.detect_language = resources.AsyncDetectLanguage(self)
        self.summarize = resources.AsyncSummarize(self)
        self.rerank = resources.AsyncRerank(self)
        self.with_raw_response = AsyncMeorphisTest11WithRawResponse(self)
        self.with_streaming_response = AsyncMeorphisTest11WithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        bearer_token = self.bearer_token
        return {"Authorization": f"Bearer {bearer_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            bearer_token=bearer_token or self.bearer_token,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class MeorphisTest11WithRawResponse:
    def __init__(self, client: MeorphisTest11) -> None:
        self.generate = resources.GenerateWithRawResponse(client.generate)
        self.embed = resources.EmbedWithRawResponse(client.embed)
        self.chat = resources.ChatWithRawResponse(client.chat)
        self.classify = resources.ClassifyWithRawResponse(client.classify)
        self.tokenize = resources.TokenizeWithRawResponse(client.tokenize)
        self.detokenize = resources.DetokenizeWithRawResponse(client.detokenize)
        self.detect_language = resources.DetectLanguageWithRawResponse(client.detect_language)
        self.summarize = resources.SummarizeWithRawResponse(client.summarize)
        self.rerank = resources.RerankWithRawResponse(client.rerank)


class AsyncMeorphisTest11WithRawResponse:
    def __init__(self, client: AsyncMeorphisTest11) -> None:
        self.generate = resources.AsyncGenerateWithRawResponse(client.generate)
        self.embed = resources.AsyncEmbedWithRawResponse(client.embed)
        self.chat = resources.AsyncChatWithRawResponse(client.chat)
        self.classify = resources.AsyncClassifyWithRawResponse(client.classify)
        self.tokenize = resources.AsyncTokenizeWithRawResponse(client.tokenize)
        self.detokenize = resources.AsyncDetokenizeWithRawResponse(client.detokenize)
        self.detect_language = resources.AsyncDetectLanguageWithRawResponse(client.detect_language)
        self.summarize = resources.AsyncSummarizeWithRawResponse(client.summarize)
        self.rerank = resources.AsyncRerankWithRawResponse(client.rerank)


class MeorphisTest11WithStreamedResponse:
    def __init__(self, client: MeorphisTest11) -> None:
        self.generate = resources.GenerateWithStreamingResponse(client.generate)
        self.embed = resources.EmbedWithStreamingResponse(client.embed)
        self.chat = resources.ChatWithStreamingResponse(client.chat)
        self.classify = resources.ClassifyWithStreamingResponse(client.classify)
        self.tokenize = resources.TokenizeWithStreamingResponse(client.tokenize)
        self.detokenize = resources.DetokenizeWithStreamingResponse(client.detokenize)
        self.detect_language = resources.DetectLanguageWithStreamingResponse(client.detect_language)
        self.summarize = resources.SummarizeWithStreamingResponse(client.summarize)
        self.rerank = resources.RerankWithStreamingResponse(client.rerank)


class AsyncMeorphisTest11WithStreamedResponse:
    def __init__(self, client: AsyncMeorphisTest11) -> None:
        self.generate = resources.AsyncGenerateWithStreamingResponse(client.generate)
        self.embed = resources.AsyncEmbedWithStreamingResponse(client.embed)
        self.chat = resources.AsyncChatWithStreamingResponse(client.chat)
        self.classify = resources.AsyncClassifyWithStreamingResponse(client.classify)
        self.tokenize = resources.AsyncTokenizeWithStreamingResponse(client.tokenize)
        self.detokenize = resources.AsyncDetokenizeWithStreamingResponse(client.detokenize)
        self.detect_language = resources.AsyncDetectLanguageWithStreamingResponse(client.detect_language)
        self.summarize = resources.AsyncSummarizeWithStreamingResponse(client.summarize)
        self.rerank = resources.AsyncRerankWithStreamingResponse(client.rerank)


Client = MeorphisTest11

AsyncClient = AsyncMeorphisTest11
