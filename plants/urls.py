from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'plants', views.PlantViewSet)

urlpatterns = [
    
    path("get_schedule/", views.get_schedule),
    path('', include(router.urls))
]