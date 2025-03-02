from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView


class OrganizationListCreateApi(APIView):

    def get(self, request: Request) -> Response:
        return Response()

    def post(self, request: Request) -> Response:
        return Response()
