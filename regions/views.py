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
    queryset = Region.objects.filter()
    serializer_class = RegionSerializer

    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        region = get_object_or_404(self.queryset, code=pk)
        serializer = self.serializer_class(region)
        return Response(serializer.data)


class ProvinceListViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer

    def list(self, request, region_pk=None):
        qs = self.queryset.filter(region_code=region_pk)
        serializer = self.serializer_class(qs, many=True)
        return Response(serializer.data)


class ProvinceListDetailViewSet(ProvinceListViewSet):
    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        qs = self.queryset.filter(code=pk)
        province = get_object_or_404(qs, code=pk)
        serializer = self.serializer_class(province)
        return Response(serializer.data)


class CityListViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    def list(self, request, province_pk=None):
        qs = City.objects.filter(province_code=province_pk)
        serializer = self.serializer_class(qs, many=True)
        return Response(serializer.data)


class CityListDetailViewSet(CityListViewSet):
    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        qs = self.queryset.filter(code=pk)
        city = get_object_or_404(qs, code=pk)
        serializer = self.serializer_class(city)
        return Response(serializer.data)


class DistrictListViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer

    def list(self, request, city_pk=None):
        qs = self.queryset.filter(city_code=city_pk)
        serializer = self.serializer_class(qs, many=True)
        return Response(serializer.data)


class DistrictListDetailViewSet(DistrictListViewSet):
    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        qs = self.queryset.filter(code=pk)
        district = get_object_or_404(qs, code=pk)
        serializer = self.serializer_class(district)
        return Response(serializer.data)