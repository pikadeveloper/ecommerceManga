from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from .models import CartProducts
from .models import Cart
from .utils import get_or_create_cart
from tienda.models import Producto
# Create your views here.
def cart(request):
    cart = get_or_create_cart(request)

    return render(request, 'cart.html', {
        'cart':cart
    })

def add(request):
    cart = get_or_create_cart(request)
    producto = get_object_or_404(Producto, pk=request.POST.get('product_id'))
    quantity = int(request.POST.get('quantity', 1))

    # cart.products.add(producto, through_defaults={
    #     'quantity': quantity
    # })

    cart_product = CartProducts.objects.create_or_update_quantity(cart=cart, product=producto, quantity=quantity)

    return render(request, 'carts/add.html',{
        'producto': producto
    })

def remove(request):
    cart = get_or_create_cart(request)
    producto = get_object_or_404(Producto, pk=request.POST.get('product_id'))

    cart.products.remove(producto)

    return redirect('carts:cart')