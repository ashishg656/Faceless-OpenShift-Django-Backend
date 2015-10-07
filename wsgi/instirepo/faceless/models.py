from django.db import models
from django.contrib.auth.models import User


class Teams(models.Model):
    name = models.CharField(max_length=255)


class UserProfiles(models.Model):
    user_link_obj = models.OneToOneField(User, related_name='user_profile')
    team_id = models.ForeignKey(Teams)
    is_admin = models.BooleanField(default=False)
    is_first_time_login = models.BooleanField(default=True)


class Channels(models.Model):
    company_id = models.ForeignKey(Teams)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)


class ChannelUnsubscriptions(models.Model):
    channel_id = models.ForeignKey(Channels)
    user_id = models.ForeignKey(UserProfiles)
    is_active = models.BooleanField(default=True)


class Posts(models.Model):
    heading = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to='posts_images', max_length=255, null=True, blank=True)


class Polls(models.Model):
    heading = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to='polls_images', max_length=255, null=True, blank=True)


class PollsChoices(models.Model):
    choice = models.TextField()
    poll_id = models.ForeignKey(Polls)


class Upvotes(models.Model):
    user_id = models.ForeignKey(UserProfiles)
    post_id = models.ForeignKey(Posts)
    poll_id = models.ForeignKey(Polls)
    is_active = models.BooleanField(default=True)
    is_upvote = models.BooleanField(default=True)


class Comments(models.Model):
    post_id = models.ForeignKey(Posts)
    poll_id = models.ForeignKey(Polls)
    comment = models.TextField()
    time = models.DateTimeField(auto_now=True)


class Flags(models.Model):
    post_id = models.ForeignKey(Posts)
    poll_id = models.ForeignKey(Polls)
    user_id = models.ForeignKey(UserProfiles)


class PollsAnswers(models.Model):
    user_id = models.ForeignKey(UserProfiles)
    choice = models.ForeignKey(PollsChoices)
    poll_id = models.ForeignKey(Polls)
