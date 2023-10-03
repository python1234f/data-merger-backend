from django.urls import re_path
from tasks import consumers

websocket_urlpatterns = [
    re_path(r'tasks/$', consumers.TaskConsumer.as_asgi()),
]