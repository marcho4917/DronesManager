from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Drone
from django.core.validators import MinValueValidator, MaxValueValidator


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class DroneForm(forms.ModelForm):
    battery_level = forms.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)])

    class Meta:
        model = Drone
        fields = ['name', 'battery_level']
