from rest_framework import serializers

from .models import Client


class ClientSerializer(serializers.Serializer):
    full_address = serializers.SerializerMethodField()

    class Meta:
        model = Client
        fields = [
            "reference_number",
            "type",
            "level",
            "created_datetime",
            "updated_datetime",
            "first_name",
            "last_name",
            "age",
            "school",
            "full_address",
        ]

    def get_full_address(self, obj):
        return f"{self.street_address}, {self.district}, {self.city}, {self.province}"
