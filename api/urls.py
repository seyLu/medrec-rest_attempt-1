from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.api_home),
    path("", include("regions.urls")),
    path("", include("users.urls")),
]
