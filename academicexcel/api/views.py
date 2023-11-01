
from backend.models import LearningPath
from rest_framework import generics

from .serializers import LearningPathSerializer

class LearningPathView(generics.ListCreateAPIView):
    queryset = LearningPath.objects.all()
    serializer_class = LearningPathSerializer
