from rest_framework import generics
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer


class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request):
        qs = self.get_queryset()
        serializer = self.get_serializer_class()(qs, many=True)
        return Response(serializer.data)
