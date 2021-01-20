from rest_framework import serializers
from .models import AchievementList, AchievementTags, ProjectList, ProjectTags

class AchievementListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AchievementList
        fields = '__all__'


class AchievementTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AchievementTags
        fields = "__all__"


class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectList
        fields = "__all__"


class ProjectTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectTags
        fields = "__all__"

