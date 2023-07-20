from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from .. import views

ROUTE_NAME = "cities"
ROUTE_LOOKUP = "city"

cities_router = DefaultRouter()
cities_router.register(
    ROUTE_NAME, views.CityListDetailViewSet, basename=f"{ROUTE_NAME}-list-detail"
)

cities_nested_router = routers.NestedDefaultRouter(
    cities_router, ROUTE_NAME, lookup=ROUTE_LOOKUP
)

cities_nested_router.register(
    r"districts", views.DistrictListViewSet, basename="districts-list"
)
