from rest_framework import serializers
from MyTasks.models import Task

class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('pk', 'title', 'created_at', 'due_date', 'is_completed')