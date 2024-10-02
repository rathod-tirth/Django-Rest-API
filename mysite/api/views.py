from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

# from .models import BlogPost
# from .serializers import BlogPostSerializer


# API
# class BlogPostListCreate(generics.ListCreateAPIView):
#     queryset = BlogPost.objects.all()
#     serializer_class = BlogPostSerializer

#     def delete(self, request, *args, **kwargs):
#         BlogPost.objects.all().delete()
#         return Response(status.HTTP_404_NOT_FOUND)


# class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     queryset = BlogPost.objects.all()
#     serializer_class = BlogPostSerializer
#     lookup_field = "pk"


# class BlogPostList(APIView):
#     def get(self, request, format=None):
#         # Get the title from query parameters (if none, default to empty string)
#         title = request.query_params.get("title", "")

#         if title:
#             # Filter the queryset based on the title
#             blog_posts = BlogPost.objects.filter(title__icontains=title)
#         else:
#             # If no title is provided, return all blog posts
#             blog_posts = BlogPost.objects.all()

#         serializer = BlogPostSerializer(blog_posts, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)


def main(request):
    context = {
        "title": "Admin Main",
        "description": "This is the admin Main.",
        "authors": "Admin Team",
        "robots": "index, follow",
        "footer": True,
    }
    return render(request, "api/layouts/_default/main.html", context)


def dashboard(request):
    context = {
        "title": "Admin Dasboard",
        "description": "This is the admin dashboard.",
        "authors": "Admin Team",
        "robots": "index, follow",
        "footer": True,
        "page_slug": "dasboard",
    }
    return render(request, "api/layouts/_default/dashboard.html", context)


def settings(request):
    context = {
        "title": "User Settings",
        "description": "This is the User Settings.",
        "authors": "Admin Team",
        "robots": "index, follow",
        "footer": True,
        "page_slug": "settings",
    }
    return render(request, "api/layouts/_default/dashboard.html", context)


def stacked_layout(request):
    return render(request, "api/layouts/_default/stacked-layout.html")


def not_found_404(request):
    context = {
        "title": "Not Found 404",
        "navbar": False,
        "footer": False,
        "page_slug": "404",
    }
    return render(request, "api/layouts/_default/main.html", context)


def server_error_500(request):
    context = {
        "title": "Server Error 404",
        "navbar": False,
        "footer": False,
        "page_slug": "500",
    }
    return render(request, "api/layouts/_default/main.html", context)


def maintenanace(request):
    context = {
        "title": "Under Maintenance",
        "navbar": False,
        "footer": False,
        "page_slug": "maintenance",
    }
    return render(request, "api/layouts/_default/main.html", context)


def pricing(request):
    context = {
        "title": "Pricing",
        "navbar": True,
        "footer": True,
        "page_slug": "pricing",
    }
    return render(request, "api/layouts/_default/main.html", context)


def products(request):
    context = {
        "title": "Products",
        "footer": False,
        "page_slug": "products",
    }
    return render(request, "api/layouts/_default/dashboard.html", context)


def users(request):
    context = {
        "title": "Users",
        "footer": False,
        "page_slug": "users",
    }
    return render(request, "api/layouts/_default/dashboard.html", context)


def forgot_password(request):
    context = {
        "title": "Forgot Password",
        "navbar": False,
        "footer": False,
        "page_slug": "forgot_password",
    }
    return render(request, "api/layouts/_default/main.html", context)


def sign_in(request):
    context = {
        "title": "Sign In",
        "navbar": False,
        "footer": False,
        "page_slug": "sign_in",
    }
    return render(request, "api/layouts/_default/main.html", context)


def sign_up(request):
    context = {
        "title": "Sign Up",
        "navbar": False,
        "footer": False,
        "page_slug": "sign_up",
    }
    return render(request, "api/layouts/_default/main.html", context)


def reset_password(request):
    context = {
        "title": "Reset Password",
        "navbar": False,
        "footer": False,
        "page_slug": "reset_password",
    }
    return render(request, "api/layouts/_default/main.html", context)


def profile_lock(request):
    context = {
        "title": "Profile Lock",
        "navbar": False,
        "footer": False,
        "page_slug": "profile_lock",
    }
    return render(request, "api/layouts/_default/main.html", context)
