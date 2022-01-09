from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import get_object_or_404, render 

from basket.basket import Basket

from .models import Category, Product


def product_all(request):
    products = Product.products.all()
    return render(request, 'store/home.html', {'products': products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/products/detail.html', {'product': product})

def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/products/category.html', {'category': category, 'products': products })

def order_completed(request):
    basket = Basket(request)
    basket.clear()
    return render(request, 'store/payment/ordercompleted.html')   

def about(request):
    return render(request, 'store/about.html')

def contact(request):
    context = {}
    return render(request, 'store/contact.html')

def contact_success(request):
    context = {}
    return render(request, 'store/contact/contactsuccess.html') 




