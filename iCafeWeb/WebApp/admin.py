from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(TelegramUser)
admin.site.register(CategoryProduct)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(User)