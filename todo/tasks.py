from celery import shared_task
from .models import Task

@shared_task
def delete_finished_tasks():
    Task.objects.filter(is_completed=True).delete()
