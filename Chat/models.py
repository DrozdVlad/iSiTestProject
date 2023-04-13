from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.db import models


class Thread(models.Model):
    participants = ArrayField(models.IntegerField(), max_length=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Thread with users {self.participants}'


class Message(models.Model):
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Message from {self.sender}'
