# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-13 22:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlecategory',
            name='code',
            field=models.CharField(default='', help_text='类别code', max_length=30, unique=True, verbose_name='类别code'),
        ),
        migrations.AlterField(
            model_name='articlecategory',
            name='name',
            field=models.CharField(default='', max_length=20, unique=True, verbose_name='文章分类名称'),
        ),
    ]