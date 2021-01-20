from django.shortcuts import render
from rest_framework import viewsets, permissions    
from .serializers import AchievementListSerializer, AchievementTagsSerializer, ProjectListSerializer, ProjectTagsSerializer    
from .models import AchievementList, AchievementTags, ProjectList, ProjectTags

# Create your views here.
class AchievementListViewSet(viewsets.ModelViewSet):
    serializer_class = AchievementListSerializer         
    queryset = AchievementList.objects.all() 
    permission_classes = [
        permissions.AllowAny
    ]


class AchievementTagsViewSet(viewsets.ModelViewSet):
    serializer_class = AchievementTagsSerializer         
    queryset = AchievementTags.objects.all() 
    permission_classes = [
        permissions.AllowAny
    ]


class ProjectListViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectListSerializer         
    queryset = ProjectList.objects.all() 
    permission_classes = [
        permissions.AllowAny
    ]


class ProjectTagsViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectTagsSerializer         
    queryset = ProjectTags.objects.all() 
    permission_classes = [
        permissions.AllowAny
    ]