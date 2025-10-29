"""
Tests for basic data types (XCorrelator, TimePeriod).
"""

import pytest
from datetime import datetime, timezone

from Basic import XCorrelator, TimePeriod


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
        time_period = TimePeriod(startDate=start)  # type: ignore
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
