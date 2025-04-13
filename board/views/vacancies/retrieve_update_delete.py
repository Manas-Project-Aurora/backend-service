from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from board.models import Vacancy
from board.serializers.vacancies.list import (
    VacancyListInputSerializer,
    VacancyListOutputSerializer,
)


class VacancyRetrieveUpdateDeleteApi(APIView):

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

        vacancies = Vacancy.objects.select_related('organization').filter(
            status__in=statuses,
        ).order_by(
            '-created_at'
        )
        if types is not None:
            vacancies = vacancies.filter(type__in=types)
        if salary_from is not None:
            vacancies = vacancies.filter(salary_from__gte=salary_from)
        if salary_to is not None:
            vacancies = vacancies.filter(salary_to__lte=salary_to)
        if salary_types is not None:
            vacancies = vacancies.filter(salary_type__in=salary_types)

        total_count = vacancies.count()
        vacancies = vacancies[skip: skip + take]

        serializer = VacancyListOutputSerializer(
            {
                'vacancies': vacancies,
                'pagination': {
                    'total_count': total_count,
                    'take': take,
                    'skip': skip,
                }
            }
        )
        return Response(serializer.data)

    def put(self, request: Request) -> Response:
        return Response()

    def delete(self, request: Request) -> Response:
        return Response()
