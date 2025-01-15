from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegisterForm(UserCreationForm):
    full_name = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'placeholder': "Enter your Full Name",
            'class': 'form-control',
        })
    )
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'placeholder': "Enter your Username",
            'class': 'form-control',
        })
    )
    phone_number = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your Phone Number',
            'class': 'form-control',
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'Enter your Email',
            'class': 'form-control',
        })
    )
    
    class Meta:
        model = User
        fields = ['full_name', 'username', 'email', 'phone_number', 'password1', 'password2']
