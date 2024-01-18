from django.contrib import admin

# Register your models here.
from .models import Project

# permet d'aficher les utilisateus dans admin django
admin.site.register(Project)
