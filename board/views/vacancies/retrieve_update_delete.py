from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from board.exceptions import VacancyNotFoundError
from board.models import Vacancy
from board.serializers.vacancies.retrieve import VacancyRetrieveOutputSerializer
from board.services.vacancies import delete_vacancy


class VacancyRetrieveUpdateDeleteApi(APIView):

    def get_permissions(self):
        if self.request.method == 'GET':
            return []
        return super().get_permissions()

    def get(self, request: Request, vacancy_id: int) -> Response:
        try:
            vacancy = Vacancy.objects.select_related('organization').get(id=vacancy_id)
        except Vacancy.DoesNotExist:
            raise VacancyNotFoundError
        serializer = VacancyRetrieveOutputSerializer(vacancy)
        return Response(serializer.data)

    def put(self, request: Request) -> Response:
        return Response()

    def delete(self, request: Request, vacancy_id: int) -> Response:
        delete_vacancy(vacancy_id, request.user.id)
        return Response(status=status.HTTP_204_NO_CONTENT)