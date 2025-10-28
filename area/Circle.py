"""Circle area type for CAMARA APIs."""

from pydantic import BaseModel, Field
from .Area import Area
from .AreaType import AreaType
from ..geography.Point import Point


class Circle(Area):
    """
    Circular area.

    Defined by a center point and radius in meters.
    """

    areaType: AreaType = AreaType.CIRCLE
    center: Point
    radius: float = Field(ge=1, description="Distance from the center in meters")
