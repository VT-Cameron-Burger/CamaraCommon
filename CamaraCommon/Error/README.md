# Error Directory

This directory contains CAMARA-compliant error response classes based on the `CAMARA_common.yaml` specification.

## Structure

- **`ErrorInfo.py`** - Base error information class
- **HTTP Error Classes** - Specific error response classes for common HTTP status codes:
  - `BadRequest.py` (400)
  - `Unauthorized.py` (401) 
  - `Forbidden.py` (403)
  - `NotFound.py` (404)
  - `UnprocessableContent.py` (422)
  - `TooManyRequests.py` (429)
  - `InternalServerError.py` (500)
  - `ServiceUnavailable.py` (503)
- **`ErrorFactory.py`** - Factory class for convenient error creation
- **`__init__.py`** - Module exports

## Usage

### Basic Usage

```python
from Error import ErrorInfo, BadRequest, ErrorFactory

# Direct instantiation
error = BadRequest(code="INVALID_ARGUMENT", message="Invalid phone number format")

# Using the factory (recommended)
error = ErrorFactory.invalid_argument("Invalid phone number format")
```

### Error Factory Methods

The `ErrorFactory` class provides convenient methods for creating standardized errors:

```python
from Error import ErrorFactory

# 400 errors
error = ErrorFactory.invalid_argument("Custom message")
error = ErrorFactory.out_of_range("Value must be between 1-100")

# 401 errors  
error = ErrorFactory.unauthenticated()

# 403 errors
error = ErrorFactory.permission_denied()
error = ErrorFactory.invalid_token_context("phoneNumber")

# 404 errors
error = ErrorFactory.not_found("User not found")
error = ErrorFactory.identifier_not_found()

# 422 errors
error = ErrorFactory.service_not_applicable()
error = ErrorFactory.missing_identifier()
error = ErrorFactory.unsupported_identifier()
error = ErrorFactory.unnecessary_identifier()

# 429 errors
error = ErrorFactory.quota_exceeded()
error = ErrorFactory.too_many_requests()

# 500 errors
error = ErrorFactory.internal_error()

# 503 errors
error = ErrorFactory.service_unavailable()
```

### Error Codes

Each error class includes an enum with the valid error codes:

```python
from Error import BadRequestCode, UnauthorizedCode

# Available codes
print(BadRequestCode.INVALID_ARGUMENT)  # "INVALID_ARGUMENT"
print(BadRequestCode.OUT_OF_RANGE)      # "OUT_OF_RANGE"
```

## CAMARA Compliance

All error classes follow the CAMARA common.yaml specification:

- Standard HTTP status codes
- Predefined error codes
- Consistent message formats
- JSON schema examples
- Proper inheritance from `ErrorInfo`

## Testing

Run tests with:

```bash
python -m pytest tests/test_error.py -v
```