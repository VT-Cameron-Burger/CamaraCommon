"""Error data types for CAMARA APIs."""

from .ErrorInfo import ErrorInfo as ErrorInfo
from .BadRequest import BadRequest as BadRequest, BadRequestCode as BadRequestCode
from .Unauthorized import (
    Unauthorized as Unauthorized,
    UnauthorizedCode as UnauthorizedCode,
)
from .Forbidden import Forbidden as Forbidden, ForbiddenCode as ForbiddenCode
from .NotFound import NotFound as NotFound, NotFoundCode as NotFoundCode
from .UnprocessableContent import (
    UnprocessableContent as UnprocessableContent,
    UnprocessableContentCode as UnprocessableContentCode,
)
from .InternalServerError import (
    InternalServerError as InternalServerError,
    InternalServerErrorCode as InternalServerErrorCode,
)
from .TooManyRequests import (
    TooManyRequests as TooManyRequests,
    TooManyRequestsCode as TooManyRequestsCode,
)
from .ServiceUnavailable import (
    ServiceUnavailable as ServiceUnavailable,
    ServiceUnavailableCode as ServiceUnavailableCode,
)
from .ErrorFactory import ErrorFactory as ErrorFactory
