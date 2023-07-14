from rest_framework import viewsets

from .models import City, District, Province
from .serializers import CitySerializer, DistrictSerializer, ProvinceSerializer


class ProvinceListDetailView(viewsets.ReadOnlyModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer

    def list(self, request):
        pass

    def retrieve(self, request, code=None):
        pass


class CityListDetailView(viewsets.ReadOnlyModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    def list(self, request):
        pass

    def retrieve(self, request, code=None):
        pass


class DistrictListDetailView(viewsets.ReadOnlyModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer

    def list(self, request):
        pass

    def retrieve(self, request, code=None):
        pass
