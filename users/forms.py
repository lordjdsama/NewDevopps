"""
Form for user registration.
"""
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):# pylint: disable=too-many-ancestors
    """
    A form for user registration.

    This form extends UserCreationForm and adds an email field for the user's email address.
    """

    email = forms.EmailField()

    class Meta:#pylint: disable=too-few-public-methods
        """
        Form for user registration.
        """
        model = User
        fields = ['username', 'email', 'password1', 'password2']
