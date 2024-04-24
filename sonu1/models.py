from django.db import models

# Create your models here.

CATAGORY_CHOICES=(
    ('CP','Cappuccino'),
    ('LT','Latte'),
    ('FC','Frappuccino'),    
    ('M','Mocha '),    
    ('AM','Americano'),    
    ('IC','Irish Coffee'),    
    ('LB','Long Black'),    
    ('DP','Doppio'),    
    ('FW','Flat White'),    
    ('MT','Macchiato'),    

)
class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    discription = models.TextField()
    composition = models.TextField(default='')
    prodapp = models.TextField(default='')
    category = models.CharField(choices= CATAGORY_CHOICES,max_length=2)
    product_image = models.ImageField(upload_to='product')
    def __str__(self):
        return self.title