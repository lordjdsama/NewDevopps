"""
For user apps
"""
from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from . import forms

def register(request):
    """
    View for registering a new user.

    If the request method is POST, processes the registration form.
    If the form is valid, saves the user and redirects to the login page.
    If the form is not valid, renders the registration form page with errors.

    If the request method is GET, renders the registration form page.

    Args:
        request: HttpRequest object.

    Returns:
        HttpResponse object rendering the registration form page.
    """
    if request.method == "POST":
        form = forms.UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # cleaned data is a dictionary
            username = form.cleaned_data.get('username')
            messages.success(request, f"{username}, your account is created, please login.")
            return redirect('users-login')
    else:
        form = forms.UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required()
def profile(request):
    """
    View for rendering the user profile page.

    Requires login. Renders the profile page.

    Args:
        request: HttpRequest object.

    Returns:
        HttpResponse object rendering the profile page.
    """
    return render(request, "users/profile.html")
