# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faceless', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chats',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('message', models.TextField(null=True)),
                ('time', models.DateTimeField(null=True, auto_now=True)),
                ('channel_id', models.ForeignKey(null=True, to='faceless.Channels')),
            ],
        ),
    ]
