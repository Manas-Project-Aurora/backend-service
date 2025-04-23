from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from board.services.vacancies import reject_vacancy


class VacancyRejectApi(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request: Request, vacancy_id: int) -> Response:
        reject_vacancy(vacancy_id, request.user)
        return Response(status=status.HTTP_204_NO_CONTENT)