# serializers.py

from rest_framework import serializers
from .models import Task


class TaskCreateSerializer(serializers.Serializer):
    id = serializers.CharField(required=True)


class TaskSerializer(serializers.ModelSerializer):
    celery_id = serializers.CharField(read_only=True)
    status = serializers.ChoiceField(choices=Task.STATUS_CHOICES, default='RUNNING', read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'celery_id', 'status']