from typing import Any

from django.contrib import messages
from django.db.models.query import QuerySet
from django.db.models import Q
from app.models import Tour
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class TourListView(LoginRequiredMixin, ListView):
    template_name = "app/home.html"
    model = Tour
    context_object_name = "tours"
    paginate_by = 6

    def get_queryset(self) -> QuerySet[Any]:

        search = self.request.GET.get("search")
        queryset = super().get_queryset().filter(creator=self.request.user)
        if search:
            queryset = queryset.filter(
                Q(oringin_contry__icontains=search)
                | Q(destination_country__icontains=search)
                | Q(comment__icontains=search)
            )
        return queryset.order_by("-create_at")


class TourCreateView(LoginRequiredMixin, CreateView):
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

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class TourUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
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

    def test_func(self) -> bool | None:
        return self.request.user == self.get_object().creator

    def post(self, request, *args, **kwargs):
        messages.success(request, "Your Tour has been update successfully!")

        return super().post(request, *args, **kwargs)


class TourDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "app/tour_delete.html"
    model = Tour
    success_url = reverse_lazy("home")
    context_object_name = "tour"

    def test_func(self) -> bool | None:
        return self.request.user == self.get_object().creator

    def post(self, request, *args, **kwargs):
        messages.success(request, "Your Tour has been delete successfully!")

        return super().post(request, *args, **kwargs)


# Create your views here.
