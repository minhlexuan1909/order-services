# Generated by Django 3.2.18 on 2023-03-24 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_alter_order_orderstatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='orderStatus',
            field=models.CharField(choices=[('PENDING', 'PENDING'), ('DELIVERING', 'DELIVERING'), ('DELIVERED', 'DELIVERED')], default='PENDING', max_length=15),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
