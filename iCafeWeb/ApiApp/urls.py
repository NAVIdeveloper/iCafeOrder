from django.urls import path,include
from .router import router
from .views import *

urlpatterns = [
	path("",include(router.urls)),
	
	path("tguser/",Api_GetTgUser),
	path("login/",Api_Login),
    path("info/",Api_Info),
]