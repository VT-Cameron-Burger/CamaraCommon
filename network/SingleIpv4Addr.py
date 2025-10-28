"""SingleIpv4Addr data type for CAMARA APIs."""

from pydantic import BaseModel, field_validator
import ipaddress


class SingleIpv4Addr(BaseModel):
    """
    A single IPv4 address with no subnet mask.
    """

    value: str

    @field_validator("value")
    @classmethod
    def validate_ipv4(cls, v: str) -> str:
        """Validate IPv4 address format."""
        try:
            ipaddress.IPv4Address(v)
        except ipaddress.AddressValueError:
            raise ValueError(f"Invalid IPv4 address: {v}")
        return v

    def __str__(self) -> str:
        return self.value

    model_config = {"json_schema_extra": {"examples": ["84.125.93.10"]}}
