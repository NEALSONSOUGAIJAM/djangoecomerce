from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def home(request):
    template = loader.get_template('pages/app/index.html')
    return HttpResponse(template.render())

def signup(request):
    template = loader.get_template('pages/app/signin.html')
    return HttpResponse(template.render())


def register(request):
    template = loader.get_template('pages/app/register.html')
    return HttpResponse(template.render())

def product(request):
    template = loader.get_template('pages/app/product.html')
    return HttpResponse(template.render())

def cart(request):
    template = loader.get_template('pages/app/cart.html')
    return HttpResponse(template.render())

def productdet(request):
    template = loader.get_template('pages/app/product-detail.html')
    return HttpResponse(template.render())

def store(request):
    template =loader.get_template('pages/app/store.html')
    return HttpResponse(template.render())

def search(request):
    template = loader.get_template('pages/app/search-result.html')
    return HttpResponse(template.render())

def place(request):
    template = loader.get_template('pages/app/place-order.html')
    return HttpResponse(template.render())   

def order_complete(request):
    template = loader.get_template('pages/app/order_complete.html')
    return HttpResponse(template.render())

def dashboard(request):
    template = loader.get_template('pages/app/dashboard.html')
    return HttpResponse(template.render())                     