from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ChartViewSet

router = DefaultRouter()
router.register(r'charts', ChartViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
