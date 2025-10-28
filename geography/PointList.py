"""PointList data type for CAMARA APIs."""

from typing import List
from pydantic import BaseModel, field_validator
from .Point import Point


class PointList(BaseModel):
    """
    List of points defining a polygon.

    Must have between 3 and 15 points.
    """

    points: List[Point]

    @field_validator("points")
    @classmethod
    def validate_point_count(cls, v: List[Point]) -> List[Point]:
        """Validate point count is between 3 and 15."""
        if len(v) < 3:
            raise ValueError("PointList must have at least 3 points")
        if len(v) > 15:
            raise ValueError("PointList must have at most 15 points")
        return v

    def __len__(self) -> int:
        return len(self.points)

    def __getitem__(self, index: int) -> Point:
        return self.points[index]
