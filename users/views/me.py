from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from users.authentication import HttpOnlyCookiesAuthentication
from users.serializers.login import LoginInputSerializer
from users.services.auth import login_user


class UserApi(APIView):

    def get(self, request: Request) -> Response:
        print(request.user)
        response = Response(status=status.HTTP_200_OK)
        return response
