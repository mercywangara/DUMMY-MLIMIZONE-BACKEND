from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import CropViewset, MarketPriceViewset

router = DefaultRouter()
router.register(r"crop", CropViewset, basename="crop")
router.register(r"marketprice", MarketPriceViewset, basename="markerprice")

urlpatterns = [
    path("", include(router.urls)),
    
]