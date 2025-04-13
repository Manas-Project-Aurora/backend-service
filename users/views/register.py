from django.db import IntegrityError
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from users.exceptions import UserAlreadyExistsError
from users.serializers.register import UserRegisterInputSerializer

from users.models import default_username, User


class UserRegisterApi(APIView):

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

        return Response(status=status.HTTP_201_CREATED)
