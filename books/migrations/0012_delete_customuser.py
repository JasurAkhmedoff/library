# Generated by Django 5.0.4 on 2024-05-04 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0011_book_already_read_alter_book_like'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]