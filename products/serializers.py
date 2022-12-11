#like form file
from rest_framework import  serializers
from .models import Product,Category,Brand


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'
        

class Productserializer(serializers.ModelSerializer):
    category=CategorySerializer()
    brand=serializers.StringRelatedField()
    price_with_tax=serializers.SerializerMethodField(method_name='price_with_tax1')
    def price_with_tax1(self,product):
        return product.price*1.1
    class Meta:
        model=Product
        fields=['id','category','brand','name','sku','subtitle','desc','flag','price','image','video_url','quan','price_with_tax']
            
    
