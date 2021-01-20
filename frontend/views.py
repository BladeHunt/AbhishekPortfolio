from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
import requests
from os import environ
from django.http import HttpResponseRedirect
import re
from django.template.loader import render_to_string
from django.http import JsonResponse
from backend.models import (
    AchievementList,
    AchievementTags,
    ProjectList,
    ProjectTags,
    Portfolio,
    Blog,
    BlogTags,
)


context = {}

PROJECT_TAG = "projects_tag/"
BLOG_TAG = "blogs_tag/"


def add_css(project_description):
    filtered_description = re.split('(<pre class="|<img)', project_description)
    updated_description = []
    for desc in filtered_description:
        if desc.startswith("<img"):
            updated_description.append(desc + " class='wd-100' ")
        elif desc.startswith("<pre"):
            updated_description.append(desc + "wd-100 ")
        else:
            updated_description.append(desc)

    return "".join(updated_description)


def update_upload(link):
    updated_upload = link.name.replace(
        "frontend/static/frontend/img/uploads/", "../../static/frontend/img/uploads/"
    )

    return updated_upload


def index(request):
    return render(request, "frontend/index.html", context)


def portfolio(request):
    context["jobs"] = Portfolio.JobList.objects.all()
    for job in context["jobs"]:
        descriptions = job.description.split(".")
        del descriptions[0]
        job.description = descriptions

    context["educations"] = Portfolio.EducationList.objects.all()

    return render(request, "frontend/portfolio.html", context)


def achievements(request):
    return render(request, "frontend/achievements.html")


def projects(request):
    project_list = ProjectList.objects.all()
    if project_list:
        for project in project_list:
            project.upload = update_upload(project.upload)
            project.slug = "/project/" + project.slug

    context = {"link": PROJECT_TAG}

    return render(request, "frontend/projects.html", {"projects": project_list})


def project_details(request, project_name):
    print("Hello")
    project = ProjectList.objects.filter(slug=project_name).first()

    if project:
        project.upload = update_upload(project.upload)

        context = {
            "project": project,
            "project_name": project_name,
            "link": PROJECT_TAG,
        }
        project.description = add_css(project.description)
    return render(request, "frontend/project_details.html", context)


def project_tag(request, project_tag):
    tags = [t.name.lower() for t in ProjectTags.objects.all()]

    if project_tag in tags:
        projects = ProjectList.objects.filter(tag__name__iexact=project_tag)
        for project in projects:
            project.upload = update_upload(project.upload)
        context = {
            "projects": projects,
            "tag": project_tag,
            "link": PROJECT_TAG + project_tag,
        }

    return render(request, "frontend/project_tag.html", context)


def blogs(request):
    ctx = {}
    url_parameter = request.GET.get("q")

    if url_parameter:
        blogs_list = Blog.objects.filter(name__icontains=url_parameter)
    else:
        blogs_list =  Blog.objects.all()

    if blogs_list:
        for blog_list in blogs_list:
            blog_list.upload = update_upload(blog_list.upload)
            blog_list.slug = "/blogs/" + blog_list.slug

    ctx["blogs"] = blogs_list
    ctx["link"] = BLOG_TAG

    if request.is_ajax():
        html = render_to_string(
            template_name="frontend/blog-partial.html", context={"blogs": blogs_list}
        )
        data_dict = {"html_from_view": html}
        return JsonResponse(data=data_dict, safe=False)

    return render(request, "frontend/blogs.html", context=ctx)


def blog_details(request, blog_name):
    blog = Blog.objects.filter(slug=blog_name).first()
    if blog:
        blog.upload = update_upload(blog.upload)

        context = {
            "blog": blog,
            "blog_name": blog_name,
            "link": BLOG_TAG + blog_tag,
        }
        blog.description = add_css(blog.description)
    return render(request, "frontend/blog_details.html", context)


def blog_tag(request, blog_tag):
    tags = [t.name.lower() for t in BlogTags.objects.all()]
    if blog_tag in tags:
        blogs = Blog.objects.filter(tag__name__iexact=blog_tag)
        for blog in blogs:
            blog.upload = update_upload(blog.upload)
        context = {
            "blogs": blogs,
            "tag": blog_tag,
            "link": BLOG_TAG + blog_tag,
        }

    return render(request, "frontend/blog_tag.html", context)


def progress(request):
    return render(request, "frontend/progress.html", {"page_type": 0})


def error_404_view(request, exception):
    return render(request, "frontend/progress.html", {"page_type": "error"})