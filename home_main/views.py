from django.shortcuts import render

# Create your views here.

# from .models import Product, PCB, Switch, Keyboard, KeyCap


def product_all(request):
    return render(request, 'home_main/index.html')
