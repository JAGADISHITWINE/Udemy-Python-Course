# Generated by Django 5.0.6 on 2024-06-05 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_movie_genre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='genre',
        ),
    ]