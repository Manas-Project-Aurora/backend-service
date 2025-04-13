from typing import Any

from drf_standardized_errors.formatter import (
    ExceptionFormatter as BaseExceptionFormatter,
)
from drf_standardized_errors.types import ErrorResponse
from rest_framework import status
from rest_framework.exceptions import APIException


class ExceptionFormatter(BaseExceptionFormatter):

    def format_error_response(self, error_response: ErrorResponse) -> Any:
        extra: dict | None = getattr(self.exc, 'extra', None)

        error_response = super().format_error_response(error_response)
        for error in error_response['errors']:
            if extra is not None and error['code'] == self.exc.default_code:
                error['extra'] = extra
            if error['attr'] is None:
                del error['attr']

        return error_response


class UserAlreadyExistsError(APIException):
    status_code = status.HTTP_409_CONFLICT
    default_code = "user_already_exists"
    default_detail = "User already exists."


class UserNotFoundError(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_code = "user_not_found"
    default_detail = "User not found."
