#view api
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.decorators import api_view
from .serializers import Productserializer
from .models import Product

@api_view(['GET'])
def product_list_api(request):
    objects=Product.objects.all()[:50]
    data=Productserializer(objects,many=True).data
    return Response({'status':200,'all products':data})

@api_view(['GET'])
def product_detail_api(request,id):
    objects=Product.objects.get(id=id)
    data=Productserializer(objects).data
    return Response({'status':200,'product detail':data})

class ProductListAPI(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=Productserializer

class ProductDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=Productserializer