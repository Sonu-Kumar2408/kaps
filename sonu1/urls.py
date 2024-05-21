from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_view
from .forms import LoginForm,MyPasswordChangeForm,MyPasswordResetForm,MySetPasswordForm
from django.contrib.auth.views import LoginView
from django.urls import path
from .views import ProfileView


urlpatterns = [
    path('',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path("category/<slug:val>",views.CategoryView.as_view(),name="category"),
    path("category-title/<val>",views.CategoryTitle.as_view(),name="category-title"),
    path("product-details/<int:pk>",views.ProductDetail.as_view(),name="product-details"),
    path("profile/",views.ProfileView.as_view(),name="profile"),
    path("address/",views.address,name="address"),
    path("updateAddress/<int:pk>",views.UpdateAddress.as_view(),name="updateAddress"),
    path("registration/",views.RegistrationView.as_view(),name="registration"),
    path("login/", LoginView.as_view(template_name='sonu1/login.html'),  name='login'),
    path('cart/',views.show_cart,name='showcart'),
    path('add-to-cart/',views.add_to_cart,name='add_to_cart'),
    path('checkout/',views.Checkout.as_view(),name='checkout'),
    path('paymentdone/',views.payment_done,name='paymentdone'),
    path('orders/',views.home,name='orders'),
    path('pluscart/',views.plus_cart),
    path('minuscart/',views.minus_cart), 
    path('removecart/',views.remove_cart), 
    


    path("passwordchange/",auth_view.PasswordChangeView.as_view(template_name='sonu1/changepassword.html',
    form_class=MyPasswordChangeForm,success_url='sonu1/passwordchangedone'),name='passwordchange'),

    path("passwordchangedone/",auth_view.PasswordChangeDoneView.as_view
    (template_name='sonu1/passwordchangedone.html'),name='passwordchangedone'),
   
   
    path('password-reset/',auth_view.PasswordResetView.as_view
    (template_name='sonu1/password_reset.html',
    form_class=MyPasswordResetForm),name='password_reset'),
   
   
    path('password-reset/done/',auth_view.PasswordResetDoneView.as_view(template_name=
    'sonu1/password_reset_done.html'),name='password_reset_done'),
    
    
    path('password-reset-confirm/<uidb64>/<token>',
    auth_view.PasswordResetConfirmView.as_view(template_name=
    'sonu1/password_reset_confirm.html',form_class=MySetPasswordForm),name='password_reset_confirm'),
   
    path('password-reset-complete/',auth_view.PasswordResetCompleteView.as_view(template_name=
    'sonu1/password_reset_complete.html'),name='password_reset_complete'),
    
    
    
        
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   
