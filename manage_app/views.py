from django.shortcuts import render

def index(request):
    return render(request,'manage_app/day_list.html')
