from django.shortcuts import render
from app.models import Tour
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView


class TourListView(ListView):
    template_name = "app/home.html"
    model = Tour
    context_object_name = "tours"


class TourCreateView(CreateView):
    template_name = "app/tour_create.html"
    model = Tour
    fields = [
        "oringin_contry",
        "destination_country",
        "number_of_nights",
        "price",
        "comment",
        "status",
    ]

    success_url = reverse_lazy("home")


class TourUpdateView(UpdateView):
    template_name = "app/tour_update.html"
    model = Tour
    fields = [
        "oringin_contry",
        "destination_country",
        "number_of_nights",
        "price",
        "comment",
        "status",
    ]
    success_url = reverse_lazy("home")
    context_object_name = "tour"


class TourDeleteView(DeleteView):
    template_name = "app/tour_delete.html"
    model = Tour
    success_url = reverse_lazy("home")
    context_object_name = "tour"


# Create your views here.
