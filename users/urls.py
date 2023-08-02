from django.urls import path

from . import views

urlpatterns = [
    path("users/", views.UserListCreateAPIView.as_view(), name="user-list-create"),
]
