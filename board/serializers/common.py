from rest_framework import serializers


class PaginationSerializer(serializers.Serializer):
    taken_count = serializers.IntegerField()
    skipped_count = serializers.IntegerField()
    total_count = serializers.IntegerField()
