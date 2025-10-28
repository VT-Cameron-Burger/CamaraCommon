"""TimePeriod data type for CAMARA APIs."""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, ConfigDict


class TimePeriod(BaseModel):
    """
    Time period with start and optional end date.

    Both dates must follow RFC 3339 format and include time zone.
    """

    model_config = ConfigDict(
        # Use modern serialization instead of deprecated json_encoders
        json_schema_extra={
            "examples": [
                {
                    "startDate": "2023-01-01T12:00:00Z",
                    "endDate": "2023-01-02T12:00:00Z"
                }
            ]
        }
    )

    startDate: datetime = Field(
        description="An instant of time, starting of the TimePeriod. It must follow RFC 3339 and must have time zone."
    )

    endDate: Optional[datetime] = Field(
        None,
        description="An instant of time, ending of the TimePeriod. If not included, then the period has no ending date. It must follow RFC 3339 and must have time zone.",
    )
