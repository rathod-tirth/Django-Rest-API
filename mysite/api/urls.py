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
    path("", index, name="index"),
    path("dashboard/", dashboard, name="dashboard"),
    path("settings/", settings, name="settings"),
    path("stacked-layout/", stacked_layout, name="stacked-layout"),
]
