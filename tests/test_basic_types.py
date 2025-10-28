"""
Tests for basic data types (XCorrelator, TimePeriod, ErrorInfo).
"""

import pytest
from datetime import datetime, timezone

from CommonDataTypes.basic import XCorrelator, TimePeriod, ErrorInfo


class TestXCorrelator:
    """Test XCorrelator validation."""

    def test_valid_xcorrelator(self):
        """Test valid XCorrelator values."""
        correlator = XCorrelator(value="test-correlation-id-123")
        assert correlator.value == "test-correlation-id-123"

    def test_xcorrelator_with_uuid(self):
        """Test XCorrelator with UUID format."""
        uuid_value = "550e8400-e29b-41d4-a716-446655440000"
        correlator = XCorrelator(value=uuid_value)
        assert correlator.value == uuid_value

    def test_valid_xcorrelator_empty(self):
        """Test that empty XCorrelator is valid (pattern allows 0 length)."""
        correlator = XCorrelator(value="")
        assert correlator.value == ""

    def test_invalid_xcorrelator_too_long(self):
        """Test invalid XCorrelator that's too long."""
        long_value = "a" * 257  # Max length is 256
        with pytest.raises(ValueError):
            XCorrelator(value=long_value)


class TestTimePeriod:
    """Test TimePeriod validation."""

    def test_valid_time_period(self):
        """Test valid TimePeriod with start and end dates."""
        start = datetime.now(timezone.utc)
        end = datetime.now(timezone.utc)
        time_period = TimePeriod(startDate=start, endDate=end)
        assert time_period.startDate == start
        assert time_period.endDate == end

    def test_time_period_start_only(self):
        """Test TimePeriod with only start date."""
        start = datetime.now(timezone.utc)
        time_period = TimePeriod(startDate=start)
        assert time_period.startDate == start
        assert time_period.endDate is None

    def test_time_period_with_timezone(self):
        """Test TimePeriod with timezone-aware datetime."""
        start = datetime(2023, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
        end = datetime(2023, 1, 2, 12, 0, 0, tzinfo=timezone.utc)
        time_period = TimePeriod(startDate=start, endDate=end)
        assert time_period.startDate.tzinfo is not None
        if time_period.endDate is not None:
            assert time_period.endDate.tzinfo is not None


class TestErrorInfo:
    """Test ErrorInfo validation."""

    def test_valid_error_info(self):
        """Test valid ErrorInfo."""
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
