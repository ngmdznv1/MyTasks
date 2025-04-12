from rest_framework import serializers
from MyTasks.models import Task
from django.contrib.auth.models import User

class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('pk', 'title', 'description', 'created_at', 'due_date', 'is_completed')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user