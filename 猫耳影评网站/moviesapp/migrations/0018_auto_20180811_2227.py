# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-11 14:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moviesapp', '0017_auto_20180811_1555'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='moviesinfo',
            options={'ordering': ['-score'], 'verbose_name': '电影信息', 'verbose_name_plural': '电影信息'},
        ),
    ]
