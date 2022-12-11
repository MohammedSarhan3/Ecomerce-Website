from django.shortcuts import render
from django.views.generic import ListView ,DetailView
from .models import Product,ProductImages ,Brand,Category
from django.db.models import Count,Q,F
# Create your views here.

def post_list(request):
    #objects=Product.objects.all()
    #objects=Product.objects.filter(price__range=(30,150))
    #objects=Product.objects.filter(category=10)
    #objects=Product.objects.filter(name__contains='sarah')
    #objects=Product.objects.filter(name__startswith='sa')
    #objects=Product.objects.filter(name__endswith='a')
    #objects=Product.objects.filter(desc__isnull=True)
    #objects=Product.objects.filter(quan__gt=10)
    #objects=Product.objects.filter(quan__gt=10,price=50)
   # objects=Product.objects.filter(
    #    Q(quan__gt=10)|
     #   ~Q(price__gt=50)
      #  )
    #objects=Product.objects.filter(quan=F('price'))
    #objects=Product.objects.order_by('name')
    #objects=Product.objects.order_by('-name')
    #objects=Product.objects.order_by('name','price')
    #objects=Product.objects.earliest('name')
    #objects=Product.objects.latest('name')
    #objects=Product.objects.price_greater_than(15)
    objects=Product.objects.price_range(185, 752)
    return render(request,'products/test_list.html',{"products":objects})
    
class ProductList(ListView):
    model =Product
    paginate_by = 100


class ProducDetail(DetailView):
    model =Product
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        myproduct=self.get_object()
        context["images"] =ProductImages.objects.filter(product=myproduct) 
        context["related"]=Product.objects.filter(category=myproduct.category)
        return context
    

class BrandList(ListView):
    model = Brand
   # paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brands"] =Brand.objects.all().annotate(product_count=Count('prodect_brand')) 
        return context
    

class BrandDetail(DetailView):
    model = Brand


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        brand=self.get_object()
        context["brand_products"] = Product.objects.filter(brand=brand)
        return context
    
    
class CategoryList(ListView):
    model =Category
    #paginate_by = 5
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] =Category.objects.all().annotate(product_count=Count('prodect_category')) 
        return context
   
