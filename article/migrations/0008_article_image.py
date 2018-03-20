# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-19 09:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_article_hit_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(default='', max_length=300, upload_to='article/images/', verbose_name='文章图片'),
        ),
    ]