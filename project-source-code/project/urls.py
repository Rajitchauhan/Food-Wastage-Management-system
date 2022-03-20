from django.urls import path
from . import views

urlpatterns = [
    path('' , views.home , name="home"),
    path('base/' , views.base , name="base"),
    path('home/' , views.home , name="home"),
    ]
