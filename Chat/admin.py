from django.contrib import admin
from Chat.models import Thread, Message


class MessageTabularInline(admin.TabularInline):
    model = Message
    readonly_fields = (
        'text',
        'created',
        'is_read',
        'thread',
        'sender'
    )


@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    list_display = (
        'participants',
        'created',
        'updated',
    )
    inlines = (MessageTabularInline,)
    readonly_fields = ['participants']
