from rest_framework import serializers


class UserRegisterInputSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
