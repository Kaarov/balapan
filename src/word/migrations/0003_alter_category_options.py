# Generated by Django 4.2.10 on 2024-02-14 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("word", "0002_alter_word_file"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={
                "ordering": ("id",),
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
            },
        ),
    ]
