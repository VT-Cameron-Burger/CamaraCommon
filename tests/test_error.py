"""
Tests for Error data types.
"""

import pytest
from CamaraCommon.Error import (
    ErrorInfo,
    ErrorFactory,
    BadRequest,
    BadRequestCode,
    Unauthorized,
    Forbidden,
    NotFound,
    UnprocessableContent,
    InternalServerError,
    TooManyRequests,
    ServiceUnavailable,
)


class TestErrorInfo:
    """Test base ErrorInfo class."""

    def test_valid_error_info(self):
        """Test valid ErrorInfo creation."""
        error = ErrorInfo(status=400, code="INVALID_ARGUMENT", message="Test error")
        assert error.status == 400
        assert error.code == "INVALID_ARGUMENT"
        assert error.message == "Test error"

    def test_error_info_different_status_codes(self):
        """Test ErrorInfo with different HTTP status codes."""
        error_404 = ErrorInfo(
            status=404, code="NOT_FOUND", message="Resource not found"
        )
        assert error_404.status == 404

        error_500 = ErrorInfo(status=500, code="INTERNAL_ERROR", message="Server error")
        assert error_500.status == 500

    def test_error_info_with_long_message(self):
        """Test ErrorInfo with longer message."""
        long_message = "This is a very detailed error message that explains exactly what went wrong"
        error = ErrorInfo(status=422, code="VALIDATION_ERROR", message=long_message)
        assert error.message == long_message


class TestBadRequest:
    """Test BadRequest error class."""

    def test_bad_request_creation(self):
        """Test BadRequest creation with default status."""
        error = BadRequest(code="INVALID_ARGUMENT", message="Test error")
        assert error.status == 400
        assert error.code == "INVALID_ARGUMENT"
        assert error.message == "Test error"


class TestUnauthorized:
    """Test Unauthorized error class."""

    def test_unauthorized_creation(self):
        """Test Unauthorized creation with default status."""
        error = Unauthorized(code="UNAUTHENTICATED", message="Auth required")
        assert error.status == 401
        assert error.code == "UNAUTHENTICATED"
        assert error.message == "Auth required"


class TestErrorFactory:
    """Test ErrorFactory convenience methods."""

    def test_invalid_argument_factory(self):
        """Test creating INVALID_ARGUMENT error via factory."""
        error = ErrorFactory.invalid_argument()
        assert error.status == 400
        assert error.code == BadRequestCode.INVALID_ARGUMENT
        assert "invalid argument" in error.message.lower()

    def test_invalid_argument_factory_custom_message(self):
        """Test creating INVALID_ARGUMENT error with custom message."""
        custom_message = "Custom validation error"
        error = ErrorFactory.invalid_argument(custom_message)
        assert error.status == 400
        assert error.code == BadRequestCode.INVALID_ARGUMENT
        assert error.message == custom_message

    def test_unauthenticated_factory(self):
        """Test creating UNAUTHENTICATED error via factory."""
        error = ErrorFactory.unauthenticated()
        assert error.status == 401
        assert error.code == "UNAUTHENTICATED"
        assert "authentication" in error.message.lower()

    def test_permission_denied_factory(self):
        """Test creating PERMISSION_DENIED error via factory."""
        error = ErrorFactory.permission_denied()
        assert error.status == 403
        assert error.code == "PERMISSION_DENIED"
        assert "permission" in error.message.lower()

    def test_invalid_token_context_factory(self):
        """Test creating INVALID_TOKEN_CONTEXT error via factory."""
        field_name = "phoneNumber"
        error = ErrorFactory.invalid_token_context(field_name)
        assert error.status == 403
        assert error.code == "INVALID_TOKEN_CONTEXT"
        assert field_name in error.message

    def test_not_found_factory(self):
        """Test creating NOT_FOUND error via factory."""
        error = ErrorFactory.not_found()
        assert error.status == 404
        assert error.code == "NOT_FOUND"
        assert "not found" in error.message.lower()

    def test_identifier_not_found_factory(self):
        """Test creating IDENTIFIER_NOT_FOUND error via factory."""
        error = ErrorFactory.identifier_not_found()
        assert error.status == 404
        assert error.code == "IDENTIFIER_NOT_FOUND"
        assert "identifier" in error.message.lower()

    def test_service_not_applicable_factory(self):
        """Test creating SERVICE_NOT_APPLICABLE error via factory."""
        error = ErrorFactory.service_not_applicable()
        assert error.status == 422
        assert error.code == "SERVICE_NOT_APPLICABLE"
        assert "service" in error.message.lower()

    def test_missing_identifier_factory(self):
        """Test creating MISSING_IDENTIFIER error via factory."""
        error = ErrorFactory.missing_identifier()
        assert error.status == 422
        assert error.code == "MISSING_IDENTIFIER"
        assert "identified" in error.message.lower()

    def test_quota_exceeded_factory(self):
        """Test creating QUOTA_EXCEEDED error via factory."""
        error = ErrorFactory.quota_exceeded()
        assert error.status == 429
        assert error.code == "QUOTA_EXCEEDED"
        assert "quota" in error.message.lower()

    def test_internal_error_factory(self):
        """Test creating INTERNAL error via factory."""
        error = ErrorFactory.internal_error()
        assert error.status == 500
        assert error.code == "INTERNAL"
        assert "server error" in error.message.lower()

    def test_service_unavailable_factory(self):
        """Test creating UNAVAILABLE error via factory."""
        error = ErrorFactory.service_unavailable()
        assert error.status == 503
        assert error.code == "UNAVAILABLE"
        assert "unavailable" in error.message.lower()


class TestErrorEnums:
    """Test error code enums."""

    def test_bad_request_codes(self):
        """Test BadRequestCode enum values."""
        assert BadRequestCode.INVALID_ARGUMENT == "INVALID_ARGUMENT"
        assert BadRequestCode.OUT_OF_RANGE == "OUT_OF_RANGE"

    def test_enum_inheritance(self):
        """Test that error code enums inherit from str."""
        assert isinstance(BadRequestCode.INVALID_ARGUMENT, str)
        assert BadRequestCode.INVALID_ARGUMENT == "INVALID_ARGUMENT"
