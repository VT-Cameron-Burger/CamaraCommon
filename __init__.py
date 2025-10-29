"""
CAMARA Common Data Types

This package contains Pydantic models for all common data types
used across CAMARA APIs, as defined in CAMARA_common.yaml.

Usage:
    from CamaraCommon.Basic import XCorrelator, TimePeriod
    from CamaraCommon.Communication import PhoneNumber, NetworkAccessIdentifier
    from CamaraCommon.Network import Port, SingleIpv4Addr, DeviceIpv4Addr, DeviceIpv6Address
    from CamaraCommon.Device import Device, DeviceResponse
    from CamaraCommon.Geography import Point, Circle, Area, Latitude, Longitude
    from CamaraCommon.Error import ErrorInfo, ErrorFactory, BadRequest
"""
