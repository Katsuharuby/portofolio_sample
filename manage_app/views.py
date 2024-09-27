from django.shortcuts import render,redirect, get_object_or_404
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
        form.save()
        return redirect('manage_app:index')
    context={
        'form':form
    }
    return render(request,'manage_app/day_form.html',context)

def update(request,pk):
    
    day = get_object_or_404(Day, pk=pk)

    form = DayCreateForm(request.POST or None, instance=day)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('manage_app:index')
    
    context={
        'form':form
    }
    return render(request, 'manage_app/day_form.html', context)

def delete(request,pk):
    
    day = get_object_or_404(Day, pk=pk)

    if request.method == 'POST':
        day.delete()
        return redirect('manage_app:index')
    
    context={
        'day':day
    }
    return render(request, 'manage_app/day_confirm_delete.html', context)

def detail(request,pk):
    
    day = get_object_or_404(Day, pk=pk)
    
    context={
        'day':day
    }
    return render(request, 'manage_app/day_detail.html', context)