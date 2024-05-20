from django.contrib import admin

# Register your models here.
from .models import Project, ProjectPage

# permet d'aficher les utilisateus dans admin django
admin.site.register(Project)
admin.site.register(ProjectPage)
