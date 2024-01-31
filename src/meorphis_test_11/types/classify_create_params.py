# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ClassifyCreateParams", "Example"]


class ClassifyCreateParams(TypedDict, total=False):
    examples: Required[List[Example]]
    """An array of examples to provide context to the model.

    Each example is a text string and its associated label/class. Each unique label
    requires at least 2 examples associated with it; the maximum number of examples
    is 2500, and each example has a maximum length of 512 tokens. The values should
    be structured as `{text: "...",label: "..."}`.

    Note: [Custom Models](/training-representation-models) trained on classification
    examples don't require the `examples` parameter to be passed in explicitly.
    """

    inputs: Required[List[str]]
    """Represents a list of queries to be classified, each entry must not be empty.

    The maximum is 96 inputs.
    """

    model: str
    """The identifier of the model.

    Currently available models are `embed-multilingual-v2.0`,
    `embed-english-light-v2.0`, and `embed-english-v2.0` (default). Smaller "light"
    models are faster, while larger models will perform better.
    [Custom models](/docs/training-custom-models) can also be supplied with their
    full ID.
    """

    preset: str
    """The ID of a custom playground preset.

    You can create presets in the
    [playground](https://dashboard.cohere.ai/playground/classify?model=large). If
    you use a preset, all other parameters become optional, and any included
    parameters will override the preset's parameters.
    """

    truncate: Literal["NONE", "START", "END"]
    """
    One of `NONE|START|END` to specify how the API will handle inputs longer than
    the maximum token length.

    Passing `START` will discard the start of the input. `END` will discard the end
    of the input. In both cases, input is discarded until the remaining input is
    exactly the maximum input token length for the model.

    If `NONE` is selected, when the input exceeds the maximum input token length an
    error will be returned.
    """


class Example(TypedDict, total=False):
    label: str

    text: str
