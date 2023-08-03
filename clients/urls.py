from django.urls import path

from . import views

urlpatterns = [
    path(
        "clients/", views.ClientListCreateAPIView.as_view(), name="client-list-create"
    ),
    path(
        "clients/<int:reference_number>",
        views.ClientDetailAPIView.as_view(),
        name="client-detail",
    ),
]
