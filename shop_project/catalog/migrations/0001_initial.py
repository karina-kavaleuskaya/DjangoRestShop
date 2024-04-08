# Generated by Django 5.0.3 on 2024-03-25 17:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cashback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percent', models.PositiveIntegerField()),
                ('treshold', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('percent', models.PositiveIntegerField()),
                ('date_start', models.DateTimeField()),
                ('date_end', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Promocode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_start', models.DateTimeField()),
                ('percent', models.PositiveIntegerField()),
                ('date_end', models.DateTimeField()),
                ('is_cumulative', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('contact', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('total_sum', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(choices=[('In process', 'In Process'), ('Packed', 'Packed'), ('On the way', 'On the way'), ('Delivered', 'Delivered'), ('Recived', 'Recived'), ('Refused', 'Refused')], max_length=100)),
                ('delivery_address', models.CharField(blank=True, max_length=250, null=True)),
                ('delivery_method', models.CharField(choices=[('Courier', 'Courier'), ('Post', 'Post'), ('Self-delivery', 'Self-delivery')], max_length=100)),
                ('payment_method', models.CharField(choices=[('Card Online', 'Card Online'), ('Card Offline', 'Card Offline'), ('Cash', 'Cash')], max_length=100)),
                ('payment_status', models.CharField(choices=[('Paid', 'Paid'), ('In process', 'In process'), ('Cancelled', 'Cancelled')], default='In process', max_length=100)),
                ('delivery_notification_before', models.PositiveIntegerField(choices=[(24, 24), (6, 6), (1, 1)], default=6)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('article', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('count_on_stock', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.category')),
                ('discount', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.discount')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.seller')),
            ],
        ),
        migrations.CreateModel(
            name='OrderProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.product')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product_images/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.product')),
            ],
        ),
    ]
