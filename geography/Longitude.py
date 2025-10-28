"""Longitude data type for CAMARA APIs."""

from pydantic import BaseModel, Field


class Longitude(BaseModel):
    """
    Longitude component of location.

    Valid range: -180 to 180 degrees
    """

    value: float = Field(
        ge=-180.0, le=180.0, description="Longitude component of location"
    )

    def __float__(self) -> float:
        return self.value

    def __str__(self) -> str:
        return str(self.value)
