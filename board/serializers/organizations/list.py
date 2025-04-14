from rest_framework import serializers

from board.models import OrganizationContact
from board.serializers.common import PaginationSerializer


class OrganizationContactSerializer(serializers.Serializer):
    type = serializers.ChoiceField(choices=OrganizationContact.Type.choices)
    value = serializers.CharField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()


class OrganizationListItemSerializer(serializers.Serializer):
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


class OrganizationListOutputSerializer(serializers.Serializer):
    organizations = OrganizationListItemSerializer(many=True)
    pagination = PaginationSerializer()


class OrganizationListInputSerializer(serializers.Serializer):
    take = serializers.IntegerField(default=50, min_value=1)
    skip = serializers.IntegerField(default=0, min_value=0)
