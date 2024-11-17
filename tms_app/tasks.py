from celery import shared_task
from .models import Task, Notification
from django.core.mail import send_mail

@shared_task
def send_task_notification(task_id, user_email):
    task = Task.objects.get(id=task_id)
    message = f'The task "{task.title}" is due soon. Please check the task details.'
    
    # Send email (this could be replaced with Slack/Telegram notification)

    print("Task task task")
    #send_mail(
     #   'Task Notification',
      #  message,
       # 'noreply@example.com',
        #[user_email],
        #fail_silently=False,
    #)

    # Optionally, create a notification in the database
    Notification.objects.create(
        user=task.assigned_to,
        task=task,
        message=message,
    )

@shared_task
def test_task():
    print("Example task executed!")
    return "Task completed!"