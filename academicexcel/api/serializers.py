from rest_framework import serializers

from backend.models import LearningPath



class LearningPathSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningPath
        fields = "__all__"