from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from . models import Product
from urllib import request

def home(request):
    return render(request,"sonu1/home.html")


class CatagoryView(View):
    def get(self,request,val):
        product = Product.objects.filter(catagory=val)
        title = Product.objects.filter(catagory=val).values('title')
        return render(request,"sonu1/catagory.html")


