from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('service/', views.service),
    path('contact/', views.contact)
]