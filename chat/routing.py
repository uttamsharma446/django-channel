from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'chat/$', consumers.TestConsumer.as_asgi()),
    re_path(r'newChate/$', consumers.NewConsumer.as_asgi()),
]