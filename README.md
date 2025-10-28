# CAMARA Common Data Types - Python Implementation

A Python package containing Pydantic models for all common data types used across CAMARA APIs, as defined in the CAMARA common specification.

> **Note**: This is a Python implementation of the official CAMARA Common Data Types. While this package maintains full compatibility with CAMARA specifications, it is independently maintained. For the official CAMARA specifications, visit the [CAMARA Project](https://github.com/camaraproject).

## Overview

This package provides validated Python classes for CAMARA API data types, organized into logical modules:

- **Basic Types** - Core data structures (XCorrelator, TimePeriod, ErrorInfo)
- **Communication** - Identifiers (PhoneNumber, NetworkAccessIdentifier)  
- **Network** - IP addresses and ports (IPv4, IPv6, Port)
- **Device** - Device identification models
- **Geography** - Coordinates and points (Latitude, Longitude, Point)
- **Area** - Geometric areas (Circle, Polygon)

## Installation

```bash
pip install -e .
```

## Quick Start

```python
from CommonDataTypes import PhoneNumber, Device, Circle, Point, Latitude, Longitude

# Create a phone number with E.164 validation
phone = PhoneNumber(value="+1234567890")

# Create a device with phone identifier
device = Device(phoneNumber=phone)

# Create geographic coordinates
point = Point(
    latitude=Latitude(value=50.735851),
    longitude=Longitude(value=7.10066)
)

# Create a circular area
area = Circle(center=point, radius=1000.0)
```

## Package Structure

```
CommonDataTypes/
├── basic/           # Core data types
│   ├── XCorrelator.py
│   ├── TimePeriod.py
│   └── ErrorInfo.py
├── communication/   # Communication identifiers
│   ├── PhoneNumber.py
│   └── NetworkAccessIdentifier.py
├── network/         # Network addressing
│   ├── Port.py
│   ├── SingleIpv4Addr.py
│   ├── DeviceIpv6Address.py
│   └── DeviceIpv4Addr.py
├── device/          # Device identification
│   ├── Device.py
│   └── DeviceResponse.py
├── geography/       # Geographic coordinates
│   ├── Latitude.py
│   ├── Longitude.py
│   ├── Point.py
│   └── PointList.py
└── area/           # Geometric areas
    ├── AreaType.py
    ├── Area.py
    ├── Circle.py
    └── Polygon.py
```

## Key Features

- **✅ Full Pydantic v2 Support** - Modern validation with excellent performance
- **✅ CAMARA Specification Compliant** - Matches official CAMARA common schema
- **✅ Type Safety** - Complete type annotations and validation
- **✅ Comprehensive Testing** - Full test suite included
- **✅ Well Organized** - Logical module structure for easy navigation

## Data Types

### Basic Types

- **XCorrelator** - Correlation ID with pattern validation
- **TimePeriod** - RFC 3339 datetime periods
- **ErrorInfo** - Standard error response structure

### Communication Types

- **PhoneNumber** - E.164 international phone numbers
- **NetworkAccessIdentifier** - GPSI network identifiers

### Network Types

- **Port** - TCP/UDP port validation (0-65535)
- **SingleIpv4Addr** - IPv4 address validation
- **DeviceIpv6Address** - IPv6 address validation
- **DeviceIpv4Addr** - Complex IPv4 device addressing with NAT support

### Device Types

- **Device** - Multi-identifier device model (requires ≥1 identifier)
- **DeviceResponse** - Single-identifier response model (requires exactly 1)

### Geography Types

- **Latitude** - Latitude validation (-90 to 90)
- **Longitude** - Longitude validation (-180 to 180)
- **Point** - Geographic coordinate pair
- **PointList** - List of 3-15 points for polygons

### Area Types

- **AreaType** - CIRCLE/POLYGON enumeration
- **Area** - Base area class with discriminator
- **Circle** - Circular area with center and radius
- **Polygon** - Polygonal area with boundary points

## Validation Examples

```python
from CommonDataTypes import PhoneNumber, XCorrelator, Circle

# Phone number validation (E.164 format)
phone = PhoneNumber(value="+1234567890")  # ✅ Valid
# PhoneNumber(value="123456789")          # ❌ Missing + prefix

# Correlation ID validation
correlator = XCorrelator(value="api-request-123")  # ✅ Valid
# XCorrelator(value="invalid@symbol")               # ❌ Invalid characters

# Geographic area validation
circle = Circle(
    center=Point(
        latitude=Latitude(value=50.735851),
        longitude=Longitude(value=7.10066)
    ),
    radius=1000.0  # meters
)
```

## Testing

Run the comprehensive test suite:

```bash
python test_common_types.py
```

## Requirements

- Python 3.8+
- Pydantic v2.12+

## License

Apache 2.0 - See LICENSE file for details

## Contributing

This package implements the official CAMARA common specification in Python. 

### For Python Implementation Issues
- Report bugs or request features: [GitHub Issues](https://github.com/VT-Cameron-Burger/camara-data-types/issues)
- Submit pull requests for implementation improvements

### For CAMARA Specification Changes
- Contribute to the upstream CAMARA specification: [CAMARA Commonalities](https://github.com/camaraproject/Commonalities)
- Changes to data models should be proposed to the official CAMARA project

## CAMARA Project

This package implements data types from the [CAMARA project](https://github.com/camaraproject), which aims to define, develop, and test the APIs for the telco edge. 

### Related Links
- [CAMARA Project Home](https://github.com/camaraproject)
- [CAMARA Common Specification](https://github.com/camaraproject/Commonalities)
- [Official CAMARA APIs](https://github.com/camaraproject)

## Author

**Cameron Burger**
- Email: cameronburger@vt.edu
- GitHub: [@VT-Cameron-Burger](https://github.com/VT-Cameron-Burger)
- Package Repository: [camara-data-types](https://github.com/VT-Cameron-Burger/camara-data-types)