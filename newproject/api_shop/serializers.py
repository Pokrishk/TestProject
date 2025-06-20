from rest_framework import serializers
from .models import (
    Book, Role, UserAccount, Cart, CartItem, OrderStatus,
    DeliveryMethod, Publisher, Format, Author, Genre,
    BookGenres, OrderTable, OrderItem
)

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            'title', 'description', 'stockquantity', 'language', 'pagecount',
            'authorid', 'publisherid', 'price', 'publicationdate', 'agerestriction'
        ]

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['name']

class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = [
            'firstname', 'lastname', 'middlename', 'email',
            'password', 'role', 'last_login', 'is_superuser',
            'is_staff', 'is_active'
        ]

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['user']

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['cart', 'book', 'quantity']

class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatus
        fields = ['name', 'description']

class DeliveryMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryMethod
        fields = ['name', 'description', 'address']

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['name', 'country', 'description']

class FormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Format
        fields = ['name', 'description']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['firstname', 'lastname', 'middlename', 'country', 'description']

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name', 'description']

class BookGenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookGenres
        fields = ['genre', 'book']

class OrderTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderTable
        fields = ['user', 'totalamount', 'orderdate', 'orderstatus', 'deliverymethod']

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['order', 'book', 'quantity']
