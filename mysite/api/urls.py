from django.urls import path
from . import views

urlpatterns = [
    path("blogpost/", views.BlogPostListCreate.as_view(), name="blog-post-create")
]
