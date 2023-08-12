from django.urls import path

from . import views

urlpatterns = [
    path("users/", views.UserListAPIView.as_view(), name="user-list"),
    path("users/<str:uuid>", views.UserDetailAPIView.as_view(), name="user-detail"),
]
