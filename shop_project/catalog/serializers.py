from rest_framework import serializers
from catalog.models import Category, Product, ProductImage, Seller, Discount, Order, OrderProducts


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name', 'description')


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('image', )

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, source='productimage_set')

    class Meta:
        model = Product
        fields = ('id', 'article', 'name', 'price', 'images')


class SellerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Seller
        fields = ('id', 'name', 'description', 'contact')


class DiscountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Discount
        fields = ('id', 'name', 'percent', 'date_start', 'date_end')

class AddProductSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    count = serializers.IntegerField()


class ProductInCartSerializer(serializers.Serializer):
    name = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    count = serializers.IntegerField()
    discount_percent = serializers.IntegerField()


class CartSerializer(serializers.Serializer):
    products = ProductInCartSerializer(many=True)
    result_price = serializers.SerializerMethodField()

    def get_result_price(self, data):
        result_price = 0
        for product in data.get('products'):
            price = product.get('price')
            count = product.get('count')
            if product.get('discount'):
                discount_data_end = product.get('discount_data_end')
                date_today = date.today()
                delta = date_today - discount_data_end
                if delta.days <= 0:
                    discount_percent = product.get(discount_percent)
                    result_price += (price * (100 - discount_percent) / 100) * count
                else:
                    result_price += price * count

            else:
                result_price += price * count
        return result_price


class DeleteProductSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()


class OrderProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderProducts
        fields = ('product', 'count')


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('created_at', 'delivery_address', 'delivery_method', 'payment_method', 'payment_status',
                  'total_sum', 'staus', 'delivery_notification_before', 'products', 'promocode', 'use_cashback')