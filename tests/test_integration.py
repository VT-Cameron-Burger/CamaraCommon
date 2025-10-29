"""
Integration test runner for all CamaraCommon tests.
"""

import pytest
import sys
from pathlib import Path

from CamaraCommon.Basic import *
from CamaraCommon.Communication import *
from CamaraCommon.Device import *
from CamaraCommon.Error import *
from CamaraCommon.Geography import *
from CamaraCommon.Network import *


def test_package_imports():
    """Test that all CamaraCommon can be imported."""
    # Basic types
    assert XCorrelator is not None
    assert TimePeriod is not None
    assert ErrorInfo is not None

    # Communication types
    assert PhoneNumber is not None
    assert NetworkAccessIdentifier is not None

    # Network types
    assert DeviceIpv6Address is not None
    assert Port is not None

    # Geography types
    assert Latitude is not None
    assert Longitude is not None
    assert Point is not None
    assert PointList is not None

    # Area types
    assert AreaType is not None
    assert Area is not None
    assert Circle is not None
    assert Polygon is not None

    # Device types
    assert Device is not None
    assert DeviceResponse is not None


def test_basic_integration():
    """Test basic integration of all types working together."""
    # Create a device with multiple identifiers
    device = Device(
        phoneNumber=PhoneNumber(value="+1234567890"),
        ipv4Address=DeviceIpv4Address(
            publicAddress="192.168.1.1",
            publicPort=Port(value=8080),
        ),
    )

    # Create a location
    center = Point(
        latitude=Latitude(value=50.735851), longitude=Longitude(value=7.10066)
    )
    area = Circle(center=center, radius=1000.0)

    # Create error info
    error = ErrorInfo(status=400, code="INVALID_DEVICE", message="Device not found")

    # Create correlation ID
    correlator = XCorrelator(value="integration-test-123")

    # Verify all objects created successfully
    assert device.phoneNumber is not None
    assert device.phoneNumber.value == "+1234567890"
    assert area.center.latitude.value == 50.735851
    assert error.status == 400
    assert correlator.value == "integration-test-123"


if __name__ == "__main__":
    # Run tests with pytest
    pytest.main([__file__, "-v"])
