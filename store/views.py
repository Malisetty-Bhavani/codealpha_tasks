from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from .models import Product


# 🏠 HOME PAGE
def home(request):

    search = request.GET.get('search')

    if search:
        products = Product.objects.filter(name__icontains=search)
    else:
        products = Product.objects.all()

    return render(request, 'store/home.html', {
        'products': products
    })


# 🛒 ADD TO CART
def add_to_cart(request, product_id):

    cart = request.session.get('cart', [])

    if product_id not in cart:
        cart.append(product_id)

    request.session['cart'] = cart

    return redirect('/')


# 🛒 CART PAGE
def cart_view(request):

    cart = request.session.get('cart', [])

    products = Product.objects.filter(id__in=cart)

    total = sum(product.price for product in products)

    return render(request, 'store/cart.html', {
        'products': products,
        'total': total
    })


# ✅ CONFIRM ORDER
def confirm_order(request):

    request.session['cart'] = []

    return render(request, 'store/order_success.html')


# 🔐 LOGIN
def login_view(request):

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:
            login(request, user)
            return redirect('/')

        else:
            return render(request, 'store/login.html', {
                'error': 'Invalid Username or Password'
            })

    return render(request, 'store/login.html')


# 🆕 SIGNUP
def signup_view(request):

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():

            return render(request, 'store/signup.html', {
                'error': 'Username already exists'
            })

        User.objects.create_user(
            username=username,
            password=password
        )

        return redirect('/login/')

    return render(request, 'store/signup.html')