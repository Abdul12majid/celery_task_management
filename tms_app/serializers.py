from rest_framework import serializers
from .models import Task, Notification
from django.contrib.auth.models import User

class TaskSerializer(serializers.ModelSerializer):
    assigned_to = serializers.ReadOnlyField(source='assigned_to.username')
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'assigned_to', 'priority', 'status', 'due_date', 'created_at', 'updated_at']


class NotificationSerializer(serializers.ModelSerializer):
    task = TaskSerializer()
    class Meta:
        model = Notification
        fields = ['user', 'task', 'message', 'read', 'created_at']
