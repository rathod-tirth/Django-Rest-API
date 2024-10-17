from django.shortcuts import render

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
