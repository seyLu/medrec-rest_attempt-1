from django.urls import path

from . import views

urlpatterns = [
    path("regions/", views.regions_view, name="demo-regions"),
    path("auth/login/", views.login_view, name="demo-login"),
]
