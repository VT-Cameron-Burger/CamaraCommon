"""HTTP 404 Not Found error responses for CAMARA APIs."""

from enum import Enum

from pydantic import BaseModel, Field

from .ErrorInfo import ErrorInfo


class NotFoundCode(str, Enum):
    """Error codes for HTTP 404 Not Found responses."""

    NOT_FOUND = "NOT_FOUND"
    IDENTIFIER_NOT_FOUND = "IDENTIFIER_NOT_FOUND"


class NotFound(ErrorInfo):
    """
    HTTP 404 Not Found error response.

    Based on CAMARA common.yaml Generic404 response.
    """

    def __init__(self, code: str, message: str, status: int = 404, **kwargs):
        super().__init__(status=status, code=code, message=message, **kwargs)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "status": 404,
                    "code": "NOT_FOUND",
                    "message": "The specified resource is not found.",
                },
                {
                    "status": 404,
                    "code": "IDENTIFIER_NOT_FOUND",
                    "message": "Device identifier not found.",
                },
            ]
        }
    }
