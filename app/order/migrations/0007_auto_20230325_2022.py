# Generated by Django 3.2.18 on 2023-03-25 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_alter_order_shippeddate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='accountId',
            new_name='account_id',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='orderDate',
            new_name='order_date',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='orderStatus',
            new_name='order_status',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='shippedDate',
            new_name='shipped_date',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='totalValue',
            new_name='total_value',
        ),
        migrations.RenameField(
            model_name='orderitem',
            old_name='productId',
            new_name='product_id',
        ),
    ]