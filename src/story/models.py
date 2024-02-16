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


class Story(TimestampedModel):
    title = models.CharField(verbose_name="Имя", max_length=255)
    image = models.ImageField("Фото", upload_to='story/')
    audio = models.FileField(verbose_name="Аудио", upload_to='story-audio', blank=True, null=True)

    class Meta:
        verbose_name = "История"
        verbose_name_plural = "Истории"
        ordering = ("-created_at",)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        text_to_speech = " ".join([text.title for text in self.text_story.all()])

        url = "http://tts.ulut.kg/api/tts"
        token = "8zH0qEKi4Cj2DxmLQ37ax1ZJaclAqQayYFg6sUm4SPlLjKmWgc7G4ijeEhdIxlGJ"

        # Your JSON data to be sent in the request body
        json_data = {
            "text": text_to_speech[:800],
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


class TextModel(TimestampedModel):
    title = models.CharField(verbose_name="Имя", max_length=255)
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='text_story')

    class Meta:
        verbose_name = "Текст"
        verbose_name_plural = "Тексты"
        ordering = ("id",)

    def __str__(self):
        return self.title
