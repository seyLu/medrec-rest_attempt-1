from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from .. import views

ROUTE_NAME = "provinces"
ROUTE_LOOKUP = "province"

provinces_router = DefaultRouter()
provinces_router.register(
    ROUTE_NAME, views.ProvinceListDetailViewSet, basename=ROUTE_NAME
)

provinces_nested_router = routers.NestedDefaultRouter(
    provinces_router, ROUTE_NAME, lookup=ROUTE_LOOKUP
)

provinces_nested_router.register(r"cities", views.CityListViewSet, basename="cities")
provinces_nested_router.register(
    r"districts", views.DistrictListViewSet, basename="districts"
)
