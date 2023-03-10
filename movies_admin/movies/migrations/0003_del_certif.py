# Generated by Django 3.2 on 2023-02-05 13:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_film_fields'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filmwork',
            name='certificate',
        ),
        migrations.AlterField(
            model_name='filmwork',
            name='creation_date',
            field=models.DateField(blank=True, verbose_name='creation_date'),
        ),
        migrations.AlterField(
            model_name='filmwork',
            name='description',
            field=models.TextField(blank=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='filmwork',
            name='rating',
            field=models.FloatField(blank=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='rating'),
        ),
        migrations.AlterField(
            model_name='filmwork',
            name='title',
            field=models.CharField(max_length=255, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='filmwork',
            name='type',
            field=models.CharField(choices=[('MV', 'movie'), ('TS', 'tv-show')], max_length=255, verbose_name='type'),
        ),
        migrations.AlterField(
            model_name='personfilmwork',
            name='role',
            field=models.CharField(choices=[('director', 'director'), ('actor', 'actor'), ('writer', 'writer')], max_length=255, null=True, verbose_name='role'),
        ),
    ]
