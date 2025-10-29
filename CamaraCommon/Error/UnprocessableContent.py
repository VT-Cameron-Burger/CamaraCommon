"""HTTP 422 Unprocessable Content error responses for CAMARA APIs."""

from enum import Enum

from pydantic import BaseModel, Field

from .ErrorInfo import ErrorInfo


class UnprocessableContentCode(str, Enum):
    """Error codes for HTTP 422 Unprocessable Content responses."""

    SERVICE_NOT_APPLICABLE = "SERVICE_NOT_APPLICABLE"
    MISSING_IDENTIFIER = "MISSING_IDENTIFIER"
    UNSUPPORTED_IDENTIFIER = "UNSUPPORTED_IDENTIFIER"
    UNNECESSARY_IDENTIFIER = "UNNECESSARY_IDENTIFIER"


class UnprocessableContent(ErrorInfo):
    """
    HTTP 422 Unprocessable Content error response.

    Based on CAMARA common.yaml Generic422 response.
    """

    def __init__(self, code: str, message: str, status: int = 422, **kwargs):
        super().__init__(status=status, code=code, message=message, **kwargs)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "status": 422,
                    "code": "SERVICE_NOT_APPLICABLE",
                    "message": (
                        "The service is not available for the provided identifier."
                    ),
                },
                {
                    "status": 422,
                    "code": "MISSING_IDENTIFIER",
                    "message": "The device cannot be identified.",
                },
                {
                    "status": 422,
                    "code": "UNSUPPORTED_IDENTIFIER",
                    "message": "The identifier provided is not supported.",
                },
                {
                    "status": 422,
                    "code": "UNNECESSARY_IDENTIFIER",
                    "message": "The device is already identified by the access token.",
                },
            ]
        }
    }
