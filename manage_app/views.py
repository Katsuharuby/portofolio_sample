from django.db.models.query import QuerySet
from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .forms import DayCreateForm
from .models import Day

class IndexView(generic.ListView):
    model = Day

    def get_queryset(self):
        return Day.objects.all().order_by('date_of_interview')

class AddView(generic.CreateView):
    model = Day
    form_class=DayCreateForm
    success_url=reverse_lazy('manage_app:index')

class UpdateView(generic.UpdateView):
    model = Day
    form_class=DayCreateForm
    success_url=reverse_lazy('manage_app:index')

class DeleteView(generic.DeleteView):
    model=Day
    success_url=reverse_lazy('manage_app:index')

class DetailView(generic.DetailView):
    model = Day
