# Generated by Django 5.0.3 on 2024-04-08 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_cart_count_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promocode',
            name='date_end',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='promocode',
            name='date_start',
            field=models.DateField(),
        ),
    ]