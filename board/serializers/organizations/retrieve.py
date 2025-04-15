from rest_framework import serializers
from board.serializers.organizations.list import OrganizationContactSerializer
from board.services.organizations import get_organization_details


class OrganizationRetrieveOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField(allow_null=True)
    logo_url = serializers.URLField(allow_null=True)
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    contacts = OrganizationContactSerializer(many=True)
    vacancy_count = serializers.IntegerField()
    event_count = serializers.IntegerField()
    video_count = serializers.IntegerField()
