# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Channels',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ChannelUnsubscriptions',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('is_active', models.BooleanField(default=True)),
                ('channel_id', models.ForeignKey(to='faceless.Channels')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('comment', models.TextField()),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Flags',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Polls',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('heading', models.TextField()),
                ('description', models.TextField()),
                ('image', models.ImageField(max_length=255, upload_to='polls_images', blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PollsAnswers',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='PollsChoices',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('choice', models.TextField()),
                ('poll_id', models.ForeignKey(to='faceless.Polls')),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('heading', models.TextField()),
                ('description', models.TextField()),
                ('image', models.ImageField(max_length=255, upload_to='posts_images', blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Upvotes',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_upvote', models.BooleanField(default=True)),
                ('poll_id', models.ForeignKey(to='faceless.Polls')),
                ('post_id', models.ForeignKey(to='faceless.Posts')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfiles',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_first_time_login', models.BooleanField(default=True)),
                ('team_id', models.ForeignKey(to='faceless.Teams')),
                ('user_link_obj', models.OneToOneField(related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='upvotes',
            name='user_id',
            field=models.ForeignKey(to='faceless.UserProfiles'),
        ),
        migrations.AddField(
            model_name='pollsanswers',
            name='choice',
            field=models.ForeignKey(to='faceless.PollsChoices'),
        ),
        migrations.AddField(
            model_name='pollsanswers',
            name='poll_id',
            field=models.ForeignKey(to='faceless.Polls'),
        ),
        migrations.AddField(
            model_name='pollsanswers',
            name='user_id',
            field=models.ForeignKey(to='faceless.UserProfiles'),
        ),
        migrations.AddField(
            model_name='flags',
            name='poll_id',
            field=models.ForeignKey(to='faceless.Polls'),
        ),
        migrations.AddField(
            model_name='flags',
            name='post_id',
            field=models.ForeignKey(to='faceless.Posts'),
        ),
        migrations.AddField(
            model_name='flags',
            name='user_id',
            field=models.ForeignKey(to='faceless.UserProfiles'),
        ),
        migrations.AddField(
            model_name='comments',
            name='poll_id',
            field=models.ForeignKey(to='faceless.Polls'),
        ),
        migrations.AddField(
            model_name='comments',
            name='post_id',
            field=models.ForeignKey(to='faceless.Posts'),
        ),
        migrations.AddField(
            model_name='channelunsubscriptions',
            name='user_id',
            field=models.ForeignKey(to='faceless.UserProfiles'),
        ),
        migrations.AddField(
            model_name='channels',
            name='company_id',
            field=models.ForeignKey(to='faceless.Teams'),
        ),
    ]
