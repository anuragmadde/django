# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-18 17:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_blog_read_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.TextField(),
        ),
    ]
