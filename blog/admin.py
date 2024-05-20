from django.contrib import admin

# Register your models here.
from .models import Post, PostPage, Category,CategoryPage, Comment


admin.site.register(Post)
admin.site.register(PostPage)
admin.site.register(Category)
admin.site.register(CategoryPage)