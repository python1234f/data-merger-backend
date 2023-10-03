from django.db import models


class Task(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    celery_id = models.CharField(max_length=255, unique=True)
    STATUS_CHOICES = [
        ('RUNNING', 'Running'),
        ('SUCCESS', 'Success'),
        ('FAILURE', 'Failure')
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='RUNNING')
