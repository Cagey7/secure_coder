from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import *



class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="Username")
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Confirm password", widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ("username", "password1", "password2")



class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="Login", widget=forms.TextInput())
    password = forms.CharField(label="Password", widget=forms.PasswordInput())
