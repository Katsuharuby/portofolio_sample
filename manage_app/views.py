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


from django.utils import timezone
from datetime import timedelta

class IndexView(LoginRequiredMixin, generic.ListView):
    model = Day
    context_object_name = 'day_list'
    paginate_by = 10

    def get_queryset(self):
        sort_by = self.request.GET.get('sort_by', 'date_of_interview')
        filter_recent = self.request.GET.get('filter_recent', None)
        queryset = Day.objects.filter(author=self.request.user)

        today = timezone.now()
        one_week_from_now = today + timedelta(days=7)

        if filter_recent == 'true':
            # フィルタリングオプションに基づいて期間を絞り込む
            if sort_by == 'date_of_interview':
                queryset = queryset.filter(date_of_interview__range=[today, one_week_from_now])
            elif sort_by == 'date_of_spi':
                queryset = queryset.filter(date_of_spi__range=[today, one_week_from_now])
            elif sort_by == 'resume_of_spi':
                queryset = queryset.filter(resume_of_spi__range=[today, one_week_from_now])
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
