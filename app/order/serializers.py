from rest_framework import serializers

from .models import Order, OrderItem


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            "id",
            "account_id",
            "order_date",
            "shipped_date",
            "total_value",
            "order_status",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("id", "account_id", "total_value", "created_at", "updated_at")


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"
        read_only_fields = ("id", "created_at", "updated_at")

    def create(self, validated_data):
        order = validated_data["order"]
        order.total_value += validated_data["quantity"] * validated_data["price"]
        order.save()

        return super().create(validated_data)


class OrderDetailSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)

    class Meta(OrderSerializer.Meta):
        fields = OrderSerializer.Meta.fields + ("order_items",)


class OrderDeliveredSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("id",)
        read_only_fields = ("id",)
