"""PhoneNumber data type for CAMARA APIs."""

from pydantic import BaseModel, Field


class PhoneNumber(BaseModel):
    """
    A public identifier addressing a telephone subscription.

    In mobile networks it corresponds to the MSISDN (Mobile Station International
    Subscriber Directory Number). Must be formatted in international format,
    according to E.164 standard, prefixed with '+'.
    """

    value: str = Field(
        pattern=r"^\+[1-9][0-9]{4,14}$",
        description="Phone number in international E.164 format, prefixed with '+'",
        examples=["+123456789"],
    )

    def __str__(self) -> str:
        return self.value
