import requests
from django.core.files.base import ContentFile

from django.db import models
from django.utils.translation import gettext_lazy as _


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(_("Дата создания"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Дата обновления"), auto_now=True)

    class Meta:
        abstract = True
        get_latest_by = "updated_at"


class Category(TimestampedModel):
    title = models.CharField(verbose_name="Имя", max_length=255)
    image = models.ImageField("Фото", upload_to='category/')

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ("id",)

    def __str__(self):
        return self.title


class Word(TimestampedModel):
    category = models.ForeignKey(
        Category,
        verbose_name="Категория",
        on_delete=models.CASCADE,
        blank=True,
        related_name='word_category'
    )
    title = models.CharField(verbose_name="Имя", max_length=255)
    image = models.ImageField("Фото", upload_to='word/')
    audio = models.FileField(verbose_name="Аудио", upload_to='word-audio', blank=True, null=True)

    class Meta:
        verbose_name = "Слово"
        verbose_name_plural = "Словы"
        ordering = ("-created_at",)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        url = "http://tts.ulut.kg/api/tts"
        token = "8zH0qEKi4Cj2DxmLQ37ax1ZJaclAqQayYFg6sUm4SPlLjKmWgc7G4ijeEhdIxlGJ"

        # Your JSON data to be sent in the request body
        json_data = {
            "text": self.title,
            "speaker_id": "1"
        }

        # Headers including Bearer token and Content-Type
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

        # Make the POST request
        response = requests.post(url, json=json_data, headers=headers)
        audio_content = response.content
        self.audio.save(f"{self.title}.mp3", ContentFile(audio_content), save=False)
        super().save(*args, **kwargs)
