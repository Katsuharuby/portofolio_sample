from django.shortcuts import render,redirect
from .forms import DayCreateForm
from .models import Day

def index(request):
    context={
        'day_list':Day.objects.all()
    }
    return render(request,'manage_app/day_list.html',context)

def add(request):
    form = DayCreateForm(request.POST or None)
    if request.method=='POST' and form.is_valid():
        form.save
        return redirect('diary:index')
    context={
        'form':form
    }
    return render(request,'manage_app/day_form.html',context)