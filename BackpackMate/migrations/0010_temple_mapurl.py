# Generated by Django 5.0.1 on 2024-12-10 14:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("BackpackMate", "0009_beach"),
    ]

    operations = [
        migrations.AddField(
            model_name="temple",
            name="mapUrl",
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
