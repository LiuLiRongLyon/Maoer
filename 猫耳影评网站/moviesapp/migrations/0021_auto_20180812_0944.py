# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-12 01:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('moviesapp', '0020_auto_20180812_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviesinfo',
            name='tag_for',
            field=models.ManyToManyField(blank=True, max_length=10, null=True, related_name='moviesinfo_set', to='moviesapp.Tag', verbose_name='分类标签外键'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='movie_for',
            field=models.ForeignKey(blank=True, max_length=128, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews_set', to='moviesapp.MoviesInfo', verbose_name='对应电影外键'),
        ),
    ]
