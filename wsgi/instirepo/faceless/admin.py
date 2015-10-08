from django.contrib import admin

from .models import *

admin.site.register(Teams)
admin.site.register(UserProfiles)
admin.site.register(Channels)
admin.site.register(ChannelUnsubscriptions)
admin.site.register(Posts)
admin.site.register(Polls)
admin.site.register(PollsChoices)
admin.site.register(Upvotes)
admin.site.register(Comments)
admin.site.register(Flags)
admin.site.register(PollsAnswers)
admin.site.register(Chats)
