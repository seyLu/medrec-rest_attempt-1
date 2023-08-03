from django.db import models
from django.utils.translation import gettext_lazy as _

from regions.models import City, District, Province, Region


class Client(models.Model):
    class ClientType(models.TextChoices):
        TEACHER = "TCH", _("Teacher")
        NONTEACHING_PERSONNEL = "NTP", _("Non-teaching Personnel")
        STUDENT = "STU", _("Student")

    reference_number = models.IntegerField(max_length=12)
    type = models.CharField(
        max_length=3,
        choices=ClientType.choices,
        default=ClientType.STUDENT,
    )
    level = models.CharField(max_length=32)  # grade_level if student, else position

    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    age = models.IntegerField(max_length=3)
    school = models.CharField(max_length=255)

    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=255)
