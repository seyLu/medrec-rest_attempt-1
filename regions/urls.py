from email.mime import base

from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from . import views

regions_router = DefaultRouter()
regions_router.register("regions", views.RegionListDetailViewSet, basename="regions")
provinces_nested_router = routers.NestedDefaultRouter(
    regions_router, "regions", lookup="region"
)
provinces_nested_router.register(
    r"provinces", views.ProvinceListViewSet, basename="provinces"
)

provinces_router = DefaultRouter()
provinces_router.register(
    "provinces", views.ProvinceListDetailViewSet, basename="provinces"
)
cities_nested_router = routers.NestedDefaultRouter(
    provinces_router, "provinces", lookup="province"
)
cities_nested_router.register(r"cities", views.CityListViewSet, basename="cities")

cities_router = DefaultRouter()
cities_router.register("cities", views.CityListDetailViewSet, basename="cities")
districts_nested_router = routers.NestedDefaultRouter(
    cities_router, "cities", lookup="city"
)
districts_nested_router.register(
    r"districts", views.DistrictListViewSet, basename="districts"
)

districts_router = DefaultRouter()
districts_router.register(
    "districts", views.DistrictListDetailViewSet, basename="districts"
)

urlpatterns = [
    path(r"", include(regions_router.urls)),
    path(r"", include(provinces_nested_router.urls)),
    path(r"", include(provinces_router.urls)),
    path(r"", include(cities_nested_router.urls)),
    path(r"", include(cities_router.urls)),
    path(r"", include(districts_nested_router.urls)),
    path(r"", include(districts_router.urls)),
]
