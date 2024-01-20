from django.urls import path, include
from django.conf import settings


from . import views
from .views import  blog_detail, blog_category

urlpatterns = [
    path("detail/<int:pk>/", blog_detail, name="blog-detail"),
    path("category/<str:category>/", blog_category, name="blog-category"),
    path("blog-delete/<int:pk>", views.blog_delete, name="blog-delete"),
    path("blog-create/", views.blog_create, name="blog-create"),
    path("blog-comment<int:post_id>/", views.blog_comment, name="blog-comment"),
    path(
        "comment-comment/<int:comment_id>/<int:post_id>",
        views.comment_comment,
        name="comment-comment",
    ),
]
