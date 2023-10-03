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
        print("\n\n\n\n1111111111111")

        id = serializer.validated_data.get('id')

        # Check if the ID already exists
        if Task.objects.filter(id=id).exists():
            raise ValidationError({'id': ['A task with this ID already exists.']})


        task = long_running_task.delay(id)

        # Create the Task instance after the celery task is launched
        task_instance = Task.objects.create(id=id, celery_id=task.id)

        response_serializer = TaskSerializer(data={
            "id": task_instance.id,
            "status": task_instance.status
        })

        if not response_serializer.is_valid():
            return Response(response_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        response_data = {"id": task_instance.id, **response_serializer.data}

        return Response(response_data, status=status.HTTP_201_CREATED)