from django.shortcuts import render,redirect
from django.http.response import JsonResponse
import telebot
from .models import *
# Create your views here.

def Menu_Page(request,cafe,user):
    cafe = User.objects.get(id=cafe)
    categorys = CategoryProduct.objects.filter(user=cafe)
    products = Product.objects.filter(category__user=cafe)
    try:
        user=TelegramUser.objects.get(tg_id=user,bot=cafe)
    except:
        user=TelegramUser.objects.create(tg_id=user,bot=cafe)
    count_cart = len(list(Cart.objects.filter(tg_user=user)))
    
    DATA = {
        "cafe":cafe,
        "categorys":categorys,
        "products":products,
        "count_cart":count_cart,
        "user":user,
    }
    return render(request,"starbelly/menu.html",DATA)

def Product_Page(request,pk,user):
    product = Product.objects.get(id=pk)
    cafe = User.objects.get(id=product.category.user.id)
    user = TelegramUser.objects.get(tg_id=user)
    count_cart = len(list(Cart.objects.filter(tg_user=user)))
    
    if request.method == 'POST':
        quantity = request.POST['quantity']
        Cart.objects.create(tg_user=user,product=product,quantity=quantity)

        return Cart_Page(request,cafe.id,user.tg_id)
        

    DATA = {
        "product":product,
        "cafe":cafe,
        "count_cart":count_cart,
        "user":user
    }
    return render(request,"starbelly/product.html",DATA)

def Cart_Page(request,cafe,user):
    cafe = User.objects.get(id=cafe)
    user = TelegramUser.objects.get(tg_id=user)
    carts = Cart.objects.filter(tg_user=user)
    cart_list = []
    subtotal_price = 0
    for i in carts:
        if i.product.category.user.id == cafe.id:
            cart_list.append(i)
            subtotal_price += i.product.price*i.quantity
            
    count_cart = len(cart_list)
    total = subtotal_price+cafe.order_price
    DATA = {
        "cafe":cafe,
        "user":user,
        "carts":cart_list,
        "count_cart":count_cart,
        "total":total,
        "subtotal_price":subtotal_price,
        
        
    }
    return render(request,"starbelly/cart.html",DATA)

def DelCart_Page(request,cart,user):
    cart = Cart.objects.get(id=cart)
    cafe = cart.product.category.user.id
    cart.delete()

    return redirect('cart',cafe,user)

def CheckOut_Page(request,cafe,user):
    cafe = User.objects.get(id=cafe)
    user = TelegramUser.objects.get(tg_id=user,bot=cafe)
    carts = Cart.objects.filter(tg_user=user)
    order = Order.objects.create(tg_user=user)
    subtotal_price = 0
    message_text = "<b>Buyurtma</b>"
    for i in carts:
        if i.product.category.user.id == cafe.id:
            item=OrderItem.objects.create(
                product=i.product,
                order=order,
                quantity=i.quantity,
            )
            subtotal_price += i.product.price*i.quantity
            i.delete()
            message_text+=f"\n{item.product.name}\n{item.quantity}x{item.product.price}={item.product.price*item.quantity}\n"
    total = subtotal_price+cafe.order_price
    message_text+=f"Mmumiy mahsulotlar narxi: {subtotal_price} so'm\nYetkazib berish narxi: {cafe.order_price} so'm\nUmumiy: {total} so'm"
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton("Tasdiqlash",callback_data=f'check-{order.id}'))
    markup.add(telebot.types.InlineKeyboardButton("Bekor qilish",callback_data=f'del-{order.id}'))
    
    tele = telebot.TeleBot(cafe.bot_token)
    tele.send_message(user.tg_id,message_text,parse_mode='HTML',reply_markup=markup)
    return redirect(f'https://t.me/{tele.get_me().username}')
