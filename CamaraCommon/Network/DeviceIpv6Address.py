"""DeviceIpv6Address data type for CAMARA APIs."""

import ipaddress

from pydantic import BaseModel, field_validator


class DeviceIpv6Address(BaseModel):
    """
    The device should be identified by the observed IPv6 address,
    or by any single IPv6 address from within the subnet allocated
    to the device (e.g. adding ::0 to the /64 prefix).
    """

    value: str

    @field_validator("value")
    @classmethod
    def validate_ipv6(cls, v: str) -> str:
        """Validate IPv6 address format."""
        try:
            ipaddress.IPv6Address(v)
        except ipaddress.AddressValueError:
            raise ValueError(f"Invalid IPv6 address: {v}")
        return v

    def __str__(self) -> str:
        return self.value

    model_config = {
        "json_schema_extra": {"examples": ["2001:db8:85a3:8d3:1319:8a2e:370:7344"]}
    }
