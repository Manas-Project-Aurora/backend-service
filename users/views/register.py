from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers.register import UserRegisterInputSerializer


User = get_user_model()


class UserRegisterApi(APIView):

    def post(self, request: Request) -> Response:
        serializer = UserRegisterInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data: dict = serializer.validated_data

        username: str = data['username']
        password: str = data['password']

        User.objects.create_user(username=username, password=password)

        return Response(status=status.HTTP_201_CREATED)
