from celery import shared_task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .models import Task
import time
import random


@shared_task(bind=True)
def long_running_task(self, id):
    print("\n\n\n\n1111111111111")
    time.sleep(random.randint(5, 150))
    print("\n\n\n\n2222222222222")

    return id


def send_ws_message(id, status):
    print("\n\n\n\n333333333333")

    channel_layer = get_channel_layer()
    # Push a message to the frontend
    async_to_sync(channel_layer.group_send)(
        'task_updates',  # This is the group name, can be set dynamically when frontend connects
        {
            'type': 'task.update',
            'message': {
                "id": id,
                "status": status
            }
        }
    )


@shared_task(bind=True)
def notify_success(id):
    task = Task.objects.get(id=id)
    task.status = 'SUCCESS'
    task.save()
    send_ws_message(id, 'SUCCESS')


@shared_task(bind=True)
def notify_failure(id):
    task = Task.objects.get(id=id)
    task.status = 'FAILURE'
    task.save()
    send_ws_message(id, 'FAILURE')