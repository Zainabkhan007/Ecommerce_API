from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
router=DefaultRouter()
router.register("category",views.Category_Viewset,basename='views')
router.register("brand",views.Brand_Viewset,basename='views')
router.register("product",views.Product_Viewset,basename='views')

urlpatterns = [
path("",include(router.urls)),
path("schema/",SpectacularAPIView.as_view(), name='schema'),
path("docs/", SpectacularSwaggerView.as_view(), name="docs"),
]