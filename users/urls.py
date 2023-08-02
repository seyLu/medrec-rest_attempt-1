from django.urls import path

from . import views
from .models import User
from .serializers import UserSerializer

urlpatterns = [
    path(
        "users/",
        views.UserListCreateAPIView.as_view(
            queryset=User.objects.all(), serializer_class=UserSerializer
        ),
        name="user-list-create"
    )
]
