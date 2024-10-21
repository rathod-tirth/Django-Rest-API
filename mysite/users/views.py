from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.conf import settings
from .models import *

# Create your views here.


@login_required
def home(request):
    """
    Dashboard Home Page
    """

    # user = {"firstname": "", "lastname": "", "email": ""}
    # if request.user.is_superuser:
    #     user.firstname = "Admin"
    # else:
    #     BackendUser = BackendUser(request.user)
    #     user.firstname = BackendUser.firstname
    #     user.lastname = BackendUser.lastname
    #     user.email = BackendUser.email

    context = {
        "title": "ShipWreck",
        "description": "ShipWreck Admin Dashboard",
        "authors": "Admin Team",
        "robots": "index, follow",
        "footer": True,
        "page_slug": "dasboard",
        # "user": user,
    }
    return render(request, "layouts/_default/dashboard.html", context)


def sign_in(request):
    """
    Sign In Page of Backend User
    """
    context = {
        "title": "Sign In",
        "navbar": False,
        "footer": False,
        "page_slug": "sign_in",
    }

    if request.method == "POST":
        form = SignInForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)

                if form.cleaned_data["remember"]:
                    request.session.set_expiry(604800)
                else:
                    request.session.set_expiry(0)

                return redirect("home")
            else:
                print("User Authentication Error")
                context["form"] = form
                context["error"] = "Incorrect Email or Password"
                return render(request, "layouts/_default/main.html", context)
        else:
            print("Form Validation Error")
            context["form"] = form
            context["error"] = "Provide Proper Email and Password"
            return render(request, "layouts/_default/main.html", context)

    else:
        form = SignInForm()
        context["form"] = form
        return render(request, "layouts/_default/main.html", context)


def sign_out(request):
    logout(request)
    return redirect(f"{settings.LOGIN_URL}")


def sign_up(request):
    pass
