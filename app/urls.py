from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('service/', views.services_view, name='services'),
    path('contact/', views.contact)
]