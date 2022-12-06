from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from ...models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)