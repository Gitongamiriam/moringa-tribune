# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-02-06 08:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20200206_1056'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Editor',
        ),
        migrations.RemoveField(
            model_name='article',
            name='editor',
        ),
        migrations.AlterField(
            model_name='article',
            name='article_image',
            field=models.ImageField(upload_to='articles/'),
        ),
    ]