# Generated by Django 5.0.2 on 2024-02-29 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_movie_genre_movie_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
