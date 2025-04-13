from rest_framework import serializers


class UserRegisterInputSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
