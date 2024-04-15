from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from . views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path(" ",home),
    path("catagory/",views.CatagoryView.as_view(),name='catagory'),

]