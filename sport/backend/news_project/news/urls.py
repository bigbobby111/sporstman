from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NewsItemViewSet

router = DefaultRouter()
router.register(r'news', NewsItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
