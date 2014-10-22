# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('date_app', '0004_merge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='profile_image',
        ),
        migrations.AlterField(
            model_name='dater',
            name='profile_image',
            field=models.ImageField(upload_to=b'profile_pictures'),
        ),
    ]
