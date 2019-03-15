from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-blog'),
    path('about/', views.about),
]