"""AreaType enumeration for CAMARA APIs."""

from enum import Enum


class AreaType(str, Enum):
    """
    Type of area.

    CIRCLE - The area is defined as a circle.
    POLYGON - The area is defined as a polygon.
    """

    CIRCLE = "CIRCLE"
    POLYGON = "POLYGON"
