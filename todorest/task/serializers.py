from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task


class UserSerializer(serializers.HyperlinkedModelSerializer):
    tasks = serializers.HyperlinkedRelatedField(many=True, view_name='task-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'pk', 'username', 'tasks')


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    queue = serializers.ReadOnlyField(source='Task.queue')

    class Meta:
        model = Task
        fields = ('url', 'pk', 'task', 'queue', 'owner')

