# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faceless', '0003_auto_20151012_0158'),
    ]

    operations = [
        migrations.AddField(
            model_name='chats',
            name='user_profile_id',
            field=models.ForeignKey(to='faceless.UserProfiles', null=True),
        ),
        migrations.AlterField(
            model_name='comments',
            name='poll_id',
            field=models.ForeignKey(null=True, blank=True, to='faceless.Polls'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='post_id',
            field=models.ForeignKey(null=True, blank=True, to='faceless.Posts'),
        ),
        migrations.AlterField(
            model_name='upvotes',
            name='poll_id',
            field=models.ForeignKey(null=True, blank=True, to='faceless.Polls'),
        ),
        migrations.AlterField(
            model_name='upvotes',
            name='post_id',
            field=models.ForeignKey(null=True, blank=True, to='faceless.Posts'),
        ),
    ]
