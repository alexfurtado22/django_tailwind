from django.urls import path
from app.views import TourCreateView, TourListView, TourUpdateView, TourDeleteView

urlpatterns = [
    path("", TourListView.as_view(), name="home"),
    path(
        "create/", TourCreateView.as_view(), name="tour_create"
    ),  # Adding a name for the route
    path(
        "<int:pk>/update/", TourUpdateView.as_view(), name="tour_update"
    ),  # Adding a name for the route
    path(
        "<int:pk>/delete/", TourDeleteView.as_view(), name="tour_delete"
    ),  # Adding a name for the route
]
