from django.urls import path

from . import views

urlpatterns = [
    path(
        "records/", views.RecordListCreateAPIView.as_view(), name="record-list-create"
    ),
    path(
        "records/<str:uuid>", views.RecordDetailAPIView.as_view(), name="record-detail"
    ),
    path(
        "records/<str:uuid>/histories/",
        views.RecordUpdateHistoryListAPIView.as_view(),
        name="record_update_history-list",
    ),
    path(
        "record-history/<str:uuid>",
        views.RecordUpdateHistoryDetailAPIView.as_view(),
        name="record_update_history-detail",
    ),
]
