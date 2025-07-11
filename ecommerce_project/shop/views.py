from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Product, Order

def home(request):
    products = Product.objects.all()
    return render(request, 'shop/home.html', {'products': products})

def place_order(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        address = request.POST.get('address')
        order = Order(product=product, customer_name=customer_name, address=address)
        order.save()
        messages.success(request, "Your order has been placed successfully!")
        return render(request, 'shop/order_form.html', {
            'product': product,
            'order_placed': True
        })
    return render(request, 'shop/order_form.html', {
        'product': product,
        'order_placed': False
    })
