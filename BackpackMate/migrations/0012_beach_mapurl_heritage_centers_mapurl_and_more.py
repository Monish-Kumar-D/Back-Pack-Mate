# Generated by Django 5.0.1 on 2024-12-10 14:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("BackpackMate", "0011_alter_temple_mapurl"),
    ]

    operations = [
        migrations.AddField(
            model_name="beach",
            name="mapUrl",
            field=models.CharField(blank=True, max_length=1200),
        ),
        migrations.AddField(
            model_name="heritage_centers",
            name="mapUrl",
            field=models.CharField(blank=True, max_length=1200),
        ),
        migrations.AddField(
            model_name="tourism_place",
            name="mapUrl",
            field=models.CharField(blank=True, max_length=1200),
        ),
    ]
