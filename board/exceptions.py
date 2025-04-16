from rest_framework import status
from rest_framework.exceptions import APIException


class VacancyNotFoundError(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_code = "vacancy_not_found"
    default_detail = "Vacancy not found."

class OrganizationNotFoundError(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_code = "organization_not_found"
    default_detail = "Organization not found."

class VacancyAccessDenied(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_code = "vacancy_access_denied"
    default_detail = "Vacancy access denied."

class OrganizationAccessDenied(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_code = "organization_access_denied"
    default_detail = "Organization access denied."