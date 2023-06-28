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
		queryset = self.queryset.filter(user=self.request.user)
		return queryset

class Viewset_Api_Product(viewsets.ModelViewSet):
	queryset = Product.objects.all()
	serializer_class = LoaderProduct
	permission_classes = [AllowAny]

	def get_queryset(self):
		return self.queryset.filter(category__user=self.request.user)
	


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
	return Response(data)
