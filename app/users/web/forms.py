from django import forms
from django.contrib.auth.forms import UserCreationForm

from users.models import User


class SignupForm(UserCreationForm):
    """
    User registration form
    """

    class Meta:
        model = User
        fields = ["name", "email", "password1", "password2"]


class LoginForm(forms.Form):
    """
    User login form
    """

    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
