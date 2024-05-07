# Generated by Django 5.0.4 on 2024-05-03 09:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_book_like'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='already_read',
            field=models.ManyToManyField(blank=True, related_name='read_books', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='book',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='liked_books', to=settings.AUTH_USER_MODEL),
        ),
    ]