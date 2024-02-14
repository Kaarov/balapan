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
    file = models.FileField("Аудио", upload_to='word-audio/')

    class Meta:
        verbose_name = "Слово"
        verbose_name_plural = "Словы"
        ordering = ("-created_at",)

    def __str__(self):
        return self.title
