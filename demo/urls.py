from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path("regions/", views.regions_view, name="demo-regions")
]
