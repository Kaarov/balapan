# Generated by Django 4.2.10 on 2024-02-14 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("story", "0002_alter_story_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="story",
            name="file",
            field=models.FileField(upload_to="story-audio/", verbose_name="Аудио"),
        ),
        migrations.AlterField(
            model_name="story",
            name="image",
            field=models.ImageField(upload_to="story/", verbose_name="Фото"),
        ),
    ]
