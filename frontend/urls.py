from django.urls import path
from . import views


app_name = "frontend"
urlpatterns = [
    path("", views.index, name='index'),
    path("portfolio/", views.portfolio, name='portfolio'),
    path("achievements/", views.progress, name='achievements'),
    path("projects/", views.projects, name="projects"),
    path("project/<str:project_name>",
         views.project_details, name="project_details"),
    path("projects_tag/<str:project_tag>",
         views.project_tag, name="project_tag"),
    path("blogs/", views.blogs, name="blogs"),
    path("blog/<str:blog_name>", views.blog_details, name="blog_details"),
    path("blogs_tag/<str:blog_tag>", views.blog_tag, name="blog_tag"),
]
