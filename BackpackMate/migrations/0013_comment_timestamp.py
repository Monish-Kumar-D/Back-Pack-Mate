# Generated by Django 5.0.1 on 2024-12-20 18:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("BackpackMate", "0012_beach_mapurl_heritage_centers_mapurl_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="timestamp",
            field=models.DateTimeField(
                auto_now_add=True,
                default=datetime.datetime(
                    2024, 12, 20, 18, 30, 13, 347064, tzinfo=datetime.timezone.utc
                ),
            ),
            preserve_default=False,
        ),
    ]
