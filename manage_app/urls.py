from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

app_name='manage_app'

urlpatterns=[
    path('',views.IndexView.as_view(),name='index'),
    path('add/',views.AddView.as_view(),name='add'),
    path('update/<int:pk>',views.UpdateView.as_view(),name='update'),
    path('delete/<int:pk>',views.DeleteView.as_view(),name='delete'),
    path('detail/<int:pk>',views.DetailView.as_view(),name='detail'),
    path('login/', auth_views.LoginView.as_view(template_name='manage_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]