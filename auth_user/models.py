from django.db import models
from django.contrib.auth.models import User
from .constants import GENDER_TYPE


class ShopUserAccount(models.Model):
    user = models.OneToOneField(User,related_name='account', on_delete=models.CASCADE)
    account_no = models.IntegerField(unique=True)
    birth_date = models.DateField(null=True,blank=True)
    gender = models.CharField(max_length=100, choices=GENDER_TYPE)
    profile_picture = models.ImageField(upload_to='auth_user/media/uploads/', blank = True, null = True)
    phone_no = models.CharField(max_length = 11)

    def __str__(self):
        return self.user.username
    

class UserAddress(models.Model):
   user = models.OneToOneField(User,related_name='address', on_delete=models.CASCADE)
   postal_code = models.IntegerField()
   street_address = models.CharField(max_length=100)
   city = models.CharField(max_length=100)
   country = models.CharField(max_length=100)
   def __str__(self):
        return self.user.username