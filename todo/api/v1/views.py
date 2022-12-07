from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from ...models import Task
from .serializers import TaskSerializer
from .paginations import DefaultPagination

class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['is_completed']
    search_fields = ['title']
    ordering_fields = ['created_date', 'updated_date']
    pagination_class = DefaultPagination

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)