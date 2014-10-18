# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('date_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='user1',
            field=models.ForeignKey(related_name=b'match_user1', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='match',
            name='user2',
            field=models.ForeignKey(related_name=b'matchmade', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
