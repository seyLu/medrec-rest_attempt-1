from django.urls import path

from . import views

urlpatterns = [
    path(
        "province/", views.ProvinceListDetailView.as_view(), name="province-list-detail"
    ),
    path("city/", views.CityListDetailView.as_view(), name="city-list-detail"),
    path(
        "district/", views.DistrictListDetailView.as_view(), name="district-list-detail"
    ),
]
