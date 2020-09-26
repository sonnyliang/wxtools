from django.shortcuts import render

# Create your views here.
from .serializers import OrderSerializer
from .models import BusinessOrder

from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend

# 计算模块
import pandas as pd
from django.db.models import Q

# 解析器
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

class OrderViewSet(viewsets.GenericViewSet, mixins.ListModelMixin,mixins.RetrieveModelMixin, mixins.UpdateModelMixin,mixins.DestroyModelMixin,mixins.CreateModelMixin):
    serializer_class = OrderSerializer
    queryset = BusinessOrder.objects.all()
    pagination_class = PageNumberPagination
    permission_classes = [AllowAny]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['billdate1','brand']

class Gauge(APIView):
    parser_classes = [JSONParser, ]

    def get(self, request, *args, **kwargs):

        params= dict(request.query_params)
        print('接收到参数：'+str(params))

        brand = params['brand'][0]

        data =BusinessOrder.objects.filter( Q(brand__exact=brand) & Q(billdate1__gte='2020-08-01') & Q(billdate1__lte='2020-08-03')).values("amount")

        data = pd.DataFrame(data)
        
        data['amount'] = data['amount'].apply(float)
        salesVolumn = data['amount'].sum()
        result = salesVolumn / 500890488

        return Response(result)