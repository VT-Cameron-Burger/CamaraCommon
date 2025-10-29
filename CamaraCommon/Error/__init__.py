"""Error data types for CAMARA APIs."""

from .BadRequest import BadRequest as BadRequest
from .BadRequest import BadRequestCode as BadRequestCode
from .ErrorFactory import ErrorFactory as ErrorFactory
from .ErrorInfo import ErrorInfo as ErrorInfo
from .Forbidden import Forbidden as Forbidden
from .Forbidden import ForbiddenCode as ForbiddenCode
from .InternalServerError import InternalServerError as InternalServerError
from .InternalServerError import \
    InternalServerErrorCode as InternalServerErrorCode
from .NotFound import NotFound as NotFound
from .NotFound import NotFoundCode as NotFoundCode
from .ServiceUnavailable import ServiceUnavailable as ServiceUnavailable
from .ServiceUnavailable import \
    ServiceUnavailableCode as ServiceUnavailableCode
from .TooManyRequests import TooManyRequests as TooManyRequests
from .TooManyRequests import TooManyRequestsCode as TooManyRequestsCode
from .Unauthorized import Unauthorized as Unauthorized
from .Unauthorized import UnauthorizedCode as UnauthorizedCode
from .UnprocessableContent import UnprocessableContent as UnprocessableContent
from .UnprocessableContent import \
    UnprocessableContentCode as UnprocessableContentCode
