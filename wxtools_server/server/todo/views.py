from django.shortcuts import render
from rest_framework.response import Response

from .models import todoList,todoListCollect
from .serializers import todoListSerializer, todoListCollectSerializer

from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import mixins, viewsets

from .task import dosomething

# Create your views here.
class getList(viewsets.GenericViewSet, mixins.ListModelMixin,mixins.RetrieveModelMixin, mixins.UpdateModelMixin,mixins.DestroyModelMixin,mixins.CreateModelMixin):
    queryset = todoList.objects.all()
    serializer_class = todoListSerializer
    pagination_class = PageNumberPagination
    permission_classes = [AllowAny] 

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'todoType']

class getListName(viewsets.GenericViewSet, mixins.ListModelMixin,mixins.RetrieveModelMixin, mixins.UpdateModelMixin,mixins.DestroyModelMixin,mixins.CreateModelMixin):
    queryset = todoListCollect.objects.all()
    serializer_class = todoListCollectSerializer
    pagination_class = PageNumberPagination
    permission_classes = [AllowAny] 



class addTodo(APIView):

    def post(self, request, *args, **kwargs):

        params = dict(request.query_params)

        add_todo = todoList.objects.create(user=params['user'][0], todo=params['todo'][0], todoType=params['todoType'][0])

        add_todo.save()

        return Response('成功添加')

# class celeryTask(request):
    # 启动异步任务
    # dosomething.delay(request)

