from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
# Create your views here.

class Category_Viewset(viewsets.ViewSet):
    @extend_schema(responses=CategorySerializer)
    def list(self,request):
        queryset=Category.objects.all()
        serializer=CategorySerializer(queryset,many=True,)
        return Response(serializer.data)



class Brand_Viewset(viewsets.ViewSet):
    @extend_schema(responses=BrandSerializer)
    def list(self,request):
        queryset=Brand.objects.all()
        serializer=BrandSerializer(queryset,many=True,)
        return Response(serializer.data)

class Product_Viewset(viewsets.ViewSet):
    @extend_schema(responses=ProductSerializer)
    def list(self,request):
        queryset=Product.objects.all()
        serializer=ProductSerializer(queryset,many=True,)
        return Response(serializer.data)
