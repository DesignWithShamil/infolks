from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home_nav/', views.home_nav, name='home_nav'),
]
