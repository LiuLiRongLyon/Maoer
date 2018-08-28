# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-12 01:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('moviesapp', '0018_auto_20180811_2227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviews',
            name='movie',
        ),
        migrations.AddField(
            model_name='moviesinfo',
            name='critics_num',
            field=models.IntegerField(blank=True, default=10, null=True, verbose_name='影评数'),
        ),
        migrations.AddField(
            model_name='reviews',
            name='movie_char',
            field=models.CharField(default=1, max_length=128, verbose_name='对应电影名称'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reviews',
            name='movie_for',
            field=models.ForeignKey(default=1, max_length=128, on_delete=django.db.models.deletion.CASCADE, related_name='reviews_set', to='moviesapp.MoviesInfo', verbose_name='对应电影外键'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='moviesinfo',
            name='tag',
        ),
        migrations.AddField(
            model_name='moviesinfo',
            name='tag',
            field=models.ManyToManyField(max_length=10, related_name='moviesinfo_set', to='moviesapp.Tag', verbose_name='分类标签'),
        ),
    ]
