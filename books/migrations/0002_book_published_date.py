# Generated by Django 5.0.4 on 2024-04-27 11:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='published_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2024, 4, 27, 11, 36, 31, 806099, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]
