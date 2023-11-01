from django.urls import path
from .views import LearningPathView

urlpatterns  = [
    path('',LearningPathView.as_view()),
]