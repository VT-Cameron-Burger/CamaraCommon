"""Error factory for creating standardized CAMARA error responses."""

from .BadRequest import BadRequest, BadRequestCode
from .ErrorInfo import ErrorInfo
from .Forbidden import Forbidden, ForbiddenCode
from .InternalServerError import InternalServerError, InternalServerErrorCode
from .NotFound import NotFound, NotFoundCode
from .ServiceUnavailable import ServiceUnavailable, ServiceUnavailableCode
from .TooManyRequests import TooManyRequests, TooManyRequestsCode
from .Unauthorized import Unauthorized, UnauthorizedCode
from .UnprocessableContent import (UnprocessableContent,
                                   UnprocessableContentCode)


class ErrorFactory:
    """
    Factory class for creating standardized CAMARA error responses.

    Provides convenient methods to create common error responses
    based on CAMARA common.yaml specifications.
    """

    @staticmethod
    def invalid_argument(
        message: str = "Client specified an invalid argument, request body or query param.",
    ) -> BadRequest:
        """Create an INVALID_ARGUMENT (400) error."""
        return BadRequest(
            status=400, code=BadRequestCode.INVALID_ARGUMENT, message=message
        )

    @staticmethod
    def out_of_range(message: str = "Client specified an invalid range.") -> BadRequest:
        """Create an OUT_OF_RANGE (400) error."""
        return BadRequest(status=400, code=BadRequestCode.OUT_OF_RANGE, message=message)

    @staticmethod
    def unauthenticated(
        message: str = "Request not authenticated due to missing, invalid, or expired credentials. A new authentication is required.",
    ) -> Unauthorized:
        """Create an UNAUTHENTICATED (401) error."""
        return Unauthorized(
            status=401, code=UnauthorizedCode.UNAUTHENTICATED, message=message
        )

    @staticmethod
    def permission_denied(
        message: str = "Client does not have sufficient permissions to perform this action.",
    ) -> Forbidden:
        """Create a PERMISSION_DENIED (403) error."""
        return Forbidden(
            status=403, code=ForbiddenCode.PERMISSION_DENIED, message=message
        )

    @staticmethod
    def invalid_token_context(field: str) -> Forbidden:
        """Create an INVALID_TOKEN_CONTEXT (403) error."""
        return Forbidden(
            status=403,
            code=ForbiddenCode.INVALID_TOKEN_CONTEXT,
            message=f"{field} is not consistent with access token.",
        )

    @staticmethod
    def not_found(message: str = "The specified resource is not found.") -> NotFound:
        """Create a NOT_FOUND (404) error."""
        return NotFound(status=404, code=NotFoundCode.NOT_FOUND, message=message)

    @staticmethod
    def identifier_not_found(message: str = "Device identifier not found.") -> NotFound:
        """Create an IDENTIFIER_NOT_FOUND (404) error."""
        return NotFound(
            status=404, code=NotFoundCode.IDENTIFIER_NOT_FOUND, message=message
        )

    @staticmethod
    def service_not_applicable(
        message: str = "The service is not available for the provided identifier.",
    ) -> UnprocessableContent:
        """Create a SERVICE_NOT_APPLICABLE (422) error."""
        return UnprocessableContent(
            status=422,
            code=UnprocessableContentCode.SERVICE_NOT_APPLICABLE,
            message=message,
        )

    @staticmethod
    def missing_identifier(
        message: str = "The device cannot be identified.",
    ) -> UnprocessableContent:
        """Create a MISSING_IDENTIFIER (422) error."""
        return UnprocessableContent(
            status=422,
            code=UnprocessableContentCode.MISSING_IDENTIFIER,
            message=message,
        )

    @staticmethod
    def unsupported_identifier(
        message: str = "The identifier provided is not supported.",
    ) -> UnprocessableContent:
        """Create an UNSUPPORTED_IDENTIFIER (422) error."""
        return UnprocessableContent(
            status=422,
            code=UnprocessableContentCode.UNSUPPORTED_IDENTIFIER,
            message=message,
        )

    @staticmethod
    def unnecessary_identifier(
        message: str = "The device is already identified by the access token.",
    ) -> UnprocessableContent:
        """Create an UNNECESSARY_IDENTIFIER (422) error."""
        return UnprocessableContent(
            status=422,
            code=UnprocessableContentCode.UNNECESSARY_IDENTIFIER,
            message=message,
        )

    @staticmethod
    def quota_exceeded(message: str = "Out of resource quota.") -> TooManyRequests:
        """Create a QUOTA_EXCEEDED (429) error."""
        return TooManyRequests(
            status=429, code=TooManyRequestsCode.QUOTA_EXCEEDED, message=message
        )

    @staticmethod
    def too_many_requests(message: str = "Rate limit reached.") -> TooManyRequests:
        """Create a TOO_MANY_REQUESTS (429) error."""
        return TooManyRequests(
            status=429, code=TooManyRequestsCode.TOO_MANY_REQUESTS, message=message
        )

    @staticmethod
    def internal_error(
        message: str = "Unknown server error.",
    ) -> InternalServerError:
        """Create an INTERNAL (500) error."""
        return InternalServerError(
            status=500, code=InternalServerErrorCode.INTERNAL, message=message
        )

    @staticmethod
    def service_unavailable(
        message: str = "Service Unavailable.",
    ) -> ServiceUnavailable:
        """Create an UNAVAILABLE (503) error."""
        return ServiceUnavailable(
            status=503, code=ServiceUnavailableCode.UNAVAILABLE, message=message
        )
