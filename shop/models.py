from django.db import models

# Create your models here.
class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=120 , default="")
    product_desc=models.CharField(max_length=200 , default="")
    product_price=models.IntegerField(default=0)
    product_category=models.CharField(max_length=200 , default="")
    product_image=models.ImageField(upload_to='shop/images',  default="")
    product_premium=models.BooleanField(default=False)
    def __str__(self) :
        return self.product_name