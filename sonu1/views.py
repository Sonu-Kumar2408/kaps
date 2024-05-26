from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from urllib import request
from django.views import View
from .models import Product
from .models import Customer,Cart
from django.db.models import Count
from .forms import RegistrationForm,CustomerProfileForm
from django.contrib import messages
from django.db.models import Count,Q
from django.conf import settings
from .models import Payment,OrderPlace
import razorpay

# Create your views here.
def home(request):
    return render(request,"sonu1/home.html")

def about(request):
    return render(request,"sonu1/about.html")

def contact(request):
    return render(request,"sonu1/contact.html")


class CategoryView(View):
    def get(self,request,val):
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')
        return render(request,"sonu1/category.html",locals())
    
class CategoryTitle(View):
    def get(self,request,val):
        product = Product.objects.filter(title=val)
        title = Product.objects.filter(category=product[0].category).values('title')
        return render(request,"sonu1/category.html",locals())

class ProductDetail(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        return render(request,"sonu1/productdetails.html",locals())

class RegistrationView(View):
    def get(self,request):
        form = RegistrationForm()
        return render(request,'sonu1/registration.html',locals())
    def post(self,request):
        form =  RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Congratulation! User registered")
        else:
            messages.warning(request,"Invalid Input Data")
        return render(request,"sonu1/registration.html",locals())


class ProfileView(View):
    def get(self,request):
        form = CustomerProfileForm()
        return render(request,"sonu1/profile.html",locals())
    def post(self,request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']

            reg = Customer(user=user,name=name,locality=locality,city=city,
            mobile=mobile,state=state,zipcode=zipcode)
            reg.save()
            messages.success(request,"Congratulation! Profile saved successfully")
        else:
            messages.warning(request,"Invalid Input Date")
        return render(request,"sonu1/profile.html",locals())


def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request,"sonu1/address.html",locals())

class UpdateAddress(View):
    def get(self,request,pk):
        add= Customer.objects.get(pk=pk)
        form=CustomerProfileForm(instance=add)
        return render(request,"sonu1/updateaddress.html",locals())
    def post(self,request,pk):
        form=CustomerProfileForm(request.POST)
        if form.is_valid():
            add = Customer.objects.get(pk=pk)
            add.name = form.cleaned_data['name']
            add.locality = form.cleaned_data['locality']
            add.city = form.cleaned_data['city']
            add.mobile = form.cleaned_data['mobile']
            add.state = form.cleaned_data['state']
            add.zipcode = form.cleaned_data['zipcode']
            add.save()
            messages.success(request,"Congratulations! Address Updated successfully")
        else:
            messages.warning(request,"Invalid Input Data")
        return redirect("address")

def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user,product=product).save()
    return redirect("/cart")

def show_cart(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    amount=0
    for p in cart:
        value = p.quantity * p.product.discounted_price
        amount = amount + value
    totalamount = amount + 40
    return render(request,'sonu1/addtocart.html',locals())

class Checkout(View):
    def get(self,request):
        user = request.user
        add = Customer.objects.filter(user=user)
        cart_items = Cart.objects.filter(user=user)
        final_amount = 0
        for a in cart_items:
            value = a.quantity * a.product.discounted_price
            final_amount = final_amount + value
        totalamount = final_amount + 40
        razoramount = int(totalamount * 100)
        client = razorpay.Client(auth=(settings.RAZOR_KEY_ID,settings.RAZOR_KEY_SECRET))
        data = {"amount":razoramount,"currency":"INR","receipt":"order_rcptid_12"}
        payment_response = client.order.create(data=data)
        print(payment_response)
        # {'id': 'order_OCH2eMzzCjjQcm', 'entity': 'order', 'amount': 504000, 'amount_paid': 0, 'amount_due': 504000, 'currency': 'INR', 'receipt': 'order_rcptid_12', 'offer_id': None, 'status': 'created', 'attempts': 0, 'notes': [], 'created_at': 1716104576}
        order_id = payment_response['id']
        order_status = payment_response['status']
        if order_status == 'created':
            payment = Payment(
                user=user,
                amount = totalamount,
                razorpay_order_id = order_id,
                razorpay_payment_status = order_status
            )
            payment.save()
        return render(request,'sonu1/checkout.html',locals())
    
def payment_done(request):
    order_id=request.GET.get('order_id')
    payment_id = request.GET.get('payment_id')
    cust_id=request.GET.get('cust_id')
    # print("payment_done":oil = ",order_id," pid = ",payment_id," cid = ",cust_id")
    user = request.user
    # return redirect("orders")
    customer = Customer.objects.get(id=cust_id)
     # To update payment status and payment id
    payment = Payment.objects.get(razorpay_order_id=order_id)
    payment.paid = True
    payment.razorpay_payment_id = payment_id
    payment.save()
    # To save order details
    cart = Cart.objects.filter(user=user)
    for c in cart:
        OrderPlace(user=user,customer=customer,product=c.product,quantity=c.quantity,payment=payment).save()
        c.delete()


def orders(request):
    order_placed = OrderPlace.objects.filter(user=request.user)
    return render(request,'sonu1/orders.html',locals())

def plus_cart(request):
    if request.method == "GET":
        prod_id=request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity+=1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for c in cart:
            value = c.quantity * c.product.discounted_price
            amount = amount + value
        totalamount = amount + 40
        data = {
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount
        }
        return JsonResponse(data)
    

def minus_cart(request):
    if request.method == "GET":
        prod_id=request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity-=1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for c in cart:
            value = c.quantity * c.product.discounted_price
            amount = amount + value
        totalamount = amount + 40
        data = {
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount
        }
        return JsonResponse(data)
    
def remove_cart(request):
    if request.method == "GET":
        prod_id=request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for c in cart:
            value = c.quantity * c.product.discounted_price
            amount = amount + value
        totalamount = amount + 40
        data = {
            'amount':amount,
            'totalamount':totalamount
        }
        return JsonResponse(data)
    




