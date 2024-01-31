from rest_framework import serializers

from apps.task.models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task 
        fields = "__all__"

class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'completed')