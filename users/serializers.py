from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "uuid",
            "email",
            "mobile_number",
            "is_email_verified",
            "is_mobile_verified",
            "is_active",
            "is_staff",
        ]
