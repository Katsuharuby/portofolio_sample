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
        # クエリパラメータを取得
        sort_by = self.request.GET.get('sort_by', 'date_of_interview')
        filter_by = self.request.GET.get('filter_by', 'date_of_interview')
        start_date = self.request.GET.get('start_date', '2024-01-01')
        end_date = self.request.GET.get('end_date', '2026-12-31')

        # ユーザーごとのデータを取得
        queryset = Day.objects.filter(author=self.request.user)

        # 日付範囲で絞り込み
        if start_date and end_date:
            queryset = queryset.filter(**{
                f'{filter_by}__range': [start_date, end_date]
            })

        # ソート
        return queryset.order_by(sort_by)


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
