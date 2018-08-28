from django.urls import path
from . import views

urlpatterns = [
    path('', views.services, name="services"),
    path('completed/', views.completed, name="completed"),
]