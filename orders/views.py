from django.shortcuts import render,get_object_or_404,redirect
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from orders.forms import *
from catalog.models import *
from orders.cart import *


# this function is to use index page 
#  let try to understooded this function process
# this function is to get all product which is to watch your index.page
def product_list(request):
    context = {}
    context['products'] = Product.objects.all().order_by('-id')
    return render(request,'product/product_list.html',context)

# this function to use which you need to add a cart to buy maybe this product you to click detail which is you cliced on product
def product_detail(request,id):
    context = {}
    context['product_detail'] = get_object_or_404(Product,id = id)
    context['cart_product_form'] = CartAddProductForm()
    return render(request,'product/product_detail.html',context)


# this function to use add cart when you click details and to watch input, How many do yo need from this product and you click add to cart.
# Next when you clicked button (add to cart) this will add in dictionary 
@require_POST
def cart_add(request,product_id):
    cart = Cart(request)
    product = get_object_or_404(Product,id = product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,quantity=cd['quantity'],overide_quantity=cd['overide'])
    return redirect('cart_detail')

# this function to use to remove in cart product
def cart_remove(request,product_id):
    cart = Cart(request)
    product = get_object_or_404(Product,id = product_id)
    cart.remove(product)
    return redirect('cart_detail')

# this function to use to watch detail how many product you add your cart and you see total price
def cart_detail(request):
    cart = Cart(request)
    return render(request,'cart/cart_detail.html',{'cart':cart})


