from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import CustomUser
from django import forms

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)  # make email required

    class Meta:
        model = CustomUser
        fields = ("username", "email", "password1", "password2")

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        class Meta:
            model = CustomUser
            fields = ("username", "email", "password1", "password2")