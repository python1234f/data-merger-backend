# from channels.routing import ProtocolTypeRouter, ChannelNameRouter
# from tasks import consumers
#
# application = ProtocolTypeRouter({
#     "websocket": consumers.TaskConsumer.as_asgi(),
# })


from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from tasks.consumers import TaskConsumer
application = ProtocolTypeRouter({
    'websocket': URLRouter([
        path('ws/tasks/', TaskConsumer.as_asgi()),
    ])
})