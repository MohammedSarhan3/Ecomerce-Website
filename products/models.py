from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import Avg
from taggit.managers import TaggableManager

PRODUCT_FLAG={
    ('New','New'),
    ('Feature','Feature'),
    ('Sale','Sale')
}

class ProductManger(models.Manager):
    def price_greater_than(self,price):
        return self.filter(price__gt=price)

    def price_range(self,start,end):
        return self.filter(price__range=(start,end))


class Product(models.Model):
    name=models.CharField(_('Name'),max_length=100)
    sku=models.IntegerField(_('SKU'))
    subtitle=models.CharField(_('Subtitle'),max_length=300)
    desc=models.TextField(_('Descreption'),max_length=10000)
    flag=models.CharField(_('Flag'),max_length=10,choices=PRODUCT_FLAG)
    price=models.FloatField(_('Price'))
    image=models.ImageField(_('Image'), upload_to='products')
    tags=TaggableManager()
    category = models.ForeignKey('Category',verbose_name=_('Category'),related_name='prodect_category',on_delete=models.SET_NULL,null=True,blank=True)
    brand = models.ForeignKey('Brand',verbose_name=_('Brand'),related_name='prodect_brand',on_delete=models.SET_NULL,null=True,blank=True)
    video_url = models.URLField(null=True,blank=True)
    quan=models.IntegerField(default=50)

    objects=ProductManger()
    def __str__(self):
        return self.name

    def get_avg(self):
        avg =self.product_review.aggregate(myavg=Avg('rate'))
        return avg



    def get_avg2(self):
        rate_sum=0
        product_review=self.product_review.all()
        for review in product_review:
            rate_sum+=review.rate
        avg=rate_sum/len(product_review)
        return avg


class ProductImages(models.Model):
    product=models.ForeignKey(Product,verbose_name=_('Product'),related_name='product_image',on_delete=models.CASCADE)
    image=models.ImageField(verbose_name=_('Image'),upload_to='productimages')
    
    def __str__(self):
        return str(self.product)




class Category(models.Model):
    name=models.CharField(_('Name'),max_length=100)
    image=models.ImageField(_('Image'),upload_to='category')

    def __str__(self):
        return self.name



class Brand(models.Model):
    name=models.CharField(_('Name'),max_length=100)
    image=models.ImageField(_('Image'),upload_to='brand')

    def __str__(self):
        return self.name


class ProductReview(models.Model):
    user=models.ForeignKey(User,related_name='user_review',on_delete=models.SET_NULL,null=True,blank=True)
    product= models.ForeignKey(Product,verbose_name=_('Product'),related_name='product_review',on_delete=models.SET_NULL,null=True,blank=True)
    rate= models.IntegerField(verbose_name=_('Rate'))
    review=models.CharField(verbose_name=_('Review'),max_length=300)
    created_at=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.product)