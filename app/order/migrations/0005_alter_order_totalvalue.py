# Generated by Django 3.2.18 on 2023-03-24 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_auto_20230324_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='totalValue',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=15),
        ),
    ]
