from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from board.exceptions import OrganizationNotFoundError
from board.models import Organization
from board.serializers.organizations.retrieve import OrganizationRetrieveOutputSerializer


class OrganizationRetrieveUpdateDeleteApi(APIView):

    def get_permissions(self):
        if self.request.method == 'GET':
            return []
        return super().get_permissions()

    def get(self, request: Request, organization_id: int) -> Response:
        try:
            organization = Organization.objects.get(id=organization_id)
        except Organization.DoesNotExist:
            raise OrganizationNotFoundError

        serializer = OrganizationRetrieveOutputSerializer(organization)
        return Response(serializer.data)

    def put(self, request: Request) -> Response:
        return Response()

    def delete(self, request: Request) -> Response:
        return Response()