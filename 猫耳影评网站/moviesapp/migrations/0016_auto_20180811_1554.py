# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-11 07:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviesapp', '0015_auto_20180811_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviesinfo',
            name='name',
            field=models.TextField(max_length=500, verbose_name='影名'),
        ),
    ]
