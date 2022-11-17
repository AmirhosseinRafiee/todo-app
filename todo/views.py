# from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Task

class TaskListView(ListView):
    template_name = 'task_list.html'

    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)