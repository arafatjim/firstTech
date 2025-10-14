from django.contrib import admin
from .models import FeatureProjects 

class FeatureProjectsAdmin(admin.ModelAdmin):
    list_display = ('Project_name', 'Project_manager', 'Project_desc')

admin.site.register(FeatureProjects, FeatureProjectsAdmin)

