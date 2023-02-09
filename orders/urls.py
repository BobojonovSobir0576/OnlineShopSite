from django.urls import path
from orders.views import *

urlpatterns = [
    path('product_list/',product_list,name='product_list'),
    path('product_detail/<int:id>/',product_detail,name='product_detail'),
    path('product_detail_in_cart/',cart_detail,name='cart_detail'),
    path('product_add_cart/<int:product_id>/',cart_add,name='cart_add'),
    path('product_remove_in_cart/<int:product_id>/',cart_remove,name='cart_remove'),
]
