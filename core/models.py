from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    thumbnail = models.ImageField(upload_to="projects", blank=True, null=True)
    lien = models.URLField(default="http://127.0.0.1:8000")

    # image = models.FilePathField(path="static/image")
    def __str__(self):
        return self.title
