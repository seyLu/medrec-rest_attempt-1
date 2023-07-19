from django.urls import include, path

from .routers import (
    cities_nested_router,
    cities_router,
    districts_router,
    provinces_nested_router,
    provinces_router,
    regions_nested_router,
    regions_router,
)

urlpatterns = [
    path(r"", include(regions_router.urls)),
    path(r"", include(regions_nested_router.urls)),
    path(r"", include(provinces_router.urls)),
    path(r"", include(provinces_nested_router.urls)),
    path(r"", include(cities_router.urls)),
    path(r"", include(cities_nested_router.urls)),
    path(r"", include(districts_router.urls)),
]
