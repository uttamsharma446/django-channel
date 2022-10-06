import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class TestConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name='test_consumer'
        self.room_group__name='test_consumer_group'
        async_to_sync(self.channel_layer.group_add)(self.room_group__name,self.channel_name)
        self.accept()
        self.send(text_data=json.dumps({'status':'connected'}))
    def receive(self,text_data):
        print(text_data)
        self.send(text_data=json.dumps(text_data))
    def disconnect(self,*args, **kwargs):
        print(self)

    def send_notification(self,event):
        print('SELF',self)
        data=event['value']
        self.send(text_data=data)