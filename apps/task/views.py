from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from apps.task.models import Task
from apps.task.serializers import TaskSerializer, TaskCreateSerializer

class TaskAPIViewSet(GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_serializer_class(self):
        if self.action == "create":
            return TaskCreateSerializer
        return TaskSerializer