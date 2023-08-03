from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response

from .models import Client
from .serializers import ClientSerializer


class ClientListCreateAPIView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def list(self, request):
        serializer = self.get_serializer_class()(self.get_queryset(), many=True)
        return Response(serializer.data)


class ClientDetailAPIView(generics.RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    lookup_field = "reference_number"

    def retrieve(self, request, reference_number=None):
        client = get_object_or_404(
            self.get_queryset(), reference_number=reference_number
        )
        serializer = self.get_serializer_class()(client)
        return Response(serializer.data)
