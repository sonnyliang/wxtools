from django.urls import include, path

from .views import PostViewSet
from rest_framework.routers import DefaultRouter
 
router = DefaultRouter()
router.register('getPost', PostViewSet)

# app_name = "blog"
urlpatterns = [

    path("api/", include(router.urls)),
    path("api/auth/", include("rest_framework.urls")),
    
]
