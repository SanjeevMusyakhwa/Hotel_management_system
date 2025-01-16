from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegisterForm(UserCreationForm):
    full_name = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'placeholder': "Enter your Full Name",
            'class': 'form-control',
        }),
        help_text="",
    )
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'placeholder': "Enter your Username",
            'class': 'form-control',
        }),
        help_text="",
    )
    phone_number = forms.CharField(
        max_length=17,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your Phone Number',
            'class': 'form-control',
        }),
        help_text="",
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'Enter your Email',
            'class': 'form-control',
        }),
        help_text="",
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Enter your Password',
            'class': 'form-control',
        }),
        help_text="",
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Confirm your Password',
            'class': 'form-control',
        }),
        help_text="",
    )

    class Meta:
        model = User
        fields = ['full_name', 'username', 'email', 'phone_number', 'password1', 'password2']
