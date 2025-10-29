# CAMARA Common Data Types - Python Implementation

A Python package containing Pydantic models for all common data types used across CAMARA APIs, as defined in the CAMARA common specification.

> **Note**: This is a Python implementation of the official CAMARA Common Data Types. While this package maintains full compatibility with CAMARA specifications, it is independently maintained. For the official CAMARA specifications, visit the [CAMARA Project](https://github.com/camaraproject).

## Overview

This package provides validated Python classes for CAMARA API data types, organized into logical modules:

- **Basic** - Core data structures (XCorrelator, TimePeriod)
- **Communication** - Identifiers (PhoneNumber, NetworkAccessIdentifier)  
- **Network** - IP addresses and ports (IPv4, IPv6, Port)
- **Device** - Device identification models
- **Geography** - Coordinates and points (Latitude, Longitude, Point)
- **Error** - Comprehensive error handling with HTTP status codes

## Installation

```bash
pip install -e .
```

## Quick Start

```python
from Basic import XCorrelator, TimePeriod
from Communication import PhoneNumber, NetworkAccessIdentifier
from Device import Device
from Geography import Point, Circle, Latitude, Longitude
from Error import ErrorInfo, ErrorFactory

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

# Create standardized errors
error = ErrorFactory.invalid_argument("Phone number format is invalid")
```

## Package Structure

```
CommonDataTypes/
├── Basic/           # Core data types
│   ├── XCorrelator.py
│   └── TimePeriod.py
├── Communication/   # Communication identifiers
│   ├── PhoneNumber.py
│   └── NetworkAccessIdentifier.py
├── Network/         # Network addressing
│   ├── Port.py
│   ├── SingleIpv4Addr.py
│   ├── DeviceIpv6Address.py
│   └── DeviceIpv4Addr.py
├── Device/          # Device identification
│   ├── Device.py
│   └── DeviceResponse.py
├── Geography/       # Geographic coordinates
│   ├── Latitude.py
│   ├── Longitude.py
│   ├── Point.py
│   └── PointList.py
├── Error/           # Error handling
│   ├── ErrorInfo.py
│   ├── ErrorFactory.py
│   ├── BadRequest.py
│   ├── Unauthorized.py
│   ├── Forbidden.py
│   ├── NotFound.py
│   ├── UnprocessableContent.py
│   ├── InternalServerError.py
│   ├── TooManyRequests.py
│   └── ServiceUnavailable.py
└── tests/          # Test suite
    ├── test_basic_types.py
    ├── test_communication.py
    ├── test_device.py
    ├── test_error.py
    ├── test_geography_area.py
    ├── test_integration.py
    └── test_network.py
```

## Key Features

- **✅ Full Pydantic v2 Support** - Modern validation with excellent performance
- **✅ CAMARA Specification Compliant** - Matches official CAMARA common schema
- **✅ Type Safety** - Complete type annotations and MyPy validation
- **✅ Comprehensive Testing** - Full test suite with pytest
- **✅ Error Handling** - Complete HTTP error response framework
- **✅ Development Tools** - MyPy and Black configuration included
- **✅ Well Organized** - Logical module structure for easy navigation

## Data Types

### Basic Types

- **XCorrelator** - Correlation ID with pattern validation
- **TimePeriod** - RFC 3339 datetime periods

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
- **AreaType** - CIRCLE/POLYGON enumeration
- **Area** - Base area class with discriminator
- **Circle** - Circular area with center and radius
- **Polygon** - Polygonal area with boundary points

### Error Types

- **ErrorInfo** - Base error response structure
- **ErrorFactory** - Convenient factory for creating standardized errors
- **HTTP Error Classes** - BadRequest (400), Unauthorized (401), Forbidden (403), NotFound (404), UnprocessableContent (422), TooManyRequests (429), InternalServerError (500), ServiceUnavailable (503)

## Validation Examples

```python
from Basic import XCorrelator
from Communication import PhoneNumber
from Geography import Point, Circle, Latitude, Longitude
from Error import ErrorFactory

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

# Error handling
error = ErrorFactory.invalid_argument("Invalid phone number format")
# Creates: BadRequest(status=400, code="INVALID_ARGUMENT", message="...")
```

## Testing

Run the comprehensive test suite:

```bash
# Run all tests
pytest

# Run specific test modules
pytest tests/test_error.py -v
pytest tests/test_basic_types.py -v
pytest tests/test_geography_area.py -v

# Run with coverage
pytest --cov=. tests/

# Type checking with MyPy
mypy .
```

## Development

### Setup Development Environment

```bash
# Install with development dependencies
pip install -e ".[dev]"

# Run linting and formatting
black .
mypy --config-file mypy.ini .

# Clean temporary files
./cleanup.sh
```

## Requirements

- Python 3.8+
- Pydantic v2.12+

## License

Apache 2.0 - See LICENSE file for details

## Contributing

This package implements the official CAMARA common specification in Python. 

### For Python Implementation Issues
- Report bugs or request features: [GitHub Issues](https://github.com/VT-Cameron-Burger/CamaraCommon/issues)
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
- Package Repository: [CamaraCommon](https://github.com/VT-Cameron-Burger/CamaraCommon)