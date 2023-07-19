from rest_framework import serializers

from .models import City, District, Province, Region


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = [
            "code",
            "name",
        ]


class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = [
            "code",
            "name",
            "region_code",
        ]


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = [
            "code",
            "name",
            "province_code",
            "region_code",
        ]


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = [
            "code",
            "name",
            "city_code",
            "province_code",
            "region_code",
        ]
