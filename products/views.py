from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Product

def index(request):
    lastes_products_list = Product.objects.order_by("-created_at")[:5]
    output = ", ".join([q.name for q in lastes_products_list])
    return HttpResponse(output)
