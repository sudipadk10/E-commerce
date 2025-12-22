from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


def test(request):
    return HttpResponse("Hello Guys")

def index(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request,'index.html',context)

def login(request):
    return render(request,'login.html')