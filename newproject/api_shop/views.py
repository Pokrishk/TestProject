from rest_framework import viewsets
from .permission import *
from hello.models import *
from .serializers import *

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage

class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage

class UserAccountViewSet(viewsets.ModelViewSet):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage

class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage

class OrderTableViewSet(viewsets.ModelViewSet):
    queryset = OrderTable.objects.all()
    serializer_class = OrderTableSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage

class DeliveryMethodViewSet(viewsets.ModelViewSet):
    queryset = DeliveryMethod.objects.all()
    serializer_class = DeliveryMethodSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage

class FormatViewSet(viewsets.ModelViewSet):
    queryset = Format.objects.all()
    serializer_class = FormatSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage

class OrderStatusViewSet(viewsets.ModelViewSet):
    queryset = OrderStatus.objects.all()
    serializer_class = OrderStatusSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage

class BookGenresViewSet(viewsets.ModelViewSet):
    queryset = BookGenres.objects.all()
    serializer_class = BookGenresSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage
