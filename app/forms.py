from django.forms import ModelForm
from app.models import Student

from django import forms
from .models import Student

class StudentFrorm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'address', 'faculty']
        
        # Custom widget and CSS classes for each field
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your name'
            }),
            'age': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your age'
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your address'
            }),
            'faculty': forms.Select(attrs={
                'class': 'form-control'
            }),
        }
