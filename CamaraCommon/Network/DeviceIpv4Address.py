"""DeviceIpv4Addr data type for CAMARA APIs."""

import ipaddress
from typing import Optional
from pydantic import BaseModel, model_validator
from .Port import Port


class DeviceIpv4Address(BaseModel):
    """
    The device should be identified by either the public (observed) IP address
    and port as seen by the application server, or the private (local) and any
    public (observed) IP addresses in use by the device.

    If the allocated and observed IP addresses are the same (i.e. NAT is not in use)
    then the same address should be specified for both publicAddress and privateAddress.

    If NAT64 is in use, the device should be identified by its publicAddress and
    publicPort, or separately by its allocated IPv6 address.

    In all cases, publicAddress must be specified, along with at least one of
    either privateAddress or publicPort.
    """

    publicAddress: str
    privateAddress: Optional[str] = None
    publicPort: Optional[Port] = None

    @model_validator(mode="after")
    def validate_device_ipv4(self) -> "DeviceIpv4Address":
        """Validate that at least privateAddress or publicPort is provided."""
        if not self.privateAddress and not self.publicPort:
            raise ValueError(
                "Either privateAddress or publicPort must be specified along with publicAddress"
            )
        # Validate that publicAddress is a valid IPv4 address

        try:
            ipaddress.IPv4Address(self.publicAddress)
        except ipaddress.AddressValueError:
            raise ValueError(f"Invalid IPv4 address: {self.publicAddress}")

        # Validate that privateAddress is a valid IPv4 address if provided
        if self.privateAddress is not None:
            try:
                ipaddress.IPv4Address(self.privateAddress)
            except ipaddress.AddressValueError:
                raise ValueError(f"Invalid IPv4 address: {self.privateAddress}")
        return self

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "publicAddress": {"value": "84.125.93.10"},
                    "publicPort": {"value": 59765},
                }
            ]
        }
    }
