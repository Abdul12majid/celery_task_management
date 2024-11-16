from django.shortcuts import render
from rest_framework import viewsets
from .models import Task, Notification
from .serializers import TaskSerializer, NotificationSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from .tasks import send_task_notification
from rest_framework import status
from rest_framework.response import Response

# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post'])
    def send_notification(self, request, pk=None):
        task = self.get_object()
        send_task_notification.delay(task.id, task.assigned_to.email)
        print("Notification sent")
        return Response({"message": "Notification sent."}, status=status.HTTP_200_OK)



class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]


