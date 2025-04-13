from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from community.serializers import CommunityResourceSerializer
from community.services import get_community_resources


class CommunityResourceListApi(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request: Request) -> Response:
        resources = get_community_resources()
        serializer = CommunityResourceSerializer(resources, many=True)
        return Response({'community_resources': serializer.data})
