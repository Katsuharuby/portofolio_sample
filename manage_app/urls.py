from django.urls import path
from .import views
app_name='manage_app'
urlpatterns=[
    path('',views.index,name='index')
]