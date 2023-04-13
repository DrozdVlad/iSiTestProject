from rest_framework import serializers

from Chat.models import Thread, Message


class ThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thread
        fields = [
            'id',
            'participants',
            'created',
            'updated'
        ]
        read_only_fields = ('id',)


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = [
            'text',
            'created',
            'is_read',
            'thread',
            'sender'
        ]
