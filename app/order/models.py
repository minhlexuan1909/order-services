from django.db import models

# Create your models here.

ORDER_STATUS = [
    ("PENDING", "PENDING"),
    ("DELIVERING", "DELIVERING"),
    ("DELIVERED", "DELIVERED"),
]


class Order(models.Model):
    account_id = models.IntegerField()
    order_date = models.DateTimeField()
    shipped_date = models.DateTimeField(blank=True, null=True)
    total_value = models.DecimalField(default=0.0, max_digits=15, decimal_places=2)
    order_status = models.CharField(max_length=15, default="PENDING", choices=ORDER_STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.id} - {self.order_status}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.IntegerField()
    quantity = models.IntegerField()
    price = models.DecimalField(default=0.0, max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order Item {self.id} - {self.order}"
