# File generated from our OpenAPI spec by Stainless.

from typing import Union

from .._models import BaseModel

__all__ = ["StreamedChatResponse", "ChatStreamEvent"]


class ChatStreamEvent(BaseModel):
    generation_id: str
    """Unique identifier for the generated reply. Useful for submitting feedback."""


StreamedChatResponse = Union[
    ChatStreamEvent, ChatStreamEvent, ChatStreamEvent, ChatStreamEvent, ChatStreamEvent, ChatStreamEvent
]
