from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from shops.views import ShopViewSet, ProductViewSet
from orders.views import OrderViewSet

router = DefaultRouter()
router.register(r'shops', ShopViewSet)
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
