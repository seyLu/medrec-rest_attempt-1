from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from .. import views

ROUTE_NAME = "regions"
ROUTE_LOOKUP = "region"

regions_router = DefaultRouter()
regions_router.register(ROUTE_NAME, views.RegionListDetailViewSet, basename=ROUTE_NAME)

regions_nested_router = routers.NestedDefaultRouter(
    regions_router, ROUTE_NAME, lookup=ROUTE_LOOKUP
)

regions_nested_router.register(
    r"provinces", views.ProvinceListViewSet, basename="provinces"
)
regions_nested_router.register(r"cities", views.CityListViewSet, basename="cities")
regions_nested_router.register(
    r"districts", views.DistrictListViewSet, basename="districts"
)
