"""DeviceResponse data type for CAMARA APIs."""

from pydantic import BaseModel, model_validator

from .Device import Device


class DeviceResponse(Device):
    """
    An identifier for the end-user equipment able to connect to the network
    that the response refers to. This parameter is only returned when the API
    consumer includes the device parameter in their request (i.e. they are using
    a two-legged access token), and is relevant when more than one device
    identifier is specified, as only one of those device identifiers is allowed
    in the response.

    If the API consumer provides more than one device identifier in their request,
    and this schema is included in the response definition, the API provider MUST
    use it to return a single identifier which is the one they are using to fulfil
    the request, even if the identifiers do not match the same device. API provider
    does not perform any logic to validate/correlate that the indicated device
    identifiers match the same device. No error should be returned if the
    identifiers are otherwise valid to prevent API consumers correlating different
    identifiers with a given end user.
    """

    @model_validator(mode="after")
    def validate_max_properties(self) -> "DeviceResponse":
        """Validate that exactly one identifier is provided (maxProperties: 1)."""
        identifiers = [
            self.phoneNumber,
            self.networkAccessIdentifier,
            self.ipv4Address,
            self.ipv6Address,
        ]

        provided_count = sum(1 for identifier in identifiers if identifier is not None)

        if provided_count != 1:
            raise ValueError(
                "Exactly one device identifier must be provided in response"
            )

        return self
