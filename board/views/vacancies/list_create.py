from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from board.models import Vacancy
from board.serializers.vacancies.create import VacancyCreateInputSerializer
from board.serializers.vacancies.list import (
    VacancyListInputSerializer,
    VacancyListOutputSerializer,
)
from board.services.vacancies import create_vacancy, get_vacancies_page


class VacancyListCreateApi(APIView):

    def get_authenticators(self):
        if self.request.method == 'GET':
            return []
        return super().get_authenticators()

    def get_permissions(self):
        if self.request.method == 'GET':
            return []
        return super().get_permissions()

    def get(self, request: Request) -> Response:
        serializer = VacancyListInputSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        data: dict = serializer.validated_data

        take: int = data['take']
        skip: int = data['skip']
        statuses: list[Vacancy.Status] = data['statuses']
        types: list[Vacancy.Type] | None = data['types']
        salary_from: int | None = data['salary_from']
        salary_to: int | None = data['salary_to']
        salary_types: list[Vacancy.SalaryType] | None = data['salary_types']
        user_ids: list[int] | None = data['user_ids']

        vacancies_page = get_vacancies_page(
            take=take,
            skip=skip,
            statuses=statuses,
            types=types,
            salary_from=salary_from,
            salary_to=salary_to,
            salary_types=salary_types,
            user_ids=user_ids,
        )

        serializer = VacancyListOutputSerializer(vacancies_page)
        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = VacancyCreateInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data: dict = serializer.validated_data
        title: str = data['title']
        description: str = data['description']
        organization_id: int = data['organization_id']
        salary_from: int | None = data['salary_from']
        salary_to: int | None = data['salary_to']
        type: str = data['type']
        salary_type: str = data['salary_type']

        create_vacancy(
            user_id=request.user.id,
            title=title,
            description=description,
            organization_id=organization_id,
            salary_from=salary_from,
            salary_to=salary_to,
            type=type,
            salary_type=salary_type,
        )

        return Response(status=status.HTTP_201_CREATED)
