# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-12-19 09:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_customuser_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='profile_image',
        ),
        migrations.AddField(
            model_name='customuser',
            name='image',
            field=models.ImageField(default='D:\\\\intro-pbn\\\\python\\\\PersonalDashborad\\\\media\\\\panda.jpg', upload_to='media'),
        ),
    ]
