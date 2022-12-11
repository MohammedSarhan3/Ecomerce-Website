from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User
from utils.generate_code import generate_code
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,related_name='user_profile', on_delete=models.CASCADE)
    image=models.ImageField(upload_to='users')

    code= models.CharField(max_length=10,default=generate_code)
    code_used=models.BooleanField(default=False)
    active=models.BooleanField(default=False)



@receiver(post_save, sender=User)


def creat_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
        



DATA_TYPE=(
    ('Home','Home'),
    ('Office','Office'),
    ('Academy','Academy'),
    ('Others','Others'),
)

class UserPhoneNumber(models.Model):
    user=models.ForeignKey(User,related_name='user_phone', on_delete=models.CASCADE)
    number=models.CharField(max_length=15)
    type=models.CharField(choices=DATA_TYPE,max_length=10)


class UserAdress(models.Model):
    user=models.ForeignKey(User,related_name='user_adress', on_delete=models.CASCADE)
    type=models.CharField(choices=DATA_TYPE,max_length=10)
    country=CountryField()
    city=models.CharField(max_length=30)
    state=models.CharField(max_length=30)
    region=models.CharField(max_length=30)
    street=models.CharField(max_length=80)
    notes=models.CharField(max_length=300)