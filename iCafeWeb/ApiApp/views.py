from WebApp.models import *

# Create your views here.
from django.db.models import Max,Min,Q as SearchQ
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.decorators import authentication_classes,permission_classes
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets
# from rest_framework.decorators import action
# from django.contrib.auth import authenticate

from .serializers import *

class Viewset_Api_CategoryProduct(viewsets.ModelViewSet):
	queryset = CategoryProduct.objects.all()
	serializer_class = LoaderCategoryProduct
	permission_classes = [IsAuthenticated]
    
	def get_queryset(self):
		queryset = self.queryset.filter(user=self.request.user).order_by('id')
		return queryset
	
	def perform_create(self, serializer):
		serializer.save(user=self.request.user)

class Viewset_Api_Product(viewsets.ModelViewSet):
	queryset = Product.objects.all()
	serializer_class = LoaderProduct
	permission_classes = [AllowAny]

	def get_queryset(self):
		return self.queryset.filter(category__user=self.request.user).order_by('id')

	def update(self, request, *args, **kwargs):
		print(request.data)
		obj = Product.objects.get(id=kwargs['pk'])
		if 'image' in request.data:
			obj.image = request.data['image']
		obj.name=request.data['name']
		obj.category=CategoryProduct.objects.get(id=request.data['category'][0])
		obj.price=request.data['price']
		obj.about=request.data['about']
		obj.save()
		return Response(LoaderProduct(obj).data)

	def create(self, request, *args, **kwargs):
		pro = Product.objects.create(
			name=request.data['name'],
			category=CategoryProduct.objects.get(id=request.data['category'][0]),
			price=request.data['price'],
			about=request.data['about'],
			image=request.data['image'],
		)
		return Response(LoaderProduct(pro).data)
	
	# def perform_create(self, serializer):
	# 	serializer.save(user=self.request.user)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def Api_GetTgUser(request):
	return Response(
		LoaderTelegramUser(
			TelegramUser.objects.filter(bot=request.user),
			many=True
			)
		)

@api_view(['POST'])
@permission_classes([AllowAny])
def Api_Login(request):
	username = request.POST['username']
	password = request.POST['password']
	data = {
		"status":False
	}
	try:
		user=User.objects.get(username=username)
		print(user.password)
		if user.password == password:
			data['status'] = True
			data['token'] = Token.objects.get(user=user).key
	except:
		pass

	return Response(data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def Api_Info(request):
	data = LoaderUser(request.user).data
	total_sum = 0
	cp_orders = Order.objects.filter(tg_user__bot=request.user,complete=True)
	for i in cp_orders:
		items = OrderItem.objects.filter(order=i)
		for t in items:
			total_sum += t.quantity*t.price

	return Response(
		{
			"cafe":data,
			"count_order":len(list(Order.objects.filter(tg_user__bot=request.user))),
			"total_sum":total_sum,
			"count_user":len(list(TelegramUser.objects.filter(bot=request.user))),
			"count_product":len(list(Product.objects.filter(category__user=request.user))),
		}
	)
