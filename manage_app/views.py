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


class IndexView(LoginRequiredMixin, generic.ListView):
    model = Day
    context_object_name = 'day_list'
    paginate_by = 10

    def get_queryset(self):
        sort_by = self.request.GET.get('sort_by', 'date_of_interview')
        filter_upcoming = self.request.GET.get('filter_upcoming', None)  # 「今日から1週間後まで」のフィルタリングオプション
        queryset = Day.objects.filter(author=self.request.user)

        today = timezone.now()
        one_week_later = today + timedelta(days=7)
        print(f"Today's date: {today}, One week later: {one_week_later}")

        if filter_upcoming == 'true':
            # 今日から一週間後までのデータに絞り込み
            queryset = queryset.filter(date_of_interview__range=[today, one_week_later])

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
