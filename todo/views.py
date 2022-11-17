# from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Task

class TaskListView(ListView):
    template_name = 'todo/task_list.html'

    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskCreateView(CreateView):
    model = Task
    fields = ('title',)
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskDeleteView(DeleteView):
    model = Task
    success_url = '/'


class TaskCompleteView(UpdateView):
    model = Task
    fields = ('is_completed',)
    success_url = '/'

class TaskEditView(UpdateView):
    template_name = 'todo/task_edit.html'
    model = Task
    fields = ('title',)
    success_url = '/'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        pk = self.kwargs.get(self.pk_url_kwarg)
        task = Task.objects.filter(user= self.request.user, id=pk)
        context['tasks'] = task
        return context

