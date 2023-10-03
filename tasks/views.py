from rest_framework import viewsets, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from .models import Task
from .tasks import long_running_task
from .serializers import TaskSerializer, TaskCreateSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return TaskCreateSerializer
        return super().get_serializer_class()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        id = serializer.validated_data.get('id')

        # Check if the ID already exists
        if Task.objects.filter(id=id).exists():
            raise ValidationError({'id': ['A task with this ID already exists.']})

        task = long_running_task.delay(id)

        # Create the Task instance after the celery task is launched
        task_instance = Task.objects.create(id=id, celery_id=task.id)

        # Return the task_instance using the serializer
        serializer = self.get_serializer(task_instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)