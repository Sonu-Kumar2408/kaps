from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
# from django.contrib.auth import views as auth_view
# from .forms import LoginForm
from django.contrib.auth.views import LoginView
from django.urls import path
from .views import ProfileView


urlpatterns = [
    path('',views.home),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path("category/<slug:val>",views.CategoryView.as_view(),name="category"),
    path("category-title/<val>",views.CategoryTitle.as_view(),name="category-title"),
    path("product-details/<int:pk>",views.ProductDetail.as_view(),name="product-details"),
    path("profile/",views.ProfileView.as_view(),name="profile"),
    path("address/",views.ProfileView.as_view(),name="address"),
    path("registration/",views.RegistrationView.as_view(),name="registration"),
    path("login/", LoginView.as_view(template_name='sonu1/login.html'),  name='login'),
    # path("account/login/", auth_view.LoginViews.as_view(temeplete_name='sonu1/login.html',
    #                         authentication_form=LoginForm),name='login'),
    
    
   
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   
