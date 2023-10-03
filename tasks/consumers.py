import json
from channels.generic.websocket import AsyncWebsocketConsumer


class TaskConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Add the WebSocket to the group 'task_updates'
        await self.channel_layer.group_add(
            'task_updates',
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Remove the WebSocket from the group 'task_updates' upon disconnection
        await self.channel_layer.group_discard(
            'task_updates',
            self.channel_name
        )

    async def receive(self, text_data):
        # For now, just logging received data. You can expand this as needed.
        print(f"Received: {text_data}")

    # Handler for 'task.update' type messages
    async def task_update(self, event):
        # Send the message content to the WebSocket
        await self.send(text_data=json.dumps(event['message']))