import datetime
from django.shortcuts import render, redirect
from .models import Doctor
from .forms import DoctorRegistrationForm

def home(request):
    tips = [
        "💧 Stay hydrated: Aim for 8–10 glasses of water daily to keep your body functioning properly.",
        "🥦 Eat more greens: Leafy vegetables are rich in essential vitamins and antioxidants.",
        "🏃 Exercise regularly: 30 minutes of moderate activity a day improves heart health and reduces stress.",
        "🛏️ Get quality sleep: Aim for 7–9 hours of sleep each night to allow your body to repair and refresh.",
        "😌 Practice stress management: Techniques like meditation and deep breathing can greatly improve mental health.",
        "🧴 Wash your hands: Prevent the spread of infections by washing hands thoroughly and often.",
        "🍎 Avoid processed foods: Opt for natural, whole foods to maintain a healthy weight and reduce disease risk.",
        "☀️ Get sunlight: A few minutes of sun exposure helps your body produce vitamin D, crucial for immunity.",
        "🧘 Take screen breaks: 5–10 minute breaks every hour help reduce eye strain and mental fatigue.",
        "🔍 Go for regular checkups: Early detection through routine screening is key for prevention."
    ]

    today = datetime.date.today()
    tip_of_the_day = tips[today.day % len(tips)]

    return render(request, 'core/home.html', {
        "health_tip": tip_of_the_day
    })

def doctors(request):
    doctor_list = Doctor.objects.filter(is_approved=True)
    return render(request, 'core/doctors.html', {'doctors': doctor_list})

def client_dashboard(request):
    tips = [
        "💧 Stay hydrated: Aim for 8–10 glasses of water daily to keep your body functioning properly.",
        "🥦 Eat more greens: Leafy vegetables are rich in essential vitamins and antioxidants.",
        "🏃 Exercise regularly: 30 minutes of moderate activity a day improves heart health and reduces stress.",
        "🛏️ Get quality sleep: Aim for 7–9 hours of sleep each night to allow your body to repair and refresh.",
        "😌 Practice stress management: Techniques like meditation and deep breathing can greatly improve mental health.",
        "🧴 Wash your hands: Prevent the spread of infections by washing hands thoroughly and often.",
        "🍎 Avoid processed foods: Opt for natural, whole foods to maintain a healthy weight and reduce disease risk.",
        "☀️ Get sunlight: A few minutes of sun exposure helps your body produce vitamin D, crucial for immunity.",
        "🧘 Take screen breaks: 5–10 minute breaks every hour help reduce eye strain and mental fatigue.",
        "🔍 Go for regular checkups: Early detection through routine screening is key for prevention."
    ]

    today = datetime.date.today()
    tip_of_the_day = tips[today.day % len(tips)]

    return render(request, 'client_dashboard.html', {
        "health_tip": tip_of_the_day
    })

def doctor_register(request):
    if request.method == 'POST':
        form = DoctorRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'core/registration_success.html')
    else:
        form = DoctorRegistrationForm()
    return render(request, 'core/doctor_register.html', {'form': form})
