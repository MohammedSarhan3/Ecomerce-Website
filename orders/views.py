from django.shortcuts import render
from products.models import Product
from .models import Cart, CartDetail, Order, OrderDetail

# Create your views here.


def add_to_cart(request):
    if request.method == "POST" :
        product_id = request.POST['product_id']
        quantity = request.POST['quantity']
        
        product = Product.objects.get(id=product_id)
        cart = Cart.objects.get(user=request.user, status='inprogress')
        cart_detail, created = CartDetail.objects.get_or_create(
            cart=card,
            product=product
        )
        cart_detail.quantity = int(quantity)
        cart_detail.price = product.price
        cart_detail.total = int(quantity) * product.price
        cart_detail.save()
    