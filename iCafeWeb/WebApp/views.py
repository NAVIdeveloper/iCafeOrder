from django.shortcuts import render
from django.http.response import JsonResponse
from .models import *
# Create your views here.

def Menu_Page(request,cafe):
    cafe = User.objects.get(id=cafe)
    categorys = CategoryProduct.objects.filter(user=cafe)
    products = Product.objects.filter(category__user=cafe)
    
    DATA = {
        "cafe":cafe,
        "categorys":categorys,
        "products":products,
    }
    return render(request,"starbelly/menu.html",DATA)

def Product_Page(request,pk):
    product = Product.objects.get(id=pk)
    cafe = User.objects.get(id=product.category.user.id)
    if request.method == 'POST':
        quantity = request.data['quantity']
        tg_id = request.data['tg_id']
        print(tg_id)
        print(quantity)
        

    DATA = {
        "product":product,
        "cafe":cafe,
    }
    return render(request,"starbelly/product.html",DATA)

def Cart_Page(request):
    DATA = {

    }
    return render(request,"starbelly/cart.html",DATA)




def Tg_User(request):
    tg_id = request.GET['tg_id']
    cafe = request.GET['cafe']
    bot = User.objects.get(id=cafe)
    try:
        user=TelegramUser.objects.get(tg_id=tg_id,bot=bot)
    except:
        user=TelegramUser.objects.create(tg_id=tg_id,bot=bot)
    count_cart = len(list(Cart.objects.filter(tg_user=user)))
    
    DATA = {
        "count_cart":count_cart,
    }

    return JsonResponse(DATA)
