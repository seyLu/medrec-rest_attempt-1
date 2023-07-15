from rest_framework import serializers

from .models import City, District, Province, Region


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = [
            "name",
            "code",
        ]


class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = [
            "region_code",
            "name",
            "code",
        ]


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = [
            "province_code",
            "name",
            "code",
        ]


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = [
            "city_code",
            "name",
            "code",
        ]
