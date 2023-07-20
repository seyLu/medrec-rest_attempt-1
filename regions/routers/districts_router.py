from rest_framework.routers import DefaultRouter

from .. import views

ROUTE_NAME = "districts"
ROUTE_LOOKUP = "district"

districts_router = DefaultRouter()
districts_router.register(
    ROUTE_NAME, views.DistrictListDetailViewSet, basename=f"{ROUTE_NAME}-list-detail"
)
