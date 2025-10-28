"""Port data type for CAMARA APIs."""

from pydantic import BaseModel, Field


class Port(BaseModel):
    """
    TCP or UDP port number.

    Valid range: 0-65535
    """

    value: int = Field(ge=0, le=65535, description="TCP or UDP port number")

    def __int__(self) -> int:
        return self.value

    def __str__(self) -> str:
        return str(self.value)
