from django.urls import include, path
from . import views
from .views import getList, addTodo, getListName

from .routers import StandardRouter


app_name = 'todo'

router = StandardRouter()



router.register('getTodo', getList)
router.register('getListName', getListName)
urlpatterns = [

    path("api/", include(router.urls)),
    path("api/auth/", include("rest_framework.urls")),

    path('api/get_list/', getList.as_view({'get': 'list'})),
    path('api/add_todo/', addTodo.as_view()),
    
]