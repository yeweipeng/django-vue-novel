# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-02 14:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20180602_1039'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookliketab',
            name='book_desc',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AddField(
            model_name='bookliketab',
            name='book_img_url',
            field=models.CharField(default='', max_length=256),
        ),
    ]
