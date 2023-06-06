from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=255,unique=True)
    phone = models.CharField(max_length=255,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    logo = models.ImageField(upload_to='logos/',null=True,blank=True)
    order_price = models.IntegerField(default=0)

    bot_token = models.CharField(max_length=500,null=True,blank=True)
    tg_group = models.CharField(max_length=255,null=True,blank=True)
    cafe_name = models.CharField(max_length=255,null=True,blank=True)
    theme_color = models.CharField(max_length=255,default="#F5C332")

    def __str__(self):
        return self.username

class TelegramUser(models.Model):
    tg_id = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    bot = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.tg_id

class CategoryProduct(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.user.cafe_name + " " + self.name


class Product(models.Model):
    category = models.ForeignKey(CategoryProduct,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    about = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name

class Cart(models.Model):
    tg_user = models.ForeignKey(TelegramUser,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.tg_user}-{self.product.name}-{self.quantity}-{self.date}"

class Order(models.Model):
    tg_user = models.ForeignKey(TelegramUser,on_delete=models.CASCADE)
    complete = models.BooleanField(default=False)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tg_user}-{self.date}-{self.complete}"

class OrderItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    date=models.DateTimeField(auto_now_add=True)

