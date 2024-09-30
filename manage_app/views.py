from django.db.models.query import QuerySet
from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .forms import DayCreateForm
from .models import Day
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(LoginRequiredMixin, generic.ListView):
    model = Day

    def get_queryset(self):
        return Day.objects.filter(author=self.request.user).order_by('date_of_interview')

class AddView(LoginRequiredMixin, generic.CreateView):
    model = Day
    form_class=DayCreateForm
    success_url=reverse_lazy('manage_app:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class UpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Day
    form_class=DayCreateForm
    success_url=reverse_lazy('manage_app:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_queryset(self):
        return Day.objects.filter(author=self.request.user)

class DeleteView(LoginRequiredMixin, generic.DeleteView):
    model=Day
    success_url=reverse_lazy('manage_app:index')

    def get_queryset(self):
        return Day.objects.filter(author=self.request.user)

class DetailView(LoginRequiredMixin, generic.DetailView):
    model = Day
