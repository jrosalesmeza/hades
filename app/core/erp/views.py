from django.http.response import JsonResponse
from django.shortcuts import render

from django.http import HttpResponse,JsonResponse


from core.erp.models import *

# Create your views here.


def myfristview(request):
    
    data= {
        'name': 'Jose',
        'categories': Category.objects.all
    }
    return render(request, 'index.html',data)

def secondview(request):

    data= {
        'name': 'Jose',
        'products': Product.objects.all
    }
    return render(request, 'second.html',data)