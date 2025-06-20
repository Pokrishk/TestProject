from django.shortcuts import render, redirect, get_object_or_404
from hello.models import Book
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from .models import Role, Cart, CartItem, OrderStatus, DeliveryMethod, OrderTable, OrderItem
from django.contrib import messages

def index(request):
    return render(request, 'hello/index.html')
def cart(request):
    return render(request, 'hello/cart.html')
def catalog(request):
    books = Book.objects.all()
    return render(request, 'hello/catalog.html', {'books': books})
def company(request):
    return render(request, 'hello/company.html')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.role = Role.objects.get(name='Пользователь')
            user.save()
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'hello/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                return redirect('/')
    else:
        form = LoginForm()
    return render(request, 'hello/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/')

@login_required
def add_to_cart(request, book_id):
    user = request.user
    book = get_object_or_404(Book, pk=book_id)

    cart, created = Cart.objects.get_or_create(user=user)

    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, book=book)
    if not item_created:
        cart_item.quantity += 1 
    cart_item.save()

    return redirect('cart_view')

@login_required
def cart_view(request):
    user = request.user
    try:
        cart = Cart.objects.get(user=user)
        items = CartItem.objects.filter(cart=cart).select_related('book')
    except Cart.DoesNotExist:
        items = []

    context = {'items': items}
    return render(request, 'hello/cart.html', context)

@login_required
def clear_cart(request):
    if request.user.is_authenticated:
        Cart.objects.filter(user=request.user).delete()
    return redirect('cart_view')

@login_required
def increase_quantity(request, cartitem_id):
    cart_item = get_object_or_404(CartItem, pk=cartitem_id, cart__user=request.user)
    if cart_item.quantity < cart_item.book.stockquantity:
        cart_item.quantity += 1
        cart_item.save()
    else:
        messages.warning(request, 'Превышен лимит на складе.')
    return redirect('cart_view')

@login_required
def decrease_quantity(request, cartitem_id):
    cart_item = get_object_or_404(CartItem, pk=cartitem_id, cart__user=request.user)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart_view')

@login_required
def make_order(request):
    user = request.user
    try:
        cart = Cart.objects.get(user=user)
        items = CartItem.objects.filter(cart=cart).select_related('book')
        if not items.exists():
            messages.error(request, "Корзина пуста.")
            return redirect('cart_view')
        

        for item in items:
            if item.quantity > item.book.stockquantity:
                messages.error(request, f"Недостаточно книг: {item.book.title}")
                return redirect('cart_view')

        order_status = OrderStatus.objects.get(name='Новый')
        delivery_method = DeliveryMethod.objects.first() 
        order = OrderTable.objects.create(
            user=user,
            totalamount=sum(item.book.price * item.quantity for item in items),
            orderdate=now().date(),
            orderstatus=order_status,
            deliverymethod=delivery_method
        )

        for item in items:
            OrderItem.objects.create(
                order=order,
                book=item.book,
                quantity=item.quantity
            )
            item.book.stockquantity -= item.quantity
            item.book.save()


        CartItem.objects.filter(cart=cart).delete()
        messages.success(request, "Заказ успешно оформлен!")
    except Exception as e:
        messages.error(request, f"Ошибка при оформлении заказа: {str(e)}")

    return redirect('cart_view')