# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-12-19 07:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_contact_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='profile_image',
            field=models.ImageField(blank=True, upload_to='profile_image_field'),
        ),
    ]
