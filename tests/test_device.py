"""
Tests for device data types.
"""

import pytest

from CommonDataTypes.device import Device, DeviceResponse
from CommonDataTypes.communication import PhoneNumber, NetworkAccessIdentifier
from CommonDataTypes.network import (
    DeviceIpv4Addr,
    DeviceIpv6Address,
    SingleIpv4Addr,
    Port,
)


class TestDevice:
    """Test Device validation."""

    def test_device_with_phone_number(self):
        """Test Device with phone number identifier."""
        device = Device(phoneNumber=PhoneNumber(value="+1234567890"))
        assert device.phoneNumber is not None
        assert device.phoneNumber.value == "+1234567890"
        assert device.networkAccessIdentifier is None
        assert device.ipv4Address is None
        assert device.ipv6Address is None

    def test_device_with_network_access_identifier(self):
        """Test Device with network access identifier."""
        device = Device(
            networkAccessIdentifier=NetworkAccessIdentifier(value="user@example.com")
        )
        assert device.networkAccessIdentifier is not None
        assert device.networkAccessIdentifier.value == "user@example.com"
        assert device.phoneNumber is None
        assert device.ipv4Address is None
        assert device.ipv6Address is None

    def test_device_with_ipv4_address(self):
        """Test Device with IPv4 address."""
        ipv4_addr = DeviceIpv4Addr(
            publicAddress=SingleIpv4Addr(value="84.125.93.10"),
            publicPort=Port(value=59765),
        )
        device = Device(ipv4Address=ipv4_addr)
        assert device.ipv4Address is not None
        assert device.ipv4Address.publicAddress.value == "84.125.93.10"
        assert device.phoneNumber is None
        assert device.networkAccessIdentifier is None
        assert device.ipv6Address is None

    def test_device_with_ipv6_address(self):
        """Test Device with IPv6 address."""
        device = Device(
            ipv6Address=DeviceIpv6Address(value="2001:db8:85a3:8d3:1319:8a2e:370:7344")
        )
        assert device.ipv6Address is not None
        assert device.ipv6Address.value == "2001:db8:85a3:8d3:1319:8a2e:370:7344"
        assert device.phoneNumber is None
        assert device.networkAccessIdentifier is None
        assert device.ipv4Address is None

    def test_device_with_multiple_identifiers(self):
        """Test Device with multiple identifiers."""
        ipv4_addr = DeviceIpv4Addr(
            publicAddress=SingleIpv4Addr(value="84.125.93.10"),
            publicPort=Port(value=59765),
        )
        device = Device(
            phoneNumber=PhoneNumber(value="+1234567890"), ipv4Address=ipv4_addr
        )
        assert device.phoneNumber is not None
        assert device.phoneNumber.value == "+1234567890"
        assert device.ipv4Address is not None
        assert device.ipv4Address.publicAddress.value == "84.125.93.10"

    def test_device_no_identifiers(self):
        """Test Device with no identifiers (should fail)."""
        with pytest.raises(
            ValueError, match="At least one device identifier must be provided"
        ):
            Device()


class TestDeviceResponse:
    """Test DeviceResponse validation."""

    def test_device_response_with_phone_number(self):
        """Test DeviceResponse with exactly one phone number."""
        device_response = DeviceResponse(phoneNumber=PhoneNumber(value="+1234567890"))
        assert device_response.phoneNumber is not None
        assert device_response.phoneNumber.value == "+1234567890"
        assert device_response.networkAccessIdentifier is None
        assert device_response.ipv4Address is None
        assert device_response.ipv6Address is None

    def test_device_response_with_ipv4(self):
        """Test DeviceResponse with exactly one IPv4 address."""
        ipv4_addr = DeviceIpv4Addr(
            publicAddress=SingleIpv4Addr(value="84.125.93.10"),
            publicPort=Port(value=59765),
        )
        device_response = DeviceResponse(ipv4Address=ipv4_addr)
        assert device_response.ipv4Address is not None
        assert device_response.ipv4Address.publicAddress.value == "84.125.93.10"
        assert device_response.phoneNumber is None
        assert device_response.networkAccessIdentifier is None
        assert device_response.ipv6Address is None

    def test_device_response_multiple_identifiers(self):
        """Test DeviceResponse with multiple identifiers (should fail)."""
        with pytest.raises(
            ValueError,
            match="Exactly one device identifier must be provided in response",
        ):
            DeviceResponse(
                phoneNumber=PhoneNumber(value="+1234567890"),
                ipv4Address=DeviceIpv4Addr(
                    publicAddress=SingleIpv4Addr(value="84.125.93.10"),
                    publicPort=Port(value=59765),
                ),
            )

    def test_device_response_no_identifiers(self):
        """Test DeviceResponse with no identifiers (should fail with parent Device validation)."""
        with pytest.raises(
            ValueError, match="At least one device identifier must be provided"
        ):
            DeviceResponse()
