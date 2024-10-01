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
    paginate_by = 100

    def get_queryset(self):
        sort_by = self.request.GET.get('sort_by', 'date_of_interview')
        start_date = self.request.GET.get('start_date', None)
        end_date = self.request.GET.get('end_date', None)
        filter_by = self.request.GET.get('filter_by', 'date_of_interview')  # 基準フィールドを取得
        
        queryset = Day.objects.filter(author=self.request.user)

        # 日付範囲でのフィルタリング
        if start_date and end_date:
            filter_field = f'{filter_by}__range'
            queryset = queryset.filter(**{filter_field: [start_date, end_date]})
        
        return queryset.order_by(sort_by)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date_range_form'] = DateRangeForm(self.request.GET or None)
        return context


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
