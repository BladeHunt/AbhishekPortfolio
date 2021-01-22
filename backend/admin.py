from django.contrib import admin
from .models import (
    AchievementList,
    AchievementTags,
    ProjectList,
    ProjectTags,
    Portfolio,
    Blog,
    BlogTags,
)
from tinymce import TinyMCE
from django.db import models


# Register your models here.
class AchievementListAdmin(admin.ModelAdmin):
    fields = ["achievement_name", "achievement_description", "achievement_date"]

    fieldsets = [
        ("Name", {"fields": ["achievement_name"]}),
        ("Data", {"fields": ["achievement_description, achievement_date"]}),
    ]


class AchievementListAdmin(admin.ModelAdmin):
    formfield_overrides = {models.TextField: {"widget": TinyMCE()}}


class ProjectListAdmin(admin.ModelAdmin):
    formfield_overrides = {models.TextField: {"widget": TinyMCE()}}


class BlogAdmin(admin.ModelAdmin):
    formfield_overrides = {models.TextField: {"widget": TinyMCE()}}


admin.site.register(AchievementList, AchievementListAdmin)
admin.site.register(AchievementTags)
admin.site.register(ProjectList, ProjectListAdmin)
admin.site.register(ProjectTags)
admin.site.register(Portfolio.EducationList)
admin.site.register(Portfolio.JobList)
admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogTags)
