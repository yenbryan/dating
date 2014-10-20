# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('date_app', '0002_auto_20141019_2316'),
    ]

    operations = [
        migrations.AddField(
            model_name='dater',
            name='profile_image',
            field=models.ImageField(null=True, upload_to=b'profile_pictures', blank=True),
            preserve_default=True,
        ),
    ]
