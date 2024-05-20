from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

# add this:
from wagtail.search import index


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=225)
    body = RichTextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("category", blank=True, null=True, related_name="posts")
    thumbnail = models.ImageField(blank=True, upload_to='blog')
    objects = models.Manager()

    def __str__(self):
        return self.title


class PostPage(Page):
    post_title = RichTextField()
    body = RichTextField(blank=True)
    date = models.DateField("Post date")
    last_modified = models.DateField("last_modified ")
    categories = models.ManyToManyField("category", related_name="posts_page")
    thumbnail = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.PROTECT, related_name='+'
    )

    search_fields = Page.search_fields + [
        index.SearchField('categories'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('post_title'),
        FieldPanel('body'),
        FieldPanel('date'),
        FieldPanel('last_modified'),
        FieldPanel('categories'),
        FieldPanel('thumbnail'),

    ]


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class CategoryPage(Page):
    name = models.CharField(max_length=20)

    content_panels = Page.content_panels + [
        FieldPanel('name'),
    ]
    templates = "blog_category.html"


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
