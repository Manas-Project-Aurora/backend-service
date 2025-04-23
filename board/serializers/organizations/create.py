from rest_framework import serializers


class OrganizationCreateInputSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=4096, required=False)
