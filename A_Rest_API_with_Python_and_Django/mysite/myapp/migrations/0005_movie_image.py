# Generated by Django 5.0.6 on 2024-06-05 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_movie_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.ImageField(default='Unknown', upload_to=''),
            preserve_default=False,
        ),
    ]
