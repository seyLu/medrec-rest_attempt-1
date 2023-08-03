from rest_framework import serializers

from .models import Record, RecordUpdateHistory


class RecordSerializer(serializers.Serializer):
    class Meta:
        model = Record
        fields = [
            "uuid",
            "created_datetime",
            "updated_datetime",
            "client_reference_number",
            "history",
            "diagnosis_and_plan",
            "remarks",
            "is_seen_by_staff",
        ]


class RecordUpdateHistorySerializer(serializers.Serializer):
    class Meta:
        model = RecordUpdateHistory
        fields = [
            "uuid",
            "record",
            "updated_by",
            "updated_datetime",
            "remarks",
        ]
