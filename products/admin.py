from django.contrib import admin


from .models import Product,ProductImages,ProductReview,Category , Brand
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

class ProductImageInline(admin.TabularInline):
    model=ProductImages


class ProductAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
    list_display=['name','price','flag']
    inlines=[ProductImageInline]


    







admin.site.register(Product,ProductAdmin)
admin.site.register(ProductImages)
admin.site.register(ProductReview)
admin.site.register(Category)
admin.site.register(Brand)
