"""
URL mappings for the order app
"""

from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import OrderViewSet, OrderItemViewSet

router = DefaultRouter()
router.register("order", OrderViewSet)
router.register("order-item", OrderItemViewSet)

app_name = "order"

urlpatterns = [
    path("", include(router.urls)),
]
