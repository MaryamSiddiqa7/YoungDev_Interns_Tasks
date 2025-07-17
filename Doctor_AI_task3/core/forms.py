from django import forms
from .models import Doctor

class DoctorRegistrationForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'specialization', 'experience', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'specialization': forms.TextInput(attrs={'class': 'form-control'}),
            'experience': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
