from rest_framework import serializers

from users.models import User


class RegisterSerializer(serializers.ModelSerializer):
    pass


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = [
            "email",
            "password",
        ]
        extra_kwargs = {"password": {"write_only": True}}
