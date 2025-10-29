"""Point data type for CAMARA APIs."""

from pydantic import BaseModel
from .Latitude import Latitude
from .Longitude import Longitude


class Point(BaseModel):
    """
    Coordinates (latitude, longitude) defining a location in a map.
    """

    latitude: Latitude
    longitude: Longitude

    model_config = {
        "json_schema_extra": {
            "examples": [
                {"latitude": {"value": 50.735851}, "longitude": {"value": 7.10066}}
            ]
        }
    }
