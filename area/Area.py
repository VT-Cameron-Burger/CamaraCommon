"""Area base schema for CAMARA APIs."""

from pydantic import BaseModel
from .AreaType import AreaType


class Area(BaseModel):
    """
    Base schema for all areas.

    This is used with discriminator for Circle and Polygon types.
    """

    areaType: AreaType
