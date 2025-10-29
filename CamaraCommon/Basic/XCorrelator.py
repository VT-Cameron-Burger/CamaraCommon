"""XCorrelator data type for CAMARA APIs."""

import re

from pydantic import BaseModel, Field


class XCorrelator(BaseModel):
    """
    Correlation id for the different services.

    Must match pattern: ^[a-zA-Z0-9-_:;./<>{}]{0,256}$
    """

    value: str = Field(
        pattern=r"^[a-zA-Z0-9-_:;./<>{}]{0,256}$",
        description="Correlation id for the different services",
        examples=["b4333c46-49c0-4f62-80d7-f0ef930f1c46"],
    )

    def __str__(self) -> str:
        return self.value
