from channels.routing import ProtocolTypeRouter, ChannelNameRouter
from tasks import consumers

application = ProtocolTypeRouter({
    "websocket": consumers.TaskConsumer.as_asgi(),
})