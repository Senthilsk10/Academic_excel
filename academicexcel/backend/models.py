from django.contrib.auth.models import User
from django.db import models


class LearningPath(models.Model):
    id = models.IntegerField(primary_key=True)
    path_name = models.CharField(max_length=100)
    created_user = models.OneToOneField(User, on_delete=models.CASCADE)
    details = models.TextField()
    topics = models.TextField()
    followers = models.IntegerField()

class Lesson(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    path = models.ForeignKey(LearningPath, on_delete=models.CASCADE)
    lesson_number = models.IntegerField()
    content_link = models.URLField()
    article_youtube_blog = models.CharField(max_length=100)
    recommend_assessment = models.BooleanField()
    description = models.TextField()

class Feedback(models.Model):
    id = models.IntegerField(primary_key=True)
    path = models.ForeignKey(LearningPath, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    feedback = models.TextField()
    time = models.DateTimeField()


class UserLearningPath(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    learning_path = models.ForeignKey(LearningPath, on_delete=models.CASCADE)
    assessment_completed = models.CharField(max_length=10)
    progress = models.CharField(max_length=10)


class Assessment(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    learning_path = models.ForeignKey(LearningPath, on_delete=models.CASCADE)
    assessment_data_id = models.IntegerField()
    source = models.URLField()
    timestamp = models.DateTimeField()


class AssessmentData(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    assessment_type = models.CharField(max_length=100)
    question_with_answer = models.TextField()
    response_id = models.IntegerField()


class Response(models.Model):
    id = models.IntegerField(primary_key=True)
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    score = models.CharField(max_length=10)
    submitted_answer = models.TextField()
    response_time = models.TextField()
    submitted_time = models.DateTimeField()
