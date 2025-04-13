from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from users.authentication import HttpOnlyRefreshTokenCookiesAuthentication
from users.serializers.me import UserOutputSerializer
from users.services.auth import login_user


class RefreshTokenApi(APIView):
    authentication_classes = [HttpOnlyRefreshTokenCookiesAuthentication]

    def post(self, request: Request, *args, **kwargs) -> Response:
        login_result = login_user(request.user)

        serializer = UserOutputSerializer(request.user)
        response = Response(serializer.data, status.HTTP_200_OK)
        response.set_cookie(
            key='refresh_token',
            value=login_result.refresh_token,
            httponly=True,
            secure=True,
            samesite='Strict',
            expires=login_result.refresh_token_expires,
        )
        response.set_cookie(
            key='access_token',
            value=login_result.access_token,
            httponly=True,
            secure=True,
            samesite='Strict',
            expires=login_result.access_token_expires,
        )
        return response
