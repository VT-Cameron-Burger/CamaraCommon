"""
Tests for communication data types (PhoneNumber, NetworkAccessIdentifier).
"""

import pytest

from CamaraCommon.Communication import NetworkAccessIdentifier, PhoneNumber


class TestPhoneNumber:
    """Test PhoneNumber validation."""

    def test_valid_phone_numbers(self):
        """Test valid phone number formats."""
        valid_numbers = [
            "+1234567890",
            "+12345678901",
            "+123456789012345",  # Max length 15 digits
            "+49123456789",
            "+86123456789012",
        ]

        for number in valid_numbers:
            phone = PhoneNumber(value=number)
            assert phone.value == number

    def test_invalid_phone_numbers(self):
        """Test invalid phone number formats."""
        invalid_numbers = [
            "1234567890",  # Missing +
            "+",  # Just plus sign
            "+0123456789",  # Cannot start with 0
            "+1234",  # Too short (less than 5 digits)
            "+1234567890123456",  # Too long (more than 15 digits)
            "+12345678ab",  # Contains letters
            "++1234567890",  # Double plus
            "+1234-567-890",  # Contains hyphens
            "+1 234 567 890",  # Contains spaces
        ]

        for number in invalid_numbers:
            with pytest.raises(ValueError):
                PhoneNumber(value=number)

    def test_phone_number_edge_cases(self):
        """Test edge cases for phone numbers."""
        # Minimum valid length (5 digits after +)
        min_phone = PhoneNumber(value="+12345")
        assert min_phone.value == "+12345"

        # Maximum valid length (15 digits after +)
        max_phone = PhoneNumber(value="+123456789012345")
        assert max_phone.value == "+123456789012345"


class TestNetworkAccessIdentifier:
    """Test NetworkAccessIdentifier validation."""

    def test_valid_network_access_identifiers(self):
        """Test valid NetworkAccessIdentifier formats."""
        valid_identifiers = [
            "user@example.com",
            "user.name@domain.org",
            "user123@test-domain.net",
            "simple@domain.co.uk",
            "test.user+tag@example-site.com",
        ]

        for identifier in valid_identifiers:
            nai = NetworkAccessIdentifier(value=identifier)
            assert nai.value == identifier

    def test_network_access_identifier_with_special_chars(self):
        """Test NetworkAccessIdentifier with special characters."""
        # Test with plus sign (common in email aliases)
        nai_plus = NetworkAccessIdentifier(value="user+alias@example.com")
        assert nai_plus.value == "user+alias@example.com"

        # Test with dots
        nai_dots = NetworkAccessIdentifier(value="first.last@sub.domain.com")
        assert nai_dots.value == "first.last@sub.domain.com"

    def test_network_access_identifier_formats(self):
        """Test NetworkAccessIdentifier with various formats (no strict validation)."""
        # NetworkAccessIdentifier doesn't have strict format validation
        # It accepts any string value
        identifiers = [
            "",  # Empty string is allowed
            "user",  # Missing @domain is allowed
            "@domain.com",  # Missing user part is allowed
            "user@",  # Missing domain part is allowed
            "user@domain.com",  # Standard format
            "user@@domain.com",  # Double @ is allowed
            "user@domain@com",  # Multiple @ is allowed
            "user name@domain.com",  # Space in user part is allowed
        ]

        for identifier in identifiers:
            nai = NetworkAccessIdentifier(value=identifier)
            assert nai.value == identifier
