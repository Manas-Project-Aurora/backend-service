from django.db import IntegrityError
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from users.exceptions import UserAlreadyExistsError
from users.serializers.me import UserOutputSerializer
from users.serializers.register import UserRegisterInputSerializer

from users.models import default_username, User
from users.services.auth import login_user


class UserRegisterApi(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request: Request) -> Response:
        serializer = UserRegisterInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data: dict = serializer.validated_data

        email: str = data['email']
        password: str = data['password']

        try:
            user = User.objects.create_user(
                username=default_username(),
                email=email,
                password=password
            )
        except IntegrityError:
            raise UserAlreadyExistsError

        login_result = login_user(user)

        serializer = UserOutputSerializer(user)
        response = Response(serializer.data, status.HTTP_201_CREATED)
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
