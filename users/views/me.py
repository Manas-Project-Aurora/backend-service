from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers.me import UserOutputSerializer


class UserApi(APIView):

    def get(self, request: Request) -> Response:
        serializer = UserOutputSerializer(request.user)
        return Response(serializer.data)
