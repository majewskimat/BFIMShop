from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import get_object_or_404, render 

from store.models import Category, Product

# Create your views here.

def categories(request):
    return {
        'categories': Category.objects.all()
    }

def products(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/products/detail.html', {'product': product})


def store(request):
    context = {}
    return render(request, 'store/store.html', context)

def about(request):
    context = {}
    return render(request, 'store/about.html', context)

def contact(request):
    context = {}
    return render(request, 'store/contact.html', context)

def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Utworzono konto dla {username}!')
            return redirect('blog-home')
    else:
        form = UserCreationForm()
    return render(request, 'store/register.html', {'form': form})

