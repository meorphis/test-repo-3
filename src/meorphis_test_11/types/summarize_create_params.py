# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SummarizeCreateParams"]


class SummarizeCreateParams(TypedDict, total=False):
    text: Required[str]
    """The text to generate a summary for.

    Can be up to 100,000 characters long. Currently the only supported language is
    English.
    """

    additional_command: str
    """A free-form instruction for modifying how the summaries get generated.

    Should complete the sentence "Generate a summary \\__". Eg. "focusing on the next
    steps" or "written by Yoda"
    """

    extractiveness: Literal["low", "medium", "high"]
    """One of `low`, `medium`, `high`, or `auto`, defaults to `auto`.

    Controls how close to the original text the summary is. `high` extractiveness
    summaries will lean towards reusing sentences verbatim, while `low`
    extractiveness summaries will tend to paraphrase more. If `auto` is selected,
    the best option will be picked based on the input text.
    """

    format: Literal["paragraph", "bullets"]
    """One of `paragraph`, `bullets`, or `auto`, defaults to `auto`.

    Indicates the style in which the summary will be delivered - in a free form
    paragraph or in bullet points. If `auto` is selected, the best option will be
    picked based on the input text.
    """

    length: Literal["short", "medium", "long"]
    """One of `short`, `medium`, `long`, or `auto` defaults to `auto`.

    Indicates the approximate length of the summary. If `auto` is selected, the best
    option will be picked based on the input text.
    """

    model: Literal["command", "command-light"]
    """The identifier of the model to generate the summary with.

    Currently available models are `command` (default), `command-nightly`
    (experimental), `command-light`, and `command-light-nightly` (experimental).
    Smaller, "light" models are faster, while larger models will perform better.
    """

    temperature: float
    """Ranges from 0 to 5.

    Controls the randomness of the output. Lower values tend to generate more
    “predictable” output, while higher values tend to generate more “creative”
    output. The sweet spot is typically between 0 and 1.
    """
