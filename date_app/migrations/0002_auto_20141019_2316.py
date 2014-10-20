# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('date_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dater',
            name='profile_image',
        ),
        migrations.AddField(
            model_name='image',
            name='profile_image',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
