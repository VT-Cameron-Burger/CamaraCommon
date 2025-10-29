"""HTTP 500 Internal Server Error responses for CAMARA APIs."""

from enum import Enum
from pydantic import BaseModel, Field
from .ErrorInfo import ErrorInfo


class InternalServerErrorCode(str, Enum):
    """Error codes for HTTP 500 Internal Server Error responses."""

    INTERNAL = "INTERNAL"


class InternalServerError(ErrorInfo):
    """
    HTTP 500 Internal Server Error response.

    Based on CAMARA common.yaml Generic500 response.
    """

    def __init__(self, code: str, message: str, status: int = 500, **kwargs):
        super().__init__(status=status, code=code, message=message, **kwargs)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "status": 500,
                    "code": "INTERNAL",
                    "message": "Unknown server error. Typically a server bug.",
                }
            ]
        }
    }
