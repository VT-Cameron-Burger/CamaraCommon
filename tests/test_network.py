"""
Tests for network data types (IP addresses, ports).
"""

import pytest

from CamaraCommon.Network import (
    DeviceIpv6Address,
    DeviceIpv4Address,
    Port,
)


class TestSingleIpv4Address:
    """Test SingleIpv4Address validation."""

    def test_valid_ipv4_addresses(self):
        """Test valid IPv4 addresses."""
        valid_addresses = [
            "192.168.1.1",
            "10.0.0.1",
            "172.16.0.1",
            "8.8.8.8",
            "1.1.1.1",
            "255.255.255.255",
            "0.0.0.0",
        ]

        for address in valid_addresses:
            ipv4 = DeviceIpv4Address(publicAddress=address, privateAddress="0.0.0.0")
            assert ipv4.publicAddress == address

    def test_invalid_ipv4_addresses(self):
        """Test invalid IPv4 addresses."""
        invalid_addresses = [
            "256.1.1.1",  # Octet > 255
            "192.168.1.256",  # Last octet > 255
            "192.168.1",  # Missing octet
            "192.168.1.1.1",  # Extra octet
            "192.168.001.1",  # Leading zeros
            "192.168.-1.1",  # Negative number
            "192.168.1.a",  # Letter in octet
            "not.an.ip.address",  # Invalid format
            "",  # Empty string
        ]

        for address in invalid_addresses:
            with pytest.raises(ValueError):
                DeviceIpv4Address(publicAddress=address)


class TestDeviceIpv6Address:
    """Test DeviceIpv6Address validation."""

    def test_valid_ipv6_addresses(self):
        """Test valid IPv6 addresses."""
        valid_addresses = [
            "2001:db8:85a3:8d3:1319:8a2e:370:7344",
            "2001:db8::1",
            "::1",
            "fe80::1",
            "2001:0db8:85a3:0000:0000:8a2e:0370:7334",
            "::ffff:192.0.2.1",  # IPv4-mapped IPv6
        ]

        for address in valid_addresses:
            ipv6 = DeviceIpv6Address(value=address)
            assert ipv6.value == address

    def test_invalid_ipv6_addresses(self):
        """Test invalid IPv6 addresses."""
        invalid_addresses = [
            "2001:db8:85a3:8d3:1319:8a2e:370:7344:extra",  # Too many groups
            "2001:db8:85a3::8d3::1319",  # Multiple ::
            "2001:db8:85a3:8d3g:1319:8a2e:370:7344",  # Invalid hex char
            "192.168.1.1",  # IPv4 address
            "",  # Empty string
            "not:an:ipv6:address",  # Invalid format
        ]

        for address in invalid_addresses:
            with pytest.raises(ValueError):
                DeviceIpv6Address(value=address)


class TestPort:
    """Test Port validation."""

    def test_valid_ports(self):
        """Test valid port numbers."""
        valid_ports = [1, 80, 443, 8080, 65535]

        for port_num in valid_ports:
            port = Port(value=port_num)
            assert port.value == port_num

    def test_invalid_ports(self):
        """Test invalid port numbers."""
        invalid_ports = [-1, 65536, 100000]  # Note: 0 is valid

        for port_num in invalid_ports:
            with pytest.raises(ValueError):
                Port(value=port_num)

    def test_port_zero_is_valid(self):
        """Test that port 0 is valid."""
        port = Port(value=0)
        assert port.value == 0

    def test_port_edge_cases(self):
        """Test port edge cases."""
        # Minimum valid port
        min_port = Port(value=1)
        assert min_port.value == 1

        # Maximum valid port
        max_port = Port(value=65535)
        assert max_port.value == 65535


class TestDeviceIpv4Addr:
    """Test DeviceIpv4Addr validation."""

    def test_valid_device_ipv4_with_port(self):
        """Test valid DeviceIpv4Addr with public port."""
        device_ipv4 = DeviceIpv4Address(
            publicAddress="84.125.93.10",
            publicPort=Port(value=59765),
        )
        assert device_ipv4.publicAddress == "84.125.93.10"
        assert device_ipv4.publicPort is not None
        assert device_ipv4.publicPort.value == 59765
        assert device_ipv4.privateAddress is None

    def test_valid_device_ipv4_with_private_address(self):
        """Test valid DeviceIpv4Addr with private address."""
        device_ipv4 = DeviceIpv4Address(
            publicAddress="84.125.93.10",
            privateAddress="192.168.1.100",
        )
        assert device_ipv4.publicAddress == "84.125.93.10"
        assert device_ipv4.privateAddress is not None
        assert device_ipv4.privateAddress == "192.168.1.100"
        assert device_ipv4.publicPort is None

    def test_valid_device_ipv4_with_both(self):
        """Test valid DeviceIpv4Addr with both private address and public port."""
        device_ipv4 = DeviceIpv4Address(
            publicAddress="84.125.93.10",
            privateAddress="192.168.1.100",
            publicPort=Port(value=8080),
        )
        assert device_ipv4.publicAddress == "84.125.93.10"
        assert device_ipv4.privateAddress is not None
        assert device_ipv4.privateAddress == "192.168.1.100"
        assert device_ipv4.publicPort is not None
        assert device_ipv4.publicPort.value == 8080

    def test_invalid_device_ipv4_missing_required(self):
        """Test invalid DeviceIpv4Addr missing privateAddress and publicPort."""
        with pytest.raises(
            ValueError, match="Either privateAddress or publicPort must be specified"
        ):
            DeviceIpv4Address(
                publicAddress="84.125.93.10"
                # Missing both privateAddress and publicPort
            )
