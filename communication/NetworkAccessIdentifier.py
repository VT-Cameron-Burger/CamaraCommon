"""NetworkAccessIdentifier data type for CAMARA APIs."""

from pydantic import BaseModel


class NetworkAccessIdentifier(BaseModel):
    """
    A public identifier addressing a subscription in a mobile network.

    In 3GPP terminology, it corresponds to the GPSI formatted with the
    External Identifier ({Local Identifier}@{Domain Identifier}).
    Unlike the telephone number, the network access identifier is not
    subjected to portability ruling in force, and is individually
    managed by each operator.
    """

    value: str

    def __str__(self) -> str:
        return self.value

    model_config = {"json_schema_extra": {"examples": ["123456789@example.com"]}}
