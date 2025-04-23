from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from board.serializers.organizations.create import \
    OrganizationCreateInputSerializer
from board.serializers.organizations.list import (
    OrganizationListInputSerializer, OrganizationListOutputSerializer,
)
from board.services.organizations import (
    create_organization,
    get_organizations_page,
)


class OrganizationListCreateApi(APIView):

    def get_authenticators(self):
        if self.request.method == 'GET':
            return []
        return super().get_authenticators()

    def get_permissions(self):
        if self.request.method == 'GET':
            return []
        return super().get_permissions()

    def get(self, request: Request) -> Response:
        serializer = OrganizationListInputSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        data: dict = serializer.validated_data

        take: int = data['take']
        skip: int = data['skip']

        organizations_page = get_organizations_page(take=take, skip=skip)

        serializer = OrganizationListOutputSerializer(organizations_page)
        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = OrganizationCreateInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data: dict = serializer.validated_data

        name: str = data['name']
        description: str | None = data['description']

        create_organization(name=name, description=description)

        return Response(status=status.HTTP_201_CREATED)
