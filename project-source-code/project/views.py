from django.shortcuts import render
from django.http import HttpResponse
#from . models import Post
from django.views.generic import ListView , DetailView

# Create your views here.

def home(request):
    return HttpResponse('<h2>Hello Bhailog !</h2>')

def base(request):
    return  render(request , 'project/base.html')

def home(request):
    return  render(request , 'project/home.html')
