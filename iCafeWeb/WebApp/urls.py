from django.urls import path
from .views import *


urlpatterns = [
    path("menu/<int:cafe>/",Menu_Page,name='menu'),
    path("product/<int:pk>/",Product_Page,name='product'),
    path("cart/",Cart_Page,name='cart'),
    path("api/cart-count/",Tg_User,name='cart_count'),
]