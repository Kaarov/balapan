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
    file = models.FileField("Аудио", upload_to='story-audio/')

    class Meta:
        verbose_name = "История"
        verbose_name_plural = "Истории"
        ordering = ("-created_at",)

    def __str__(self):
        return self.title


class TextModel(TimestampedModel):
    title = models.CharField(verbose_name="Имя", max_length=255)
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='text_story')

    class Meta:
        verbose_name = "Текст"
        verbose_name_plural = "Тексты"
        ordering = ("-created_at",)

    def __str__(self):
        return self.title
