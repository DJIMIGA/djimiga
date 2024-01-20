from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=225)
    body = RichTextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("category", related_name="posts")
    thumbnail = models.ImageField(blank=True, upload_to='blog')
    objects = models.Manager()

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=20)


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("post", on_delete=models.CASCADE)
    parent_comment = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True
    )

    objects = models.Manager()

    def __str__(self):
        return f"Comment by{self.author} on {self.post.title}"
