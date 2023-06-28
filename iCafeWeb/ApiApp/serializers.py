from rest_framework.serializers import ModelSerializer
from WebApp.models import *

# ModelSerializer

class LoaderUser(ModelSerializer):
	class Meta:
		model = User
		fields =  "__all__"

class LoaderCategoryProduct(ModelSerializer):
	class Meta:
		model = CategoryProduct
		fields = "__all__"

class LoaderTelegramUser(ModelSerializer):
	class Meta:
		model = TelegramUser
		fields = "__all__"

class LoaderProduct(ModelSerializer):
	category = LoaderCategoryProduct(read_only=True)
	class Meta:
		model = Product
		fields =  "__all__"

class LoaderOrder(ModelSerializer):
	class Meta:
		model = Order
		fields =  "__all__"
