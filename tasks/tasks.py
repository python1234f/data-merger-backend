from celery import shared_task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from traceback import format_exc
import time
import random
import logging
logger = logging.getLogger(__name__)


def custom_round(value, decimals=0):

    value = round(value, 2)
    str_val = str(value)
    if len(str_val) > 4:
        str_val = str_val[:4]

    return float(str_val)


@shared_task(bind=True)
def long_running_task(self, id):
    try:
        progress = 0
        while progress < 1:
            # Sleep for a random duration between 5 to 20 seconds
            time.sleep(random.randint(1, 30)/10)

            # Increase progress by a random value between 0.1 and 0.3
            progress_increment = random.uniform(0.1, 0.3)

            # Ensure progress doesn't exceed 1
            progress = custom_round(min(1, progress + progress_increment))

            # Notify the websocket about the current progress
            notify_progress.delay(id, progress)

        # Task completed successfully
        notify_success.delay(id)

        return id
    except Exception as e:
        notify_failure.delay(id, traceback=format_exc())
        raise e


def send_ws_message(id, status, payload=None):

    channel_layer = get_channel_layer()
    message = {
        'type': 'task_update',
        'message': {
            "id": id,
            "status": status,
        }
    }
    if payload:
        message['message']['payload'] = payload

    # Push a message to the frontend
    async_to_sync(channel_layer.group_send)(
        'task_updates',  # This is the group name, can be set dynamically when frontend connects
        message
    )


@shared_task(bind=True)
def notify_progress(self, id, progress):
    send_ws_message(id, 'PROGRESS', {'progress': progress})


@shared_task(bind=True)
def notify_success(self, id):
    send_ws_message(id, 'SUCCESS')


@shared_task(bind=True)
def notify_failure(self, id, traceback):
    send_ws_message(id, f"FAILURE {traceback}")
