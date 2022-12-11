from django.urls import path
from .views import signup,user_activate,profile
app_name='accounts'

urlpatterns = [

    path('signup',signup,name='signup'),
    path('profile',profile,name='profile'),
    path('<str:username>/activate',user_activate,name='user_activate')

]
