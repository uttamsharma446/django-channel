from email.policy import default
import json
from django.db import models
from django.contrib.auth.models import User
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

class Student(models.Model):
    name=models.CharField(max_length=250, null=True,blank=True)
    email=models.CharField(max_length=250, null=True,blank=True)
    address=models.TextField(null=True,blank=True)
    age=models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.name

class Notification(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,blank=True)
    notification=models.TextField(max_length=100)
    is_seen=models.BooleanField(default=False)  
    def __str__(self):
        return self.notification
    def save(self,*args, **kwargs):
        # print("SAVE IS")
        channel_layer=get_channel_layer()
        notifcation_count=Notification.objects.filter(is_seen=False).count()
        data={'count':notifcation_count,'current_notification':self.notification}
        async_to_sync(channel_layer.group_send)('test_consumer_group',{
            'type':'send_notification',
            'value':json.dumps(data)
        })
        super(Notification,self).save(*args,**kwargs)

