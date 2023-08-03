from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import User
from .serializers import UserSerializer


class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request):
        serializer = self.get_serializer_class()(self.get_queryset(), many=True)
        return Response(serializer.data)


class UserDetailApiView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "uuid"

    def retrieve(self, request, uuid=None):
        user = get_object_or_404(self.get_queryset(), uuid=uuid)
        serializer = self.get_serializer_class()(user, many=True)
        return Response(serializer.data)
