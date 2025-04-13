from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView


class UserLogoutApi(APIView):

    def post(self, request: Request) -> Response:
        response = Response(status=status.HTTP_205_RESET_CONTENT)
        response.delete_cookie(key='refresh_token')
        response.delete_cookie(key='access_token')
        return response
