from django.urls import path
from . import views

urlpatterns = [
    path('login', views.Login, name='Login'),
    path('logout', views.Logout, name='Logout'),
]