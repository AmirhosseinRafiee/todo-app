from rest_framework import serializers
from ...models import Task

class TaskSerializer(serializers.ModelSerializer):
    relative_url = serializers.URLField(source='get_absolute_api_url')
    class Meta:
        model = Task
        fields = ('id', 'user', 'title', 'is_completed', 'relative_url','created_date', 'updated_date')
