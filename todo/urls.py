from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.TaskListView.as_view(), name='task-list'),
    path('create/', views.TaskCreateView.as_view(), name='task-create'),
    path('delete/<int:pk>/', views.TaskDeleteView.as_view(), name='task-delete'),
    path('finish/<int:pk>/', views.TaskEditView.as_view(), name='task-edit'),
]