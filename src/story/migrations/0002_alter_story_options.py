# Generated by Django 4.2.10 on 2024-02-14 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("story", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="story",
            options={
                "ordering": ("-created_at",),
                "verbose_name": "История",
                "verbose_name_plural": "Истории",
            },
        ),
    ]
