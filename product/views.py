from django.shortcuts import render
from django.http import JsonResponse


from .models import *


def store(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'product/store.html', context)


def register(request):
    context = {}
    return render(request, 'product/register.html', context)


def login(request):
    context = {}
    return render(request, 'product/login.html', context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.order_item_set.all()
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total': 0}
    context = {'items': items, 'order': order}
    return render(request, 'product/cart.html', context)


def view(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.order_item_set.all()
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total': 0}
    context = {'items': items, 'order': order}
    return render(request, 'product/view.html', context)


def update_item(response):
    return JsonResponse("item was added", safe=False)
