from rest_framework import serializers
from .models import todoList, todoListCollect

class todoListSerializer(serializers.ModelSerializer):

    class Meta:
        model=todoList
        fields = [
            'id',
            'user',
            'todo',
            'todoType',
            'create_time',
            'update_time',
        ]

class todoListCollectSerializer(serializers.ModelSerializer):

    class Meta:
        model=todoListCollect
        fields = [
            'id',
            'listName',
        ]