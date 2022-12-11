from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from utils.generate_code import generate_code
from products.models import Product
# Create your models here.



STATUS=(
    ('inprogress','inprogress'),
    ('compeleted','compeleted'),
   
)
class Cart(models.Model):
    code=models.CharField( max_length=8,default=generate_code)
    user=models.ForeignKey(User, related_name='user_cart', on_delete=models.SET_NULL,null=True,blank=True)

    status=models.CharField(choices=STATUS, max_length=10)

    def  __str__(self):
        return self.code
    


class CartDetail (models.Model):
    Cart==models.ForeignKey(Cart, related_name='cart_detail', on_delete=models.CASCADE)
    product= models.ForeignKey(Product,related_name='cart_product', on_delete=models.SET_NULL,null=True,blank=True)
    quantity=models.IntegerField()
    price=models.FloatField()
    total=models.FloatField()


    def __str__(self):
        return str(self.product)
    
    











STATUS=(
    ('recevied','recevied'),
    ('processed','processed'),
    ('shiped','shiped'),
    ('deliverd','deliverd'),
)
class Order(models.Model):
    code=models.CharField( max_length=8,default=generate_code)
    user=models.ForeignKey(User, related_name='user_order', on_delete=models.SET_NULL,null=True,blank=True)
    Order_time=models.DateField(default=timezone.now)
    delivery_time=models.DateField(null=True,blank=True)
    status=models.CharField(choices=STATUS, max_length=10)

    def  __str__(self):
        return self.code
    


class OrderDetail (models.Model):
    Order==models.ForeignKey(Order, related_name='order_detail', on_delete=models.CASCADE)
    product= models.ForeignKey(Product,related_name='order_product', on_delete=models.SET_NULL,null=True,blank=True)
    quantity=models.IntegerField()
    price=models.FloatField()
    total=models.FloatField()


    def __str__(self):
        return str(self.Order)
    
    
    

   