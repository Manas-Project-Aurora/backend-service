from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from board.services.vacancies import approve_vacancy


class VacancyApproveApi(APIView):
    def post(self, request: Request, vacancy_id: int) -> Response:
        approve_vacancy(vacancy_id, request.user)
        return Response(status=status.HTTP_204_NO_CONTENT)