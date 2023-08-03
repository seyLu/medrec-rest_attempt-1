from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response

from .models import Record, RecordUpdateHistory
from .serializers import RecordSerializer, RecordUpdateHistorySerializer


class RecordListCreateAPIView(generics.ListCreateAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer

    def list(self, request):
        serializer = self.get_serializer_class()(self.get_queryset(), many=True)
        return Response(serializer.data)


class RecordDetailAPIView(generics.RetrieveAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    lookup_field = "client_reference_number"

    def retrieve(self, request, client_reference_number=None):
        client = get_object_or_404(
            self.get_queryset(), client_reference_number=client_reference_number
        )
        serializer = self.get_serializer()(client)
        return Response(serializer.data)


class RecordUpdateHistoryListAPIView(generics.ListAPIView):
    queryset = RecordUpdateHistory.objects.all()
    serializer_class = RecordUpdateHistorySerializer
    lookup_field = "uuid"

    def list(self, request, record_uuid=None):
        qs = self.get_queryset().filter(record_uuid=record_uuid)
        serializer = self.get_serializer_class()(qs, many=True)
        return Response(serializer.data)


class RecordUpdateHistoryDetailAPIView(generics.RetrieveAPIView):
    queryset = RecordUpdateHistory.objects.all()
    serializer_class = RecordUpdateHistorySerializer
    lookup_field = "uuid"

    def retrieve(self, request, uuid):
        record_update_history = get_object_or_404(self.get_queryset(), uuid=uuid)
        serializer = self.get_serializer_class()(record_update_history)
        return Response(serializer.data)
