from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from board.serializers.organizations.retrieve import OrganizationRetrieveOutputSerializer
from board.services.organizations import get_organization_details, delete_organization


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

    def delete(self, request: Request, organization_id: int) -> Response:
        delete_organization(organization_id, request.user)
        return Response(status=status.HTTP_204_NO_CONTENT)