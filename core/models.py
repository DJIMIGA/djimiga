from django.db import models

from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.search import index
from wagtail.fields import RichTextField


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    thumbnail = models.ImageField(upload_to="projects", blank=True, null=True)
    lien = models.URLField(default="http://127.0.0.1:8000")

    # image = models.FilePathField(path="static/image")
    def __str__(self):
        return self.title


class ProjectPage(Page):
    description = RichTextField(blank=True)
    technology = models.CharField(max_length=20)
    thumbnail = models.ImageField(upload_to="projects", blank=True, null=True)
    lien = models.URLField(default="http://127.0.0.1:8000")
    content_panels = Page.content_panels + [
        FieldPanel("description"),
        FieldPanel("technology"),
        FieldPanel("thumbnail"),
        FieldPanel("lien"),
    ]

    search_fields = Page.search_fields + [
        index.SearchField("description"),
    ]

    def __str__(self):
        return self.title

    trmplates = "core/templates/Sproject_page.html"

