import json
from channels.generic.websocket import WebsocketConsumer,AsyncJsonWebsocketConsumer
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
class NewConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.room_name='new_consumer'
        self.room_group__name='new_consumer_group'
        await (self.channel_layer.group_add)(self.room_group__name,self.channel_name)
        await self.accept()
        await self.send(text_data=json.dumps({'status':'connected from new consumer'}))
    async def receive(self,text_data):
        print(text_data)
        print("Hii")
        await  self.send(text_data=json.dumps(text_data))
    async def disconnect(self,*args, **kwargs):
        await print(self)


    async def send_notification(self,event):
        print('SELF',self)
        data=event['value']
        await self.send(text_data=data)