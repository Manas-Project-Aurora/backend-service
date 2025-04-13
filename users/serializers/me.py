from rest_framework import serializers


class UserOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    telegram_id = serializers.IntegerField(allow_null=True)
    email = serializers.EmailField()
    is_active = serializers.BooleanField()
    is_admin = serializers.BooleanField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
