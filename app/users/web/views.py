from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from .forms import LoginForm, SignupForm


def user_signup(request):
    """
    View for user signup
    """
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = SignupForm()
    return render(request, "authentication/signup.html", {"form": form})


# login page
def user_login(request):
    """
    View for user login
    """
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect("task_list")
    else:
        form = LoginForm()
    return render(request, "authentication/login.html", {"form": form})


# logout page
def user_logout(request):
    """
    View for user logout
    """
    logout(request)
    return redirect("login")
