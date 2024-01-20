from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from .models import Project


@modeladmin_register
class ProjectAdmin(ModelAdmin):
    model = Project
    menu_label = "Projects"
    menu_icon = "placeholder"
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("title", "technology")
    search_fields = ("title", "technology")
    index_templates = "../templates/modeladmin/core/project/project_index.html"
