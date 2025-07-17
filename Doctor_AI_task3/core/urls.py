from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('doctors/', views.doctors, name='doctors'),
    path('client/', views.client_dashboard, name='client_dashboard'),
    path('register-doctor/', views.doctor_register, name='register_doctor'),
]
