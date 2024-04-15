from django.db import models

# Create your models here.

CATAGORY_CHOICE=(
    ('ml','milk coffee'),
    ('Cf','coffee'),
    ('C','coff')
)
class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    discription = models.TextField()
    composition = models.TextField()
    prodapp = models.TextField()
    catagory = models.CharField(choices= CATAGORY_CHOICE,max_length=2)
    product_image = models.ImageField(upload_to='product')
    def __str__(self):
        return self.title