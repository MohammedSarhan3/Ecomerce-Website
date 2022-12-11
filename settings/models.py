from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Company(models.Model):
    name= models.CharField(_("Name"), max_length=100)
    logo =models.ImageField(_("Logo"), upload_to="company")
    subtitle =models.CharField(_("Subtitle"),blank=True,null=True,max_length=2000)
    fb_link=models.URLField(_("FacebookLink"), blank=True,null=True)
    tw_link=models.URLField(_("TwaterLink"), blank=True,null=True)
    li_link=models.URLField(_("LinkedinLink"), blank=True,null=True)
    adress=models.TextField(_("Adress"),max_length=200)
    phone_number=models.TextField(_("PhoneNumber"),max_length=200)
    email=models.TextField(_("Email"),max_length=200)
    call_us=models.CharField(_("CallUs"), max_length=50)
    email_us=models.EmailField(_("EmailUS"), max_length=254)

    def __str__(self):
        return self.name
    

