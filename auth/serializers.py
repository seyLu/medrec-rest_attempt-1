from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from users.models import User


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    re_password = serializers.CharField()

    class Meta:
        model = User
        fields = [
            "email",
            "password",
            "re_password",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, attrs):
        unknown = set(self.initial_data) - set(self.fields)
        if unknown:
            raise ValidationError("Unknown field(s): {}".format(", ".join(unknown)))

        if attrs["password"] != attrs["re_password"]:
            raise ValidationError({"message": "Password does not match."})

        return attrs

    def create(self, validated_data):
        return User.objects.create_user(
            validated_data["email"],
            validated_data["password"],
        )


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
