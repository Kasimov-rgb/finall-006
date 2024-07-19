# Generated by Django 5.0.3 on 2024-07-19 12:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0003_alter_item_basket_alter_item_product'),
        ('products', '0002_rename_c_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='basket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items_basket', to='basket.basket', verbose_name='Корзина'),
        ),
        migrations.AlterField(
            model_name='item',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='basket_item', to='products.product', verbose_name='Продукт'),
        ),
    ]