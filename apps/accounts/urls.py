"""Module imports"""
# pylint: disable=E0401
from django.urls import path
import apps.accounts.views as Account

urlpatterns = [
    path(
        "signup/",
        Account.UserSignup.as_view(),
        name="user-signup"
    ),
    path(
        "login/",
        Account.UserLogin.as_view(),
        name="user-login"
    ),
    path(
        "logout/",
        Account.UserLogout.as_view(),
        name="user-logout"
    ),
]
