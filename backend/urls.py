from django.contrib import admin
from django.urls import path, include
from rest_framework import routers              
from .api import AchievementListViewSet, AchievementTagsViewSet, ProjectListViewSet, ProjectTagsViewSet  

router = routers.DefaultRouter()  

router.register(r'api/achievements', AchievementListViewSet, 'achievements') 
router.register(r'api/achievementtags', AchievementTagsViewSet, 'achievements') 
router.register(r'api/projects', ProjectListViewSet, 'achievements') 
router.register(r'api/projecttags', ProjectTagsViewSet, 'achievements') 

urlpatterns = router.urls