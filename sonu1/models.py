from django.db import models
from django.contrib.auth.models import User

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

STATE_CHOICES=(
    ('Andhra Pradesh','Andhra Pradesh'),
    ('Arunachal Pradesh','Arunachal Pradesh'),
    ('Assam','Assam'),
    ('Andaman and Nicobar Islands','Andaman and Nicobar Islands'),
    ('Bihar','Bihar'),
    ('Chandigarh','Chandigarh'),
    ('Chhattisgarh','Chhattisgarh'),
    ('Dadra and Nagar Haveli and Daman and Diu','Dadra and Nagar Haveli and Daman and Diu'),
    ('Delhi','Delhi'),
    ('Goa','Goa'),
    ('Gujarat','Gujarat'),
    ('Himachal Pradesh','Himachal Pradesh'),
    ('Jammu and Kashmir','Jammu and Kashmir'),
    ('Jharkhand','Jharkhand'),
    ('Karnataka','Karnataka'),
    ('Kerala','Kerala'),
    ('Ladakh','Ladakh'),
    ('Lakshadweep','Lakshadweep'),
    ('Madhya Pradesh','Madhya Pradesh'),
    ('Maharashtra','Maharashtra'),
    ('Manipur','Manipur'),
    ('Meghalaya','Meghalaya'),
    ('Mizoram','Mizoram'),
    ('Nagaland','Nagaland'),
    ('Odisha','Odisha'),
    ('Puducherry','Puducherry'),
    ('Punjab','Punjab'),
    ('Rajasthan','Rajasthan'),
    ('Sikkim','Sikkim'),
    ('Haryana','Haryana'),
    ('Tamil Nadu','Tamil Nadu'),
    ('Telangana','Telangana'),
    ('Tripura','Tripura'),
    ('Uttar Pradesh','Uttar Pradesh'),
    ('Uttarakhand','Uttarakhand'),
    ('West Bengal','West Bengal'),
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
    

class Customer(models.Model):
        user=models.ForeignKey(User,on_delete=models.CASCADE)
        name=models.CharField(max_length=100)
        locality=models.CharField(max_length=100)
        city=models.CharField(max_length=100)
        mobile=models.IntegerField(default=0)
        zipcode=models.IntegerField()
        state = models.CharField(choices=STATE_CHOICES,max_length=100)
        def __str__(self):
            return self.name
        

class Cart(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     product = models.ForeignKey(Product,on_delete=models.CASCADE)
     quantity = models.PositiveIntegerField(default=1)

     @property
     def total_cost(self):
          return self.quantity * self.product.discounted_price
