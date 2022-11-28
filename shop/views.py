from django.shortcuts import render
from django.http import HttpResponse

from .models import Product
# Create your views here.
def index(request):
    product=Product.objects.all()
    print(product)
    print(product[0].prod_name)
    return render(request,'shop/index.html')
def contact(request):
    return HttpResponse('<h2>contact Us </h2>') 
def about(request):
    return render(request,'shop/about.html') 
def checkout(request):
    return HttpResponse('<h2>check out </h2>') 
def productView(request):
    return HttpResponse('<h2>Product View </h2>') 
def search(request):
    return HttpResponse('<h2>Search</h2>') 
def tracker(request):
    return HttpResponse('<h2>tracker</h2>') 

