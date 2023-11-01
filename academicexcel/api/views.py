from backend.models import User
from rest_framework import generics

from .serializers import UserSerializer

class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer