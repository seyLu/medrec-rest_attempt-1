import uuid

from django.db import models

from clients.models import Client
from users.models import User


class Record(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    client_reference_number = models.ForeignKey(
        Client, to_field="reference_number", on_delete=models.CASCADE
    )
    history = models.TextField()
    diagnosis_and_plan = models.TextField()
    remarks = models.TextField(blank=True)

    is_seen_by_staff = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        record_update_history = RecordUpdateHistory(
            record=self.uuid,
            updated_by=self.context.get("request").user,
            remarks=self.remarks,
        )
        record_update_history.save()

        super().save(*args, **kwargs)


class RecordUpdateHistory(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    record = models.ForeignKey(Record, to_field="uuid", on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, to_field="uuid", on_delete=models.CASCADE)
    updated_datetime = models.DateTimeField(auto_now=True)
    remarks = models.TextField(blank=True)
