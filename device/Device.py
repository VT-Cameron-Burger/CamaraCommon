"""Device data type for CAMARA APIs."""

from typing import Optional
from pydantic import BaseModel, model_validator
from ..communication.PhoneNumber import PhoneNumber
from ..communication.NetworkAccessIdentifier import NetworkAccessIdentifier
from ..network.DeviceIpv4Addr import DeviceIpv4Addr
from ..network.DeviceIpv6Address import DeviceIpv6Address


class Device(BaseModel):
    """
    End-user equipment able to connect to a mobile network.
    Examples of devices include smartphones or IoT sensors/actuators.

    The developer can choose to provide the below specified device identifiers:
    * ipv4Address
    * ipv6Address
    * phoneNumber
    * networkAccessIdentifier

    NOTE1: the network operator might support only a subset of these options.
    The API invoker can provide multiple identifiers to be compatible across
    different network operators. In this case the identifiers MUST belong to
    the same device.

    NOTE2: as for this Commonalities release, we are enforcing that the
    networkAccessIdentifier is only part of the schema for future-proofing,
    and CAMARA does not currently allow its use.
    """

    phoneNumber: Optional[PhoneNumber] = None
    networkAccessIdentifier: Optional[NetworkAccessIdentifier] = None
    ipv4Address: Optional[DeviceIpv4Addr] = None
    ipv6Address: Optional[DeviceIpv6Address] = None

    @model_validator(mode="after")
    def validate_min_properties(self) -> "Device":
        """Validate that at least one identifier is provided."""
        identifiers = [
            self.phoneNumber,
            self.networkAccessIdentifier,
            self.ipv4Address,
            self.ipv6Address,
        ]

        if not any(identifiers):
            raise ValueError("At least one device identifier must be provided")

        return self
