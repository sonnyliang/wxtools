from django.urls import include, path

from .views import OrderViewSet, Gauge
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('getOrder', OrderViewSet)

urlpatterns =[
    path('api/', include(router.urls)),
    path('api/gauge/', Gauge.as_view()),
]