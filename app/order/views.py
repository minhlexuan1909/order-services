from django.shortcuts import render

from .models import Order, OrderItem
from .serializers import (
    OrderSerializer,
    OrderDetailSerializer,
    OrderItemSerializer,
    OrderDeliveredSerializer,
)

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from datetime import datetime


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderDetailSerializer

    def get_queryset(self):
        return self.queryset.filter(account_id=self.request.user.id)

    def get_serializer_class(self):
        """Return the serializer class for request"""
        if self.action == "list":
            return OrderSerializer
        elif self.action == "delivered":
            return OrderDeliveredSerializer
        return self.serializer_class

    def perform_create(self, serializer):
        serializer.save(account_id=self.request.user.id)

    def retrieve(self, request, pk=None):
        order = self.get_object()
        order.order_items = OrderItem.objects.filter(order=order)
        serializer = self.get_serializer(order)
        return Response(serializer.data)

    @action(detail=True, methods=["put"])
    def delivering(self, request, pk=None):
        order = self.get_object()
        order.order_status = "DELIVERING"
        order.save()
        return Response(status=status.HTTP_200_OK)

    @action(detail=True, methods=["put"])
    def delivered(self, request, pk=None):
        order = self.get_object()
        order.order_status = "DELIVERED"
        order.shipped_date = datetime.now()
        order.save()
        return Response(status=status.HTTP_200_OK)


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

    def get_queryset(self):
        return self.queryset

    def perform_create(self, serializer):
        serializer.save()
