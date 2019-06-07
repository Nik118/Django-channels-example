from django.db import models
from asgiref.sync import async_to_sync
from chat.notify import push_data
# Create your models here.


class Room(models.Model):
    name = models.TextField()
    label = models.SlugField(unique=True)


class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages',
                             on_delete=models.CASCADE)
    handle = models.TextField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        ret = super().save(*args, **kwargs)
        async_to_sync(push_data)()
        return ret

    def delete(self, *args, **kwargs):
        ret = super().delete(*args, **kwargs)
        async_to_sync(push_data)()
        return ret
