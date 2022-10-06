import os

import django
from channels.http import AsgiHandler
from channels.routing import ProtocolTypeRouter,URLRouter
from django.urls import path
from chat import consumers
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()


ws_pattern=[
    path('test/',consumers.TestConsumer.as_asgi())
]
application = ProtocolTypeRouter({
  "http": AsgiHandler(),
  'websocket':URLRouter(ws_pattern)
  ## IMPORTANT::Just HTTP for now. (We can add other protocols later.)
})

