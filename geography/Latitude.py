"""Latitude data type for CAMARA APIs."""

from pydantic import BaseModel, Field


class Latitude(BaseModel):
    """
    Latitude component of a location.

    Valid range: -90 to 90 degrees
    """

    value: float = Field(
        ge=-90.0, le=90.0, description="Latitude component of a location"
    )

    def __float__(self) -> float:
        return self.value

    def __str__(self) -> str:
        return str(self.value)
