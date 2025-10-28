"""
CAMARA Common Data Types

This package contains Pydantic models for all common data types
used across CAMARA APIs, as defined in CAMARA_common.yaml.

Usage (when installed):
    from camara_common_data_types.geography import Point, Circle, Area
    from camara_common_data_types.basic import XCorrelator, TimePeriod
    from camara_common_data_types.communication import PhoneNumber
    from camara_common_data_types.network import Port, SingleIpv4Addr
    from camara_common_data_types.device import Device

Usage (during development in project directory):
    from geography import Point, Circle, Area
    from basic import XCorrelator, TimePeriod
    from communication import PhoneNumber
    from network import Port, SingleIpv4Addr
    from device import Device
"""