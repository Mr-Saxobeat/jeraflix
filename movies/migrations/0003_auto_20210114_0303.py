# Generated by Django 3.1.5 on 2021-01-14 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movie_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='tmdb_id',
            field=models.IntegerField(verbose_name='tmdb_id'),
        ),
    ]
