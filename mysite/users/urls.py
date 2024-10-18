from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("sign-in", sign_in, name="sign-in"),
]
