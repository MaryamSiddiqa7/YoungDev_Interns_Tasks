from django.shortcuts import render
from .models import Doctor

def home(request):
    return render(request, 'core/home.html')

def doctors(request):
    doctor_list = Doctor.objects.all()
    return render(request, 'core/doctors.html', {'doctors': doctor_list})
def client_dashboard(request):
    return render(request, 'client_dashboard.html')
