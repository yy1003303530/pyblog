# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-19 08:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_article_is_hot'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='hit_num',
            field=models.IntegerField(default=0, verbose_name='文章点击量'),
        ),
    ]
