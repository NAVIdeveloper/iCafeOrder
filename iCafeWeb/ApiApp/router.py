from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('category', Viewset_Api_CategoryProduct)
router.register('product', Viewset_Api_Product)
