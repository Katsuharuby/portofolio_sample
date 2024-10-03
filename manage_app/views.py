from django.db.models.query import QuerySet
from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .forms import DayCreateForm
from .models import Day
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import DayCreateForm, SignUpForm
from django.contrib.auth import login
from django.utils import timezone
from datetime import timedelta
from .forms import DateRangeForm

class IndexView(LoginRequiredMixin, generic.ListView):
    model = Day
    context_object_name = 'day_list'
    paginate_by = 10

    def get_queryset(self):
        filter_by = self.request.GET.get('filter_by', 'date_of_interview')

        default_start_date = '2024-01-01'
        default_end_date = '2026-12-31'

        start_date = self.request.GET.get('start_date', default_start_date)
        end_date = self.request.GET.get('end_date', default_end_date)

        queryset = Day.objects.filter(author=self.request.user)

        if start_date and end_date:
            queryset = queryset.filter(**{
                f'{filter_by}__range': [start_date, end_date]
            })

        return queryset.order_by(filter_by)


class AddView(LoginRequiredMixin, generic.CreateView):
    model = Day
    form_class = DayCreateForm
    success_url = reverse_lazy('manage_app:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        response = super().form_valid(form)

        if self.request.POST.get('action') == 'save_and_add':
            return redirect('manage_app:add')
        return response

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

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('manage_app:index')
    else:
        form = SignUpForm()
    return render(request, 'manage_app/signup.html', {'form': form})
