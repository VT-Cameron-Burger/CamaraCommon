"""HTTP 400 Bad Request error responses for CAMARA APIs."""

from enum import Enum
from pydantic import BaseModel, Field
from .ErrorInfo import ErrorInfo


class BadRequestCode(str, Enum):
    """Error codes for HTTP 400 Bad Request responses."""

    INVALID_ARGUMENT = "INVALID_ARGUMENT"
    OUT_OF_RANGE = "OUT_OF_RANGE"


class BadRequest(ErrorInfo):
    """
    HTTP 400 Bad Request error response.

    Based on CAMARA common.yaml Generic400 response.
    """

    def __init__(self, code: str, message: str, status: int = 400, **kwargs):
        super().__init__(status=status, code=code, message=message, **kwargs)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "status": 400,
                    "code": "INVALID_ARGUMENT",
                    "message": (
                        "Client specified an invalid argument, request body or query param."
                    ),
                },
                {
                    "status": 400,
                    "code": "OUT_OF_RANGE",
                    "message": "Client specified an invalid range.",
                },
            ]
        }
    }
