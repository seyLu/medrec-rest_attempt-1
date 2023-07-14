# Generated by Django 4.2.3 on 2023-07-14 17:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("regions", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="city",
            name="province",
        ),
        migrations.RemoveField(
            model_name="district",
            name="city",
        ),
        migrations.AddField(
            model_name="city",
            name="province_code",
            field=models.ForeignKey(
                default="0831600000",
                on_delete=django.db.models.deletion.CASCADE,
                to="regions.province",
                to_field="code",
            ),
        ),
        migrations.AddField(
            model_name="district",
            name="city_code",
            field=models.ForeignKey(
                default="0831600000",
                on_delete=django.db.models.deletion.CASCADE,
                to="regions.province",
                to_field="code",
            ),
        ),
        migrations.AlterField(
            model_name="city",
            name="code",
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name="district",
            name="code",
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name="province",
            name="code",
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
