from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import BlogPost
from .serializers import BlogPostSerializer


# API
class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    def delete(self, request, *args, **kwargs):
        BlogPost.objects.all().delete()
        return Response(status.HTTP_404_NOT_FOUND)


class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = "pk"


class BlogPostList(APIView):
    def get(self, request, format=None):
        # Get the title from query parameters (if none, default to empty string)
        title = request.query_params.get("title", "")

        if title:
            # Filter the queryset based on the title
            blog_posts = BlogPost.objects.filter(title__icontains=title)
        else:
            # If no title is provided, return all blog posts
            blog_posts = BlogPost.objects.all()

        serializer = BlogPostSerializer(blog_posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


def index(request):
    context = {
        "title": "Admin Dashboard",
        "description": "This is the admin dashboard.",
        "authors": "Admin Team",
        "robots": "index, follow",
    }
    return render(request, "layouts/_default/main.html", context)


def dashboard(request):
    return render(request, "layouts/_default/dashboard.html")


def stacked_layout(request):
    return render(request, "layouts/_default/stacked-layout.html")
