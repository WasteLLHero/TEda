# Generated by Django 4.2 on 2023-04-30 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_category_dish_order_remove_orders_user_delete_tokens_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_dish',
            name='count',
            field=models.IntegerField(default=1),
        ),
    ]