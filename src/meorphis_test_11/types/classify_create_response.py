# File generated from our OpenAPI spec by Stainless.

from typing import Dict, List, Optional

from .._models import BaseModel

__all__ = ["ClassifyCreateResponse", "Classification", "ClassificationLabels", "Meta", "MetaAPIVersion"]


class ClassificationLabels(BaseModel):
    confidence: Optional[float] = None


class Classification(BaseModel):
    id: str

    confidence: float
    """The confidence score for the top predicted class"""

    labels: Dict[str, ClassificationLabels]
    """A map containing each label and its confidence score according to the
    classifier.

    All the confidence scores add up to 1.
    """

    prediction: str
    """The predicted label for the associated query"""

    confidences: Optional[List[object]] = None
    """
    An array containing each label and its confidence score according to the
    classifier
    """

    input: Optional[str] = None
    """The input text that was classified"""


class MetaAPIVersion(BaseModel):
    version: str

    is_deprecated: Optional[bool] = None

    is_experimental: Optional[bool] = None


class Meta(BaseModel):
    api_version: Optional[List[MetaAPIVersion]] = None

    warnings: Optional[List[str]] = None


class ClassifyCreateResponse(BaseModel):
    id: str

    classifications: List[Classification]

    meta: Optional[List[Meta]] = None
