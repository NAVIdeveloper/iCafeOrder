from django.urls import path
from .views import *


urlpatterns = [
    path("menu/<int:cafe>/<int:user>/",Menu_Page,name='menu'),
    path("product/<int:pk>/<int:user>/",Product_Page,name='product'),
    path("cart/<int:cafe>/<int:user>/",Cart_Page,name='cart'),
    path("del-cart/<int:cart>/<int:user>/",DelCart_Page,name='del-cart'),
    path("check-out/<int:cafe>/<int:user>/",CheckOut_Page,name='check-out'),   
    # path("add-cart/<int:pk>/<int:user>/",AddCart_Page,name='add-cart')
]