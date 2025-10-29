"""HTTP 429 Too Many Requests error responses for CAMARA APIs."""

from enum import Enum
from pydantic import BaseModel, Field
from .ErrorInfo import ErrorInfo


class TooManyRequestsCode(str, Enum):
    """Error codes for HTTP 429 Too Many Requests responses."""

    QUOTA_EXCEEDED = "QUOTA_EXCEEDED"
    TOO_MANY_REQUESTS = "TOO_MANY_REQUESTS"


class TooManyRequests(ErrorInfo):
    """
    HTTP 429 Too Many Requests error response.

    Based on CAMARA common.yaml Generic429 response.
    """

    def __init__(self, code: str, message: str, status: int = 429, **kwargs):
        super().__init__(status=status, code=code, message=message, **kwargs)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "status": 429,
                    "code": "QUOTA_EXCEEDED",
                    "message": "Out of resource quota.",
                },
                {
                    "status": 429,
                    "code": "TOO_MANY_REQUESTS",
                    "message": "Rate limit reached.",
                },
            ]
        }
    }
