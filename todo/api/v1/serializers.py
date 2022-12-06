from rest_framework import serializers
from ...models import Task

class TaskSerializer(serializers.ModelSerializer):
    relative_url = serializers.URLField(source='get_absolute_api_url', read_only=True)
    absolute_url = serializers.SerializerMethodField()
    class Meta:
        model = Task
        fields = ('id', 'user', 'title', 'is_completed', 'relative_url', 'absolute_url','created_date', 'updated_date')
        read_only_fields = ('user',)
    
    def get_absolute_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.pk)

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        request = self.context.get('request')
        if request.parser_context.get('kwargs').get('pk'):
            rep.pop('relative_url', None)
            rep.pop('absolute_url', None)
        else:
            rep.pop('created_date', None)
        return rep


    def create(self, validated_data):
        validated_data['user'] = self.context.get('request').user
        return super().create(validated_data)