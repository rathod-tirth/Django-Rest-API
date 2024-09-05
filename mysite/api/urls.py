from django.urls import path
from . import views

urlpatterns = [
    path("blogpost/", views.BlogPostListCreate.as_view(), name="blog-post-create"),
    path(
        "blogpost/<int:pk>",
        views.BlogPostRetrieveUpdateDestroy.as_view(),
        name="blog-post-update-delete",
    ),
    path("blogpost-get/", views.BlogPostList.as_view(), name="blog-post-get"),
    path("", views.index, name="index"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("stacked-layout/", views.stacked_layout, name="stacked-layout"),
]
