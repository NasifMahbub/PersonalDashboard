# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-12-19 09:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20191219_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pic'),
        ),
    ]