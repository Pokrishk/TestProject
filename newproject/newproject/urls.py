"""
URL configuration for newproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from hello.views import index
from hello.views import cart
from hello.views import catalog
from hello.views import company
from hello.views import register_view, login_view, logout_view, cart_view, add_to_cart, clear_cart, increase_quantity, decrease_quantity, make_order

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('company.html', company, name='company'),
    path('catalog.html', catalog, name='catalog'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('cart/', cart_view, name='cart_view'),
    path('add_to_cart/<int:book_id>/', add_to_cart, name='add_to_cart'),
    path('clear_cart/', clear_cart, name='clear_cart'),
     path('cart/increase/<int:cartitem_id>/', increase_quantity, name='increase_quantity'),
    path('cart/decrease/<int:cartitem_id>/', decrease_quantity, name='decrease_quantity'),
    path('make_order/', make_order, name='make_order'),
    path('api/', include('api_shop.urls'))
]
