import imp
from django.shortcuts import render
from .models import Product
import math
# Create your views here.
def index(req):
    p=Product.objects.all()
    n=len(p)
    slides=n//4+math.ceil((n/4)-(n//4))
    c=Product.objects.values('product_category')
    print(c)
    params=[[p,range(n),slides],[p,range(n),slides]]
    ap={'ap':params}
    return render(req,'home.html',ap)
def AddtoList(req):
    
    return render(req,'insert.html')    