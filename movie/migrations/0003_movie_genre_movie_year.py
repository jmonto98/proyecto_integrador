# Generated by Django 5.0.2 on 2024-02-29 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_alter_movie_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='movie',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]