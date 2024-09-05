from django.urls import path
from .views import *

urlpatterns = [
    path("blogpost/", BlogPostListCreate.as_view(), name="blog-post-create"),
    path(
        "blogpost/<int:pk>",
        BlogPostRetrieveUpdateDestroy.as_view(),
        name="blog-post-update-delete",
    ),
    path("blogpost-get/", BlogPostList.as_view(), name="blog-post-get"),
    path("main/", main, name="main"),
    path("", dashboard, name="dashboard"),
    path("settings/", settings, name="settings"),
    path("stacked-layout/", stacked_layout, name="stacked-layout"),
    path("404/", not_found_404, name="not-found-404"),
    path("500/", server_error_500, name="server-error-500"),
]
