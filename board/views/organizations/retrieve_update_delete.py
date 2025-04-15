from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from board.exceptions import OrganizationNotFoundError
from board.models import Organization
from board.serializers.organizations.retrieve import OrganizationRetrieveOutputSerializer
from board.services.organizations import get_organization_details


class OrganizationRetrieveUpdateDeleteApi(APIView):

    def get_permissions(self):
        if self.request.method == 'GET':
            return []
        return super().get_permissions()

    def get(self, request: Request, organization_id: int) -> Response:
        organization = get_organization_details(organization_id)
        serializer = OrganizationRetrieveOutputSerializer(organization)
        return Response(serializer.data)

    def put(self, request: Request) -> Response:
        return Response()

    def delete(self, request: Request) -> Response:
        return Response()