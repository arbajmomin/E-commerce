from time import timezone
from django.db import models
from django.utils.timezone import datetime
from datetime import date
# Create your models here.
class Product(models.Model):
    prod_id= models.AutoField
    prod_date=models.DateField(default=date.today())
    prod_name= models.CharField(max_length=50)
    subcategory= models.CharField(max_length=50,default="")
    prod_desc= models.CharField(max_length=500)
    price= models.IntegerField(default=0)
    images=models.ImageField(upload_to="shop/images",default="")

    def __str__(self):
        return self.prod_name