from django.contrib import admin
from .models import Task
class TaskAdmin(admin.ModelAdmin):
    model = Task
    list_display = ('user', 'title', 'is_completed', 'updated_date')

admin.site.register(Task, TaskAdmin)
