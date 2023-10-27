from django.urls import path

from .views import user_login, user_logout, user_signup

urlpatterns = [
    path("login/", user_login, name="login"),
    path("signup/", user_signup, name="signup"),
    path("logout/", user_logout, name="logout"),
]
