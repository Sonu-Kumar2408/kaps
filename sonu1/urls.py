from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import *
urlpatterns = [
    path("",home),
    path("category/",views.CategoryView.as_view(),name='category'),

]