from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register('categories', CategoryViewSet, basename='categories')


urlpatterns = [
    path('', include(router.urls)),
]
