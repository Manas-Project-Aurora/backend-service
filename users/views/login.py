from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from users.exceptions import UserNotFoundError
from users.serializers.login import LoginInputSerializer
from users.serializers.me import UserOutputSerializer
from users.services.auth import login_user


class UserLoginApi(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request: Request) -> Response:
        serializer = LoginInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data: dict = serializer.validated_data

        email: str = data['email']
        password: str = data['password']

        user = authenticate(email=email, password=password)
        if not user:
            raise UserNotFoundError
        login_result = login_user(user)

        serializer = UserOutputSerializer(user)
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
