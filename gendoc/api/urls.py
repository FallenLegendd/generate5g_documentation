from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TerminalViewSet

router = DefaultRouter()
router.register(r'terminals', TerminalViewSet)

urlpatterns = [
    path('', include(router.urls)),
]