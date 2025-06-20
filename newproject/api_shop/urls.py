from django.urls import path
from rest_framework import routers
from .views import *

urlpatterns = [
    
]

router = routers.SimpleRouter()
router.register('books', BookViewSet, basename='books')
router.register('authors', AuthorViewSet, basename='authors')
router.register('publishers', PublisherViewSet, basename='publishers')
router.register('genres', GenreViewSet, basename='genres')
router.register('users', UserAccountViewSet, basename='users')
router.register('carts', CartViewSet, basename='carts')
router.register('cart-items', CartItemViewSet, basename='cart-items')
router.register('orders', OrderTableViewSet, basename='orders')
router.register('order-items', OrderItemViewSet, basename='order-items')
router.register('delivery-methods', DeliveryMethodViewSet, basename='delivery-methods')
router.register('formats', FormatViewSet, basename='formats')
router.register('roles', RoleViewSet, basename='roles')
router.register('order-statuses', OrderStatusViewSet, basename='order-statuses')
router.register('book-genres', BookGenresViewSet, basename='book-genres')

urlpatterns += router.urls
