# Generated by Django 5.1.4 on 2024-12-17 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Question",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("question_text", models.CharField(max_length=200)),
                ("first_choice", models.CharField(max_length=200)),
                ("second_choice", models.CharField(max_length=200)),
                ("third_choice", models.CharField(max_length=200)),
                ("fourth_choice", models.CharField(max_length=200)),
                (
                    "correct_choice",
                    models.CharField(
                        choices=[("1", "1"), ("2", "2"), ("3", "3"), ("4", "4")],
                        max_length=200,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="QuizSession",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("answered", models.IntegerField(default=0)),
                ("correct", models.IntegerField(default=0)),
                ("incorrect", models.IntegerField(default=0)),
            ],
        ),
    ]