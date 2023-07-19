from django.urls import include, path

from .routers.cities_router import cities_nested_router, cities_router
from .routers.districts_router import districts_router
from .routers.provinces_router import provinces_nested_router, provinces_router
from .routers.regions_router import regions_nested_router, regions_router

urlpatterns = [
    path(r"", include(regions_router.urls)),
    path(r"", include(regions_nested_router.urls)),
    path(r"", include(provinces_router.urls)),
    path(r"", include(provinces_nested_router.urls)),
    path(r"", include(cities_router.urls)),
    path(r"", include(cities_nested_router.urls)),
    path(r"", include(districts_router.urls)),
]
