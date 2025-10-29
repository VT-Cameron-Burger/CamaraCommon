"""HTTP 403 Forbidden error responses for CAMARA APIs."""

from enum import Enum
from pydantic import BaseModel, Field
from .ErrorInfo import ErrorInfo


class ForbiddenCode(str, Enum):
    """Error codes for HTTP 403 Forbidden responses."""

    PERMISSION_DENIED = "PERMISSION_DENIED"
    INVALID_TOKEN_CONTEXT = "INVALID_TOKEN_CONTEXT"


class Forbidden(ErrorInfo):
    """
    HTTP 403 Forbidden error response.

    Based on CAMARA common.yaml Generic403 response.
    """

    def __init__(self, code: str, message: str, status: int = 403, **kwargs):
        super().__init__(status=status, code=code, message=message, **kwargs)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "status": 403,
                    "code": "PERMISSION_DENIED",
                    "message": (
                        "Client does not have sufficient permissions to perform this action."
                    ),
                },
                {
                    "status": 403,
                    "code": "INVALID_TOKEN_CONTEXT",
                    "message": "Field is not consistent with access token.",
                },
            ]
        }
    }
