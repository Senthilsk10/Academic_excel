from django.contrib import admin

from django.contrib import admin
from .models import User, LearningPath, Feedback, Lesson, UserLearningPath, Assessment, AssessmentData, Response

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(LearningPath)
class LearningPathAdmin(admin.ModelAdmin):
    list_display = ('id', 'path_name', 'created_user', 'details', 'topics', 'followers')

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'path', 'user', 'feedback', 'time')

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'path', 'lesson_number', 'content_link', 'article_youtube_blog', 'recommend_assessment', 'description')

@admin.register(UserLearningPath)
class UserLearningPathAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'learning_path', 'assessment_completed', 'progress')

@admin.register(Assessment)
class AssessmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'learning_path', 'assessment_data_id', 'source', 'timestamp')

@admin.register(AssessmentData)
class AssessmentDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'assessment_type', 'question_with_answer', 'response_id')

@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ('id', 'assessment', 'score', 'submitted_answer', 'response_time', 'submitted_time')
