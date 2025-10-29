"""ErrorInfo data type for CAMARA APIs."""

from pydantic import BaseModel, Field


class ErrorInfo(BaseModel):
    """
    Error information structure for API responses.

    Contains HTTP status code, error code, and human-readable message.
    Based on CAMARA common.yaml ErrorInfo schema.
    """

    status: int = Field(..., description="HTTP response status code")

    code: str = Field(..., description="A human-readable code to describe the error")

    message: str = Field(
        ..., description="A human-readable description of what the event represents"
    )
