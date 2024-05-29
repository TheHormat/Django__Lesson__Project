from django.urls import path
from .views import *

app_name = "account"

urlpatterns = [
    path("register", register__view, name="register"),
    path("login", login__view, name="login"),
    path("logout", logout__view, name="logout"),
]