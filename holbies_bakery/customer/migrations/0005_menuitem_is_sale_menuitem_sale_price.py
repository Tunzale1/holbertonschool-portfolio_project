# Generated by Django 4.2 on 2024-06-27 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_alter_orderitem_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='is_sale',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='sale_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]