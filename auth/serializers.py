from rest_framework import serializers
from rest_framework.exceptions import ValidationError

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

    def validate(self, attrs):
        unknown = set(self.initial_data) - set(self.fields)
        if unknown:
            raise ValidationError("Unknown field(s): {}".format(", ".join(unknown)))
        return attrs


class LogoutSerializer(serializers.ModelSerializer):
    pass
