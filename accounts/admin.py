from django.contrib import admin
from .models import Profile,UserPhoneNumber, UserAdress
# Register your models here.
admin.site.register(Profile)
admin.site.register(UserAdress)
admin.site.register(UserPhoneNumber)
