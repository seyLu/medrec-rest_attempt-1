from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"Region(name={self.name}, code={self.code})"


class Province(models.Model):
    region_code = models.ForeignKey(
        Region, to_field="code", on_delete=models.CASCADE, default="0800000000"
    )
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"Province(name={self.name}, code={self.code})"


class City(models.Model):
    province_code = models.ForeignKey(
        Province, to_field="code", on_delete=models.CASCADE, default="0831600000"
    )
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"City(name={self.name}, code={self.code})"


class District(models.Model):
    city_code = models.ForeignKey(
        Province, to_field="code", on_delete=models.CASCADE, default="0831600000"
    )
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"District(name={self.name}, code={self.code})"
