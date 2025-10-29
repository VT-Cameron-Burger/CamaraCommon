"""HTTP 503 Service Unavailable error responses for CAMARA APIs."""

from enum import Enum

from pydantic import BaseModel, Field

from .ErrorInfo import ErrorInfo


class ServiceUnavailableCode(str, Enum):
    """Error codes for HTTP 503 Service Unavailable responses."""

    UNAVAILABLE = "UNAVAILABLE"


class ServiceUnavailable(ErrorInfo):
    """
    HTTP 503 Service Unavailable error response.

    Based on CAMARA common.yaml Generic503 response.
    """

    def __init__(self, code: str, message: str, status: int = 503, **kwargs):
        super().__init__(status=status, code=code, message=message, **kwargs)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "status": 503,
                    "code": "UNAVAILABLE",
                    "message": "Service Unavailable.",
                }
            ]
        }
    }
