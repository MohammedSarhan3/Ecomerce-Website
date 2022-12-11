from django.urls import path
from .views import ProductList,ProducDetail,BrandList,BrandDetail,CategoryList,post_list
from .api import product_list_api,product_detail_api,ProductListAPI,ProductDetailAPI

app_name='products'
urlpatterns = [
    path("testing/", post_list ),
    path('',ProductList.as_view(),name='product_list'),
    path('<int:pk>',ProducDetail.as_view(),name='product_detail'),
    path('brands/',BrandList.as_view(),name='brand_list'),
    path('brands/<int:pk>',BrandDetail.as_view(),name="brand_detail"),
    path('category/',CategoryList.as_view(),name='category_list'),

    #apiproduct_detail_api
    path('api/',product_list_api),
    path('api/<int:id>',product_detail_api),
    path('api/cbv',ProductListAPI.as_view()),
        path('api/cbv/<int:pk>',ProductDetailAPI.as_view()),



]
