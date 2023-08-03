from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from .models import City, District, Province, Region
from .serializers import (
    CitySerializer,
    DistrictSerializer,
    ProvinceSerializer,
    RegionSerializer,
)


class RegionListDetailViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    lookup_field = "code"

    def list(self, request):
        serializer = self.get_serializer_class()(self.get_queryset(), many=True)
        return Response(serializer.data)

    def retrieve(self, request, code=None):
        region = get_object_or_404(self.get_queryset(), code=code)
        serializer = self.get_serializer_class()(region)
        return Response(serializer.data)


class ProvinceListViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer
    lookup_field = "code"

    def list(self, request, region_code=None):
        qs = self.get_queryset().filter(region_code=region_code)
        serializer = self.get_serializer_class()(qs, many=True)
        return Response(serializer.data)


class ProvinceListDetailViewSet(ProvinceListViewSet):
    def list(self, request):
        serializer = self.get_serializer_class()(self.get_queryset(), many=True)
        return Response(serializer.data)

    def retrieve(self, request, code=None):
        province = get_object_or_404(self.get_queryset(), code=code)
        serializer = self.get_serializer_class()(province)
        return Response(serializer.data)


class CityListViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    lookup_field = "code"

    def list(self, request, province_code=None, region_code=None):
        parent_endpoint = request.get_full_path().split("/")[-4]

        if parent_endpoint == "regions":
            qs = self.get_queryset().filter(region_code=region_code)
        elif parent_endpoint == "provinces":
            qs = self.get_queryset().filter(province_code=province_code)

        serializer = self.get_serializer_class()(qs, many=True)
        return Response(serializer.data)


class CityListDetailViewSet(CityListViewSet):
    def list(self, request):
        serializer = self.get_serializer_class()(self.get_queryset(), many=True)
        return Response(serializer.data)

    def retrieve(self, request, code=None):
        city = get_object_or_404(self.get_queryset(), code=code)
        serializer = self.get_serializer_class()(city)
        return Response(serializer.data)


class DistrictListViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    lookup_field = "code"

    def list(self, request, city_code=None, province_code=None, region_code=None):
        parent_endpoint = request.get_full_path().split("/")[-4]

        if parent_endpoint == "regions":
            qs = self.get_queryset().filter(region_code=region_code)
        elif parent_endpoint == "provinces":
            qs = self.get_queryset().filter(province_code=province_code)
        elif parent_endpoint == "cities":
            qs = self.get_queryset().filter(city_code=city_code)

        serializer = self.get_serializer_class()(qs, many=True)
        return Response(serializer.data)


class DistrictListDetailViewSet(DistrictListViewSet):
    def list(self, request):
        serializer = self.get_serializer_class()(self.get_queryset(), many=True)
        return Response(serializer.data)

    def retrieve(self, request, code=None):
        district = get_object_or_404(self.get_queryset(), code=code)
        serializer = self.get_serializer_class()(district)
        return Response(serializer.data)
