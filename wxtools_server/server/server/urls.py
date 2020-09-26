"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include, path

from rest_framework import routers

from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings

# 使用xadmin
# import xadmin
# xadmin.autodiscover()
# version模块自动注册需要版本控制的 Model
# from xadmin.plugins import xversion
# xversion.register_models()
 
router = routers.DefaultRouter()
urlpatterns = [
    # path(r'xadmin/', include(xadmin.site.urls)),
    path('admin/', admin.site.urls),

    # path("api/", include(router.urls)),
    # path("api/auth/", include("rest_framework.urls", namespace="rest_framework")),

    path('todo/',include('todo.urls')),
    path('blog/',include('blog.urls')),
    path('bi/',include('bi.urls')),

    url(r'mdeditor/', include('mdeditor.urls'))
]

# if settings.DEBUG:
    # # static files (images, css, javascript, etc.)
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
