from rest_framework import serializers


class CommunityResourceSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    group_id = serializers.IntegerField()
    group_name = serializers.CharField()
    url = serializers.URLField()
    color = serializers.CharField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
