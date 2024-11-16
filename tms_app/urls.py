from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'notifications', NotificationViewSet)



urlpatterns = [
    #path('', views.index, name="index"),
    path('api/', include(router.urls)),
    
]
