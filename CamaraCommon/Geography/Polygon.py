"""Polygon area type for CAMARA APIs."""

from pydantic import BaseModel

from .Area import Area
from .AreaType import AreaType
from .PointList import PointList


class Polygon(Area):
    """
    Polygonal area. The Polygon should be a simple polygon,
    i.e. should not intersect itself.

    Defined by a boundary of 3-15 points.
    """

    areaType: AreaType = AreaType.POLYGON
    boundary: PointList
