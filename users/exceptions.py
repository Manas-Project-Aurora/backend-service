from rest_framework.exceptions import APIException
from rest_framework import status


class UserAlreadyExistsError(APIException):
    status_code = status.HTTP_409_CONFLICT
    default_code = "user_already_exists"
    default_detail = "User already exists."
