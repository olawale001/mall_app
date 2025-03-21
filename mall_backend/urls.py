from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from shops.views import ShopViewSet, ProductViewSet, recommend_product, analysis_sentiment
from orders.views import OrderViewSet


router = DefaultRouter()
router.register(r'shops', ShopViewSet)
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/recommend/', recommend_product),
    path('api/sentiment/', analysis_sentiment),
]
