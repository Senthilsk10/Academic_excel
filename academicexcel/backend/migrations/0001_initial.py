# Generated by Django 4.2.6 on 2023-11-01 04:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Assessment",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("assessment_data_id", models.IntegerField()),
                ("source", models.URLField()),
                ("timestamp", models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name="LearningPath",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("path_name", models.CharField(max_length=100)),
                ("details", models.TextField()),
                ("topics", models.TextField()),
                ("followers", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="UserLearningPath",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("assessment_completed", models.CharField(max_length=10)),
                ("progress", models.CharField(max_length=10)),
                (
                    "learning_path",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="backend.learningpath",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="backend.user"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Response",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("score", models.CharField(max_length=10)),
                ("submitted_answer", models.TextField()),
                ("response_time", models.TextField()),
                ("submitted_time", models.DateTimeField()),
                (
                    "assessment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="backend.assessment",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Lesson",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("lesson_number", models.IntegerField()),
                ("content_link", models.URLField()),
                ("article_youtube_blog", models.CharField(max_length=100)),
                ("recommend_assessment", models.BooleanField()),
                ("description", models.TextField()),
                (
                    "path",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="backend.learningpath",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="learningpath",
            name="created_user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="backend.user"
            ),
        ),
        migrations.CreateModel(
            name="Feedback",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("feedback", models.TextField()),
                ("time", models.DateTimeField()),
                (
                    "path",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="backend.learningpath",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="backend.user"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AssessmentData",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("assessment_type", models.CharField(max_length=100)),
                ("question_with_answer", models.TextField()),
                ("response_id", models.IntegerField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="backend.user"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="assessment",
            name="learning_path",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="backend.learningpath"
            ),
        ),
        migrations.AddField(
            model_name="assessment",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="backend.user"
            ),
        ),
    ]
