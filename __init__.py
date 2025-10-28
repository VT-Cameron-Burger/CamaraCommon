"""
CAMARA Common Data Types

This package contains Pydantic models for all common data types
used across CAMARA APIs, as defined in CAMARA_common.yaml.
"""

# Basic types
from .basic.XCorrelator import XCorrelator
from .basic.TimePeriod import TimePeriod
from .basic.ErrorInfo import ErrorInfo

# Communication types
from .communication.PhoneNumber import PhoneNumber
from .communication.NetworkAccessIdentifier import NetworkAccessIdentifier

# Network types
from .network.Port import Port
from .network.SingleIpv4Addr import SingleIpv4Addr
from .network.DeviceIpv6Address import DeviceIpv6Address
from .network.DeviceIpv4Addr import DeviceIpv4Addr

# Device types
from .device.Device import Device
from .device.DeviceResponse import DeviceResponse

# Geography types
from .geography.Latitude import Latitude
from .geography.Longitude import Longitude
from .geography.Point import Point
from .geography.PointList import PointList

# Area types
from .area.AreaType import AreaType
from .area.Area import Area
from .area.Circle import Circle
from .area.Polygon import Polygon

__all__ = [
    # Basic types
    "XCorrelator",
    "TimePeriod",
    "ErrorInfo",
    # Communication types
    "PhoneNumber",
    "NetworkAccessIdentifier",
    # Network types
    "Port",
    "SingleIpv4Addr",
    "DeviceIpv6Address",
    "DeviceIpv4Addr",
    # Device types
    "Device",
    "DeviceResponse",
    # Geography types
    "Latitude",
    "Longitude",
    "Point",
    "PointList",
    # Area types
    "AreaType",
    "Area",
    "Circle",
    "Polygon",
]
