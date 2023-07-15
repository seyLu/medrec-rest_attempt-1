from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from . import views

regions_router = DefaultRouter()
regions_router.register("", views.RegionListDetailViewSet, basename="")

provinces_router = routers.NestedDefaultRouter(regions_router, "", lookup="region")
provinces_router.register(
    r"provinces", views.ProvinceListDetailViewSet, basename="provinces"
)

cities_router = routers.NestedDefaultRouter(
    provinces_router, r"provinces", lookup="province"
)
cities_router.register(r"cities", views.CityListDetailViewSet, basename="cities")

districts_router = routers.NestedDefaultRouter(cities_router, r"cities", lookup="city")
districts_router.register(
    r"districts", views.DistrictListDetailViewSet, basename="districts"
)

urlpatterns = [
    path(r"", include(regions_router.urls)),
    path(r"", include(provinces_router.urls)),
    path(r"", include(cities_router.urls)),
    path(r"", include(districts_router.urls)),
]
