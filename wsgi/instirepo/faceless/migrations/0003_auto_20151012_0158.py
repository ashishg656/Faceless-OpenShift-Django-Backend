# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faceless', '0002_chats'),
    ]

    operations = [
        migrations.AddField(
            model_name='polls',
            name='date_created',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='polls',
            name='team_id',
            field=models.ForeignKey(to='faceless.Teams', null=True),
        ),
        migrations.AddField(
            model_name='posts',
            name='date_created',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='posts',
            name='team_id',
            field=models.ForeignKey(to='faceless.Teams', null=True),
        ),
    ]
