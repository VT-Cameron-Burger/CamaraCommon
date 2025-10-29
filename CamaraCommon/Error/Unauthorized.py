"""HTTP 401 Unauthorized error responses for CAMARA APIs."""

from enum import Enum

from pydantic import BaseModel, Field

from .ErrorInfo import ErrorInfo


class UnauthorizedCode(str, Enum):
    """Error codes for HTTP 401 Unauthorized responses."""

    UNAUTHENTICATED = "UNAUTHENTICATED"


class Unauthorized(ErrorInfo):
    """
    HTTP 401 Unauthorized error response.

    Based on CAMARA common.yaml Generic401 response.
    """

    def __init__(self, code: str, message: str, status: int = 401, **kwargs):
        super().__init__(status=status, code=code, message=message, **kwargs)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "status": 401,
                    "code": "UNAUTHENTICATED",
                    "message": (
                        "Request not authenticated due to missing, invalid, or expired credentials. A new authentication is required."
                    ),
                }
            ]
        }
    }
