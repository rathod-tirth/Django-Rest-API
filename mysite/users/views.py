from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import *

# Create your views here.


def home(request):
    context = {
        "title": "Admin Dasboard",
        "description": "This is the admin dashboard.",
        "authors": "Admin Team",
        "robots": "index, follow",
        "footer": True,
        "page_slug": "dasboard",
    }
    return render(request, "layouts/_default/dashboard.html", context)


def sign_in(request):
    if request.method == "POST":
        form = SignInForm(request.POST)

        if form.is_valid():
            username = request.POST["email"]
            password = request.POST["password"]

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print("Logged In")
            else:
                print("User Authentication Error")
        else:
            print("Form Validation Error")

    else:
        form = SignInForm()
        context = {
            "title": "Sign In",
            "navbar": False,
            "footer": False,
            "page_slug": "sign_in",
            "form": form,
        }
        return render(request, "layouts/_default/main.html", context)
