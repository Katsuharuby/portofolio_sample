from django.shortcuts import render
from .forms import DayCreateForm

def index(request):
    return render(request,'manage_app/day_list.html')

def add(request):
    context={
        'form':DayCreateForm()
    }
    return render(request,'manage_app/day_form.html',context)