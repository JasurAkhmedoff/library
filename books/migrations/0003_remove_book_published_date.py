# Generated by Django 5.0.4 on 2024-04-27 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_published_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='published_date',
        ),
    ]